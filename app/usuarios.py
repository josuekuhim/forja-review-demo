import sqlite3


def conectar(caminho):
    return sqlite3.connect(caminho)


def buscar_usuario(conn, user_id):
    cur = conn.execute("SELECT id, nome, email FROM usuarios WHERE id = ?", (user_id,))
    return cur.fetchone()
