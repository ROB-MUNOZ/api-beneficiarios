# Prueba Técnica - Encargado de Bases de Datos
# Roberto Muñoz Ñanco

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

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/api-beneficiarios.git
   cd api-beneficiarios
