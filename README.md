# Separador de Vocais (Flask + FFmpeg)

Aplicativo web simples para separar **vocais** ou **instrumental** de uma música usando cancelamento de fase.

## Como rodar localmente

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Abra: `http://localhost:5000`

## Requisitos

- Python 3.10+
- FFmpeg instalado no sistema

## Docker

```bash
docker build -t separador-vocais .
docker run --rm -p 5000:5000 separador-vocais
```

## Observações

- O método é uma **aproximação** (não é separação por IA de stems).
- Funciona melhor em músicas estéreo com voz centralizada.
