from flask import request, jsonify
from functools import wraps
from dotenv import load_dotenv
import jwt
import os


load_dotenv()
KEY = os.getenv("KEY_TOKEN")

def auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "Authorization" in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]

        if not token:
            return jsonify({"erro": "Token de acesso ausente"}), 401
        
        try:
            # Decodifica o token que foi e retornado no services cliente e nas rotas tarefas
            # Payload = Body da requisição
            payload = jwt.decode(token, KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({"erro": "Tokem expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"erro": "Token inválido"}), 401
        
        return f(payload, *args, **kwargs)
    
    return decorated