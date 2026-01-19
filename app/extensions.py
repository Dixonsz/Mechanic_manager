from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

# Inicializar extensiones
db = SQLAlchemy()
cors = CORS()
migrate = Migrate()
