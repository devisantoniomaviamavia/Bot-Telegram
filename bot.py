python
import sqlite3, os
from flask import Flask
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "7999705337:AAHSVp2GmGxitTXGogm_7cwwTzr5tX51NHE"
ADMIN_ID = 7572728909
app = Flask(_name_)

Banco de dados
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, saldo REAL DEFAULT 0)")
conn.commit()

def add_user(user_id):
    cursor.execute("INSERT OR IGNORE INTO users (id) VALUES (?)", (user_id,))
    conn.commit()

def update_saldo(user_id, valor):
    cursor.execute("UPDATE users SET saldo = saldo + ? WHERE id = ?", (valor, user_id))
