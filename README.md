# Style Manager API

API REST con Flask para gestión de estilos CSS usando MySQL.

## 📁 Estructura del Proyecto

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

## 🚀 Configuración

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
CREATE DATABASE style_manager CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 4. Configurar variables de entorno

Editar el archivo `.env` con tus credenciales:

```env
DATABASE_URL=mysql+pymysql://usuario:contraseña@localhost:3306/style_manager
SECRET_KEY=tu-clave-secreta-segura
```

### 5. Ejecutar la aplicación

```bash
python run.py
```

La API estará disponible en: `http://localhost:5000`

## 📡 Endpoints

### Health Check
- **GET** `/api/health` - Verificar estado de la API

### Estilos

- **GET** `/api/styles` - Obtener todos los estilos
- **GET** `/api/styles/<id>` - Obtener un estilo específico
- **POST** `/api/styles` - Crear nuevo estilo
- **PUT** `/api/styles/<id>` - Actualizar estilo
- **DELETE** `/api/styles/<id>` - Eliminar estilo

## 📝 Ejemplos de Uso

### Crear un estilo

```bash
curl -X POST http://localhost:5000/api/styles \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Dark Theme",
    "description": "Tema oscuro para la aplicación",
    "css_content": "body { background-color: #1a1a1a; color: #ffffff; }"
  }'
```

### Obtener todos los estilos

```bash
curl http://localhost:5000/api/styles
```

### Actualizar un estilo

```bash
curl -X PUT http://localhost:5000/api/styles/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Dark Theme Updated",
    "css_content": "body { background-color: #000000; }"
  }'
```

### Eliminar un estilo

```bash
curl -X DELETE http://localhost:5000/api/styles/1
```

## 🛠️ Tecnologías

- **Flask** - Framework web
- **Flask-SQLAlchemy** - ORM para base de datos
- **Flask-CORS** - Manejo de CORS
- **PyMySQL** - Conector MySQL
- **python-dotenv** - Variables de entorno

## 📦 Estructura de Datos

### Style Model

```json
{
  "id": 1,
  "name": "Dark Theme",
  "description": "Tema oscuro para la aplicación",
  "css_content": "body { background-color: #1a1a1a; }",
  "created_at": "2026-01-18T10:30:00",
  "updated_at": "2026-01-18T10:30:00"
}
```
