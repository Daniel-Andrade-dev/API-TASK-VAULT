from core.repository.usuario_repository import UsuarioRepository
from core.cript_senha.cript import validar_hash_e_senha
from core.domain.usuario.usuario import Usuario
from core.validator.validator import Validator
from core.auth.auth_jwt import KEY
from datetime import datetime, timedelta
import jwt


class ServiceUsuario:
    def __init__(self) -> None:
        self.usuario_repository: UsuarioRepository = UsuarioRepository()
        self.validator: Validator = Validator()

    def cadastrar_usuario_service(self, usuario_obj) -> dict:
        try:
            if isinstance(usuario_obj, Usuario):
                if not usuario_obj.email or not usuario_obj.senha:
                    return {"erro": "A campos vazios para ser preenchido"}
                
                if not self.validator.validar_email(usuario_obj.email):
                    return {"erro": "Email inválido"}
                
                if not self.validator.validar_senha(usuario_obj.senha):
                    return {"erro": "Senha inválida precisa ter no minímo 8 caracteres"}
                
                return self.usuario_repository.cadastra_usuario_repository(
                    usuario_obj
                )
            return {"erro": "Objeto inválido"}
        except Exception as e:
            raise ValueError(f"Ocorreu um erro na camada de serviços usuario >> {e}")
            

    def login_usuario_service(self, email: str, senha: str) -> dict[str]:
        try:
            conta_cadastrada = self.usuario_repository.login_usuario_repository(email)
            
            if not email or not senha:
                return {"erro": "A campos vazios para ser preenchido"}
            
            if conta_cadastrada is None:
                return {"erro": "Email não encontrado"}
            
            if not self.validator.validar_email(email):
                return {"erro": "Email inválido"}
            
            if not self.validator.validar_senha(senha):
                return {"erro": "Senha inválida precisa ter no minímo 8 caracteres"}
            
            if validar_hash_e_senha(conta_cadastrada["hash"], senha):
                token: str = jwt.encode(
                        {
                            "email": conta_cadastrada['email'],
                            "exp": datetime.utcnow() + timedelta(hours=1)
                        },
                        KEY,
                        algorithm="HS256"
                    )

                return {
                    "sucesso": True,
                    "msg": "Login realizado com sucesso",
                    "token": token
                }
            else:
                return {
                    "sucesso": False,
                    "erro": "Email ou senha inválidos"
                }
        except Exception as e:
            raise ValueError(f"Ocorreu um erro na camada de serviços usuario >> {e}")


    def buscar_usuario_service(self, email: str) -> dict | None:
        try:
            return self.usuario_repository.buscar_usuario_repository(email)
        except Exception as e:
            raise ValueError(f"Ocorreu um erro na camada de serviços usuario >> {e}")