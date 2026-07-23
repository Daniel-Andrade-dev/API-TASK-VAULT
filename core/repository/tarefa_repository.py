from core.domain.tarefa.tarefa import Tarefa
from core.schema.tabelas import NAME_DB
import sqlite3 as sql



class TarefaRepository:
    def conexao_database(self):
        try:
            conn = sql.connect(NAME_DB)
            conn.row_factory = sql.Row
            return conn
        except sql.InternalError:
            raise ValueError("Erro para fazer conexão ao banco de dados")

    def cadastra_tarefa_repository(self, tarefa_obj, horario_cadastrada) -> dict[str]:
        try:
            with self.conexao_database() as conn:
                if isinstance(tarefa_obj, Tarefa):
                    cur = conn.execute(
                        """
                        INSERT INTO tarefas 
                        (id_usuario,titulo,descricao,horario_cadastrada)
                        VALUES(?,?,?,?)
                        """,(
                             tarefa_obj.id_usuario,
                             tarefa_obj.titulo,
                             tarefa_obj.descricao,
                             horario_cadastrada
                            )
                    )

                    tarefa_id: int = cur.lastrowid

                    return {
                        "tarefa_id": tarefa_id,
                        "usuario_id": tarefa_obj.id_usuario,
                        "titulo": tarefa_obj.titulo,
                        "descricao": tarefa_obj.descricao,
                        "status": "pendente",
                        "horario_cadastrada": horario_cadastrada
                    }
                return {"erro": "Objeto inválido"}
        except sql.IntegrityError:
            return {
                "sucesso": False,
                "erro": "Tarefa já está cadastrada"
            }
        except sql.Error as e:
            raise ValueError(f"Erro para cadastra tarefa ao banco de dados >> {e}")

    def tarefas_adicionada_repository(self, id_usuario: int) -> list[dict]:
        try:
            with self.conexao_database() as conn:
                cur = conn.execute(
                    """
                    SELECT 
                        id_tarefa,
                        id_usuario,
                        titulo,
                        descricao,
                        
                        status,horario_cadastrada
                    FROM 
                        tarefas WHERE id_usuario = ?
                    """,(id_usuario,)
                )
                tarefas = cur.fetchall()
                
                return [dict(tarefa) for tarefa in tarefas]
        except sql.Error as e:
            raise ValueError(f"Erro para listar tarefa para o usuário >> {e}")
        
    def buscar_tarefa_repository(self, id_tarefa: int, id_usuario: int) -> dict | None:
        try:
            with self.conexao_database() as conn:
                cur = conn.execute(
                    """
                    SELECT 
                        id_tarefa,
                        id_usuario,
                        titulo,
                        descricao,
                        status
                    FROM tarefas WHERE id_tarefa = ? AND id_usuario = ?
                    """,(id_tarefa,id_usuario,)
                )

                tarefa = cur.fetchone()

                if tarefa:
                    return {
                        "id_tarefa": tarefa['id_tarefa'],
                        "titulo": tarefa['titulo'],
                        "descricao": tarefa['descricao'],
                        "status": tarefa['status']
                    }
                else:
                    return None
        except sql.Error as e:
            raise ValueError(f"Erro para buscar ID da tarefa >> {e}")



    def atualizar_tarefa_repository(self, titulo, descricao, status, horario_cadastrada, id_tarefa, id_usuario):
        try:
            with self.conexao_database() as conn:
                
                buscar_tarefa = self.buscar_tarefa_repository(id_tarefa,id_usuario)

                if buscar_tarefa:
                    conn.execute(
                        """
                        UPDATE tarefas
                        SET titulo = ?, descricao = ?, status = ?, horario_cadastrada = ?
                        WHERE id_tarefa = ? AND id_usuario = ?
                        """,(
                            titulo,
                            descricao,
                            status,
                            horario_cadastrada,
                            id_tarefa,
                            id_usuario
                        )
                    )

                    return {
                        "titulo": titulo,
                        "descricao": descricao,
                        "status": status,
                        "horario": horario_cadastrada,
                    }
                return None

        except sql.Error as e:
            raise ValueError(f"Erro para atualizar tarefa >> {e}")

    def deletar_tarefa_repository(self, id_tarefa: int, id_usuario: int) -> bool:
        try:
            with self.conexao_database() as conn:
                cur = conn.execute(
                    """
                    DELETE FROM tarefas
                    WHERE id_tarefa = ? AND id_usuario = ?
                    """,(id_tarefa,id_usuario,)
                )


                return cur.rowcount > 0
        except sql.Error as e:
            raise ValueError(f"Erro para deletar tarefa >> {e}")