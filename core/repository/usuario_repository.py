from core.domain.usuario.usuario import Usuario
from core.schema.tabelas import NAME_DB
from core.cript_senha.cript import gerar_hash
import sqlite3 as sql



class UsuarioRepository:
    def conect_database(self):
        try:
            conn = sql.connect(NAME_DB)
            conn.row_factory = sql.Row
            return conn
        except sql.InternalError:
            raise ValueError(f"Erro para fazer conexão ao banco")

    def cadastra_usuario_repository(self, usuario_obj) -> dict:
        try:
            with self.conect_database() as conn:
                if isinstance(usuario_obj, Usuario):
                    cur = conn.execute(
                        """ 
                        INSERT INTO usuarios
                        (email,senha)
                        VALUES(?,?)
                        """,(usuario_obj.email,gerar_hash(usuario_obj.senha))
                    )

                    usuario_id: int = cur.lastrowid

                    usuario_obj = Usuario(
                        usuario_id,
                        usuario_obj.email,
                        usuario_obj.senha
                    )

                    return {
                        "usuario_id": usuario_id,
                        "email": usuario_obj.email,
                        "senha": gerar_hash(usuario_obj.senha)
                    }
                return {"erro": "Objeto inválido obtido"}
            
        except sql.IntegrityError:
            return {
                "sucesso": False,
                "erro": "Conta já está cadastrada"
            }
        except sql.Error as e:
            raise ValueError(f"Erro ao cadastra usuário para o banco >> {e}")

    def login_usuario_repository(self, email: str) -> dict | None:
        try:
            with self.conect_database() as conn:
                cur = conn.execute(
                    """
                    SELECT 
                        id_usuario,
                        email,
                        senha AS hash 
                    FROM usuarios WHERE email = ?
                    """,(email,)
                )

                usuario = cur.fetchone()

                if usuario:
                    return {
                        "id_usuario": usuario['id_usuario'],
                        "email": usuario['email'],
                        "hash": usuario['hash']
                    }
                else:
                    return None
        except sql.Error as e:
            raise ValueError(f"Erro ao fazer login do usuário >> {e}")

    def buscar_usuario_repository(self, email: str) -> dict | None:
        try:
            with self.conect_database() as conn:
                cur = conn.execute(
                    """
                    SELECT 
                        id_usuario, 
                        email
                    FROM usuarios WHERE email = ?
                    """,(email,)
                )

                usuario = cur.fetchone()

                if usuario:
                    return {
                        "id_usuario": usuario['id_usuario'],
                        "email": usuario['email']
                    }
                else:
                    return None
        except sql.Error as e:
            raise ValueError(f"Erro ao buscar email do usuário >> {e}")