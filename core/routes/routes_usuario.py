from flask import Blueprint, request, jsonify
from core.domain.usuario.usuario import Usuario
from core.services.service_usuario import ServiceUsuario



usuario_bp = Blueprint("usuario", __name__)
service_usuario = ServiceUsuario()



@usuario_bp.route("/cadastra_usuario", methods=['POST'])
def cadastra_usuario():
    try:
        body_json = request.get_json()
        
        if not body_json:
            return jsonify({"erro": "Corpo da requisição inválido"}), 401
        
        usuario_obj = Usuario(
            0,
            body_json['email'],
            body_json['senha']
        )
       
        cadastro:  dict | bool = service_usuario.cadastrar_usuario_service(usuario_obj)

        if "erro" in cadastro:
            return jsonify(cadastro), 400
        
     
        return jsonify({
            "sucesso": True,
            "msg": "Contra cadastrada",
            "conta": cadastro
        }), 201
        
    except Exception as e:
        return jsonify({
            "erro_servidor": "Ocorreu um erro no servidor",
            "erro >>": str(e)
        }), 500



@usuario_bp.route("/login_usuario", methods=["POST"])
def login_usuario():
    try:
        body_json = request.get_json()

        if not body_json:
            return jsonify({"erro": "Corpo da requisição inválido"}), 401
        
        login = service_usuario.login_usuario_service(
            body_json['email'],
            body_json['senha']
        )

        if "erro" in login:
            return jsonify(login), 400
        
        return jsonify({
            "sucesso": True,
            "login": login
        }), 201
    
    except Exception as e:
        return jsonify({
            "erro_servidor": "Ocorreu um erro no servidor",
            "erro >>": str(e)
        }), 500

