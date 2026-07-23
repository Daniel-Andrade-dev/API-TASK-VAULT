from flask import Flask
from core.routes.routes_usuario import usuario_bp
from core.routes.routes_tarefa import tarefa_bp


app = Flask(__name__)


app.register_blueprint(usuario_bp)
app.register_blueprint(tarefa_bp)

if __name__ == "__main__":
    app.run(debug=True)