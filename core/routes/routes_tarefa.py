from flask import Blueprint, request, jsonify
from core.domain.tarefa.tarefa import Tarefa
from core.services.service_tarefa import ServiceTarefa
from core.auth.auth_jwt import auth
from core.services.service_usuario import ServiceUsuario

tarefa_bp = Blueprint("tarefa", __name__)
service_tarefa = ServiceTarefa()
service_usuario = ServiceUsuario()

@tarefa_bp.route("/tarefa", methods=['POST'])
@auth
def cadastra_tarefa(payload):
    try:
        body_json = request.get_json()

        if not body_json:
            return jsonify({
                "erro": "Corpo da requisição inválido"
            }), 400
        
        usuario: dict | None = service_usuario.buscar_usuario_service(payload['email'])

        if usuario is None:
            return jsonify({"erro": "Usuário não cadastrado"}), 404

        tarefa = Tarefa(
            0,
            usuario['id_usuario'],
            body_json['titulo'],
            body_json['descricao']
        )

        adicionar_tarefa = service_tarefa.cadastra_tarefa_service(tarefa)

        if "erro" in adicionar_tarefa:
            return jsonify(adicionar_tarefa), 400
        
        return jsonify({
            "sucesso": True,
            "msg": "Tarefa adicionada",
            "tarefa": adicionar_tarefa
        }), 201
    
    except Exception as e:
        return jsonify({
            "erro_servidor": "Ocorreu um erro no servidor",
            "erro >>": str(e)
        }), 500
    

@tarefa_bp.route("/tarefa", methods=['GET'])
@auth
def tarefas_adicionadas(payload):
    try:
        
        usuario: dict | None = service_usuario.buscar_usuario_service(payload['email'])

        if usuario is None:
            return jsonify({"erro": "Usuário não cadastrado"}), 404

        tarefas = service_tarefa.tarefas_adicionada_service(usuario['id_usuario'])
        
        if tarefas:
            return jsonify({
                "sucesso": True,
                "tarefas": tarefas
            }), 200
        else:
            return jsonify({
                "sucesso": False,
                "erro": "Não a tarefas adicionada"
            }), 404
        
    except Exception as e:
        return jsonify({
            "erro_servidor": "Ocorreu um erro no servidor",
            "erro >>": str(e)
        }), 500


@tarefa_bp.route("/tarefa/<int:id_tarefa>", methods=['GET'])
@auth
def buscar_tarefa(payload, id_tarefa: int):
    try:
        usuario: dict | None = service_usuario.buscar_usuario_service(payload['email'])

        if usuario is None:
            return jsonify({
                "erro": "Usuário não encontrado"
            }), 404
        
        tarefa: dict | None = service_tarefa.buscar_tarefa_service(id_tarefa,usuario['id_usuario'])

        
        if tarefa is not None:
            return jsonify({
                "successo": True,
                "tarefa": tarefa
            }), 200
        else:
            return jsonify({
                "sucesso": False,
                "msg": "Tarefa não encontrada ou você não e dono da tarefa"
            }), 403
        
    except Exception as e:
        return jsonify({
            "erro_servidor": "Ocorreu um erro no servidor",
            "erro >>": str(e)
        }), 500



@tarefa_bp.route("/tarefa/<int:id_tarefa>", methods=['PUT'])
@auth
def atualizar_tarefa(payload, id_tarefa: int):
    try:
        body_json = request.get_json()
    
        if not body_json:
            return jsonify({
                "erro": "Corpo da requisição inválido"
            }), 400
        
        usuario = service_usuario.buscar_usuario_service(payload['email'])

        if usuario is None:
            return jsonify({
                "erro": "Usuário não encontrado"
            }), 404
    
        tarefa_atualizada = service_tarefa.atualizar_tarefa_service(
            body_json['titulo'],
            body_json['descricao'],
            body_json['status'],
            id_tarefa,
            usuario['id_usuario']
        )
        
        if "erro" in tarefa_atualizada:
            return jsonify(tarefa_atualizada), 400
        
        if tarefa_atualizada:
            return jsonify({
                "sucesso": True,
                "msg": "Tarefa atualizada",
                "tarefa": tarefa_atualizada
            }), 200
        
        if tarefa_atualizada is None:
            return jsonify({
                "sucesso": False,
                "erro": "Tarefa não encontrada"
            }), 404
        
    except Exception as e:
        return jsonify({
            "erro_servidor": "Ocorreu um erro no servidor",
            "erro >>": str(e)
        }), 500

@tarefa_bp.route("/tarefa/<int:id_tarefa>", methods=['DELETE'])
@auth
def deletar_tarefa(payload, id_tarefa: int):
    try:
        
        usuario = service_usuario.buscar_usuario_service(payload['email'])

        deletar: bool = service_tarefa.deletar_tarefa_service(id_tarefa,usuario['id_usuario'])
        

        if deletar:
            return jsonify({
                "sucesso": True,
                "msg": "Tarefa deletada com sucesso"
            }), 200
        else:
            return jsonify({
                "sucesso": False,
                "erro": "Tarefa não encontrada ou você não e dono"
            }), 403
    except Exception as e:
        return jsonify({
            "erro_servidor": "Ocorreu um erro no servidor",
            "erro >>": str(e)
        }), 500
