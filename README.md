# Mechanic Manager API

API REST con Flask para gestión de Taller automotriz usando MySQL.

##Estructura del Proyecto

```
Style_manager/
├── app/
│   ├── __init__.py              # Inicialización de la aplicación Flask
│   ├── routes.py                # Definición de rutas y blueprints
│   ├── controllers/
│   │   └── style_controller.py  # Controladores (lógica de negocio)
│   └── models/
│       └── style_model.py       # Modelos (acceso a datos)
├── .env                         # Variables de entorno
├── .gitignore                   # Archivos a ignorar en git
├── run.py                       # Punto de entrada de la aplicación
├── requirements.txt             # Dependencias del proyecto
└── venv/                        # Entorno virtual
```

##Configuración

### 1. Activar el entorno virtual

```bash
venv\Scripts\activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar la base de datos

Crear la base de datos en MySQL:

```sql
CREATE DATABASE mechanic_manager CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 4. Configurar variables de entorno

Editar el archivo `.env` con tus credenciales:

```env
DATABASE_URL=mysql+pymysql://usuario:contraseña@localhost:3306/mechanic_manager
SECRET_KEY=tu-clave-secreta-segura
```

### 5. Ejecutar la aplicación

```bash
python run.py
```

La API estará disponible en: `http://localhost:5000`

##Endpoints

### Health Check
- **GET** `/api/health` - Verificar estado de la API


