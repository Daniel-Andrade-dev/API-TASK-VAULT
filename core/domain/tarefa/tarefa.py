from core.enum.status import Status

"""

Validações das entidade na camada service

"""


class Tarefa:
    def __init__(self, id_tarefa, id_usuario, titulo, descricao) -> None:
        self.__id_tarefa: int = id_tarefa
        self.__id_usuario: int = id_usuario
        self.__titulo: str = titulo
        self.__descricao: str = descricao
        self.__status: Status = Status.PENDENTE

    @property
    def id_tarefa(self) -> int:
        return self.__id_tarefa
    
    @property
    def id_usuario(self) -> int:
        return self.__id_usuario
    
    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario
        
    @property
    def titulo(self) -> str:
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def descricao(self) -> str:
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status):
        self.__status = status
