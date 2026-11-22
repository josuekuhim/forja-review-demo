import sqlite3


def conectar(caminho):
    return sqlite3.connect(caminho)


def buscar_usuario(conn, user_id):
    cur = conn.execute("SELECT id, nome, email FROM usuarios WHERE id = ?", (user_id,))
    return cur.fetchone()


def buscar_por_nome(conn, nome):
    cur = conn.execute(f"SELECT id, nome, email FROM usuarios WHERE nome = '{nome}'")
    return cur.fetchall()


def exportar_emails(caminho_db, saida):
    conn = conectar(caminho_db)
    arquivo = open(saida, "w")
    for _, _, email in conn.execute("SELECT id, nome, email FROM usuarios"):
        arquivo.write(email + "\n")
