from flask import Flask
from flask_cors import CORS
from backend.routes.chat_routes import chat_bp
from backend.routes.session_routes import session_bp
from backend.database.db import init_db

from backend.routes.code_review_routes import code_review_bp
from backend.routes.research_routes import research_bp
from backend.routes.document_routes import document_bp



app = Flask(__name__)
CORS(app, supports_credentials=True)

init_db()



# Register Blueprints
app.register_blueprint(chat_bp, url_prefix="/api")
app.register_blueprint(session_bp, url_prefix="/api")
app.register_blueprint(code_review_bp, url_prefix="/api")
app.register_blueprint(research_bp, url_prefix="/api")
app.register_blueprint(document_bp, url_prefix="/api")




if __name__ == "__main__":
    app.run(debug=True)

# from flask import Flask
# from routes.chat_routes import chat_bp
# from routes.session_routes import session_bp
#
# def create_app():
#     app = Flask(__name__)
#
#     # Register blueprints
#     app.register_blueprint(chat_bp, url_prefix="/api")
#     app.register_blueprint(session_bp, url_prefix="/api")
#
#     @app.get("/health")
#     def health():
#         return {"status": "ok"}
#
#     return app
#
# if __name__ == "__main__":
#     app = create_app()
#     app.run(debug=True)
#