
"""

Validações das entidades na camada service

"""


class Usuario:
    def __init__(self, id_usuario, email, senha) -> None:
        self.__id_usuario: int = id_usuario
        self.__email: str = email
        self.__senha: str = senha
        
    @property
    def id_usuario(self) -> int:
        return self.__id_usuario
    
    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def senha(self) -> str:
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha