# Prueba Técnica - Encargado de Bases de Datos - Roberto Muñoz Ñanco

# API REST - Beneficiarios

Este proyecto expone una API REST construida con FastAPI que permite consultar datos de beneficiarios almacenados en una base de datos SQL Server.

## Endpoints

- `GET /beneficiaries`: Lista de beneficiarios (con paginación opcional).
- `GET /beneficiaries/{id}`: Información de un beneficiario por ID.
- `GET /beneficiaries/program/{program}`: Filtra beneficiarios por programa.

## Requisitos

- Python 3.9+
- SQL Server Express (u otra versión)
- ODBC Driver 17 for SQL Server
- pip

## Instalación y ejecución local

### 1. Clonar este repositorio 
```bash
git clone https://github.com/ROB-MUNOZ/api-beneficiarios.git
cd api-beneficiarios
```

### 2. Crear y activar entorno virtual
```bash
python -m venv venv
venv\Scripts\activate  # En Windows
```

### 3. Instalar las dependencias
```bash
pip install -r previos.txt
```

### 4. Configurar archivo .env
Crear un archivo llamado .env con este contenido (ajústalarlo al entorno):

DB_SERVER=DESKTOP-PH77UF4\SQLEXPRESS
DB_NAME=prueba_tecnica

Este archivo está ignorado por .gitignore por seguridad. Usar .env.example como referencia.

### 5. Ejecutar el servidor
```bash
uvicorn main:app --reload
```

### 6. Acceder a la documentación Swagger
Abre tu navegador en:
http://127.0.0.1:8000/docs
Allí se verá Swagger UI, una interfaz interactiva para probar la API.

### 7. Estructura del proyecto
.
├── main.py
├── basedatos.py
├── modelos.py
├── previos.txt
├── .env.example
├── .gitignore
├── README.md
└── PROPUESTA_TECNICA.md
