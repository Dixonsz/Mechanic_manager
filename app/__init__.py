from flask import Flask
import os
from pathlib import Path
from dotenv import load_dotenv
from app.extensions import db, cors, migrate
from flask_migrate import upgrade as flask_migrate_upgrade

# Cargar variables de entorno desde el archivo .env en la raíz del proyecto
basedir = Path(__file__).resolve().parent.parent
load_dotenv(basedir / '.env')

def create_app():
    """Factory para crear la aplicación Flask"""
    app = Flask(__name__)
    
    # Configuración
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'mysql+pymysql://root:@localhost:3306/style_manager')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_SORT_KEYS'] = False
    app.config['AUTO_MIGRATE'] = os.getenv('AUTO_MIGRATE', 'False').lower() == 'true'
    
    # Inicializar extensiones
    db.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)
    
    # Importar modelos para que Flask-Migrate los detecte
    from app.models import user, rol
    
    # Registrar blueprints
    from app.routes import register_routes
    register_routes(app)
    
    # Auto-migración (solo para desarrollo)
    if app.config['AUTO_MIGRATE']:
        with app.app_context():
            try:
                flask_migrate_upgrade()
                print("✓ Migraciones aplicadas automáticamente")
            except Exception as e:
                print(f"⚠ Error al aplicar migraciones: {e}")
    
    return app
