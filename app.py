import os
import subprocess
import tempfile
from pathlib import Path

from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {"mp3", "wav", "flac", "ogg", "m4a"}

app = Flask(__name__)


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def run_ffmpeg(input_path: Path, output_path: Path, mode: str) -> None:
    """
    mode='vocals' gera uma aproximação da voz por cancelamento de fase (L-R).
    mode='instrumental' gera uma aproximação instrumental removendo o centro.
    """
    if mode == "vocals":
        filter_complex = "pan=stereo|c0=c0-c1|c1=c1-c0,highpass=f=120,lowpass=f=8000"
    elif mode == "instrumental":
        filter_complex = "pan=stereo|c0=c0-c1|c1=c1-c0,volume=-1[a];[0:a][a]amix=inputs=2:weights='1 1'"
    else:
        raise ValueError("Modo inválido")

    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        str(input_path),
        "-filter_complex",
        filter_complex,
        "-vn",
        str(output_path),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "Falha no ffmpeg")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    file = request.files.get("audio")
    mode = request.form.get("mode", "vocals")

    if not file or not file.filename:
        return render_template("index.html", error="Envie um arquivo de áudio."), 400

    if not allowed_file(file.filename):
        return render_template("index.html", error="Formato não suportado."), 400

    with tempfile.TemporaryDirectory() as tmpdir:
        filename = secure_filename(file.filename)
        input_path = Path(tmpdir) / filename
        output_name = f"{Path(filename).stem}_{mode}.wav"
        output_path = Path(tmpdir) / output_name

        file.save(input_path)

        try:
            run_ffmpeg(input_path, output_path, mode)
        except Exception as exc:  # noqa: BLE001
            return render_template("index.html", error=f"Erro ao processar: {exc}"), 500

        return send_file(
            output_path,
            as_attachment=True,
            download_name=output_name,
            mimetype="audio/wav",
        )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
