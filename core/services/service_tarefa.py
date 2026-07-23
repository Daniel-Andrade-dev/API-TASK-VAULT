from core.repository.tarefa_repository import TarefaRepository
from core.enum.status import Status
from core.domain.tarefa.tarefa import Tarefa
from datetime import datetime



"""

Apenas tem uma validação do Status, você pode mudar o status a qualquer momento 

Pode atualizar para pendente, em_andamento e concluida e vice versa

Pensei em fazer isso pois segui essa lógica

Se a tarefa foi concluida, mas ele que volta ou atualizar ela pois esqueceu algo etc..
Ele pode voltar para pendente ou em_andamento

"""


class ServiceTarefa:
    def __init__(self):
        self.tarefa_repository: TarefaRepository = TarefaRepository()

    def obter_hora(self) -> str:
        return datetime.now().strftime("%H:%M")
    
    def cadastra_tarefa_service(self, tarefa_obj):
        try:
            if isinstance(tarefa_obj, Tarefa):
                if not tarefa_obj.titulo:
                    return {"erro": "A campos vazios"}
                
                return self.tarefa_repository.cadastra_tarefa_repository(
                    tarefa_obj,
                    self.obter_hora()
                )
            return {"erro": "Objeto inválido"}
        except Exception as e:
            raise ValueError(f"Ocorreu um erro na camada de serviços tarefa  >> {e}")
    
    def tarefas_adicionada_service(self, id_usuario: int) -> list[dict]:
        try:
            return self.tarefa_repository.tarefas_adicionada_repository(id_usuario)
        except Exception as e:
            raise ValueError(f"Ocorreu um erro na camada de serviços tarefa  >> {e}")
    
    def buscar_tarefa_service(self, id_tarefa: int, id_usuario: int) -> dict | None:
        try:
            return self.tarefa_repository.buscar_tarefa_repository(id_tarefa, id_usuario) is not None
        except Exception as e:
            raise ValueError(f"Ocorreu um erro na camada de serviços tarefa  >> {e}")

    def atualizar_tarefa_service(self, titulo, descricao, status, id_tarefa: int, id_usuario: int):
        try:
            if not titulo or not status :
                return {"erro": "A campos vazios"}
            
            if status not in Status:
                return {"erro": "Status inválido"}

            return self.tarefa_repository.atualizar_tarefa_repository(
                titulo,
                descricao,
                status,
                self.obter_hora(),
                id_tarefa,
                id_usuario
                
            ) is not None
        except Exception as e:
            raise ValueError(f"Ocorreu um erro na camada de serviços tarefa  >> {e}")
        

    def deletar_tarefa_service(self, id_tarefa: int, id_usuario: int) -> bool:
        try:
            return self.tarefa_repository.deletar_tarefa_repository(id_tarefa,id_usuario)
        except Exception as e:
            raise ValueError(f"Ocorreu um erro na camada de serviços tarefa  >> {e}")