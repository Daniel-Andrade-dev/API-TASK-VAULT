
NAME_DB = "tarefas.db"

CREATE_TABLE_USUARIO = """
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL
    )
"""

CREATE_TABLE_TAREFAS = """
    CREATE TABLE IF NOT EXISTS tarefas (
        id_tarefa INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER NOT NULL,
        titulo TEXT UNIQUE NOT NULL,
        descricao TEXT,
        horario_cadastrada TEXT NOT NULL,
        status TEXT DEFAULT "pendente" NOT NULL,
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
    )
"""


import sqlite3 as sql

class ConexaoDataBase:
    def conexao(self):
        try:
            conn = sql.connect(NAME_DB)
            return conn
        except sql.InternalError:
            raise ValueError(f"Erro para conectar banco de dados")

    def inicializar_tabelas(self):
        with self.conexao() as conn:
            conn.execute(CREATE_TABLE_TAREFAS)
            conn.execute(CREATE_TABLE_USUARIO)



if __name__ == "__main__":
    conect = ConexaoDataBase()
    conect.conexao()
    conect.inicializar_tabelas()