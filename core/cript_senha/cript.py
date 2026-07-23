from werkzeug.security import generate_password_hash, check_password_hash

def gerar_hash(senha) -> str:
    return generate_password_hash(senha)

def validar_hash_e_senha(hash_salvo, senha) -> bool:
    return check_password_hash(hash_salvo, senha)