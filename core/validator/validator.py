import re


class Validator:
    def validar_email(self, email: str) -> bool:
        regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return bool(re.match(regex, email))
    
    # Apenas uma validação básica da senha
    def validar_senha(self, senha: str) -> bool:
        return False if len(senha) < 8 else True
    