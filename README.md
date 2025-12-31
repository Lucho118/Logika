# Logika
Prueba tecnica fastapi

API REST desarrollada con **FastAPI**, **PostgreSQL** y **SQLAlchemy**, que implementa
autenticación JWT y un CRUD de tareas.

El objetivo es entregar una solución funcional, clara y fácil de ejecutar en entorno local.

---

## 🧰 Tecnologías

- Python 3.11
- FastAPI
- SQLAlchemy
- PostgreSQL (Docker)
- Alembic (migraciones)
- JWT para autenticación
- Docker Compose

---

## 📦 Requisitos

- Docker y Docker Compose
- Python 3.11+
- Git

---

## � Estructura del Proyecto

```
Logika/
├── app/
│   ├── main.py                 # Punto de entrada de FastAPI
│   ├── api/
│   │   ├── deps.py             # Dependencias compartidas (JWT, DB)
│   │   ├── health.py           # Endpoint de health check
│   │   └── routes/
│   │       ├── auth.py         # Rutas de autenticación
│   │       ├── users.py        # Rutas de usuarios
│   │       └── tasks.py        # Rutas de tareas
│   ├── core/
│   │   ├── config.py           # Configuración del proyecto
│   │   └── security.py         # Funciones de seguridad y JWT
│   ├── db/
│   │   ├── base.py             # Base para modelos SQLAlchemy
│   │   └── session.py          # Configuración de sesión DB
│   ├── models/
│   │   ├── user.py             # Modelo User
│   │   └── task.py             # Modelo Task
│   └── schemas/
│       ├── user.py             # Schemas Pydantic de User
│       └── task.py             # Schemas Pydantic de Task
├── alembic/                    # Migraciones de base de datos
├── docker-compose.yml          # Configuración de servicios
├── requirements.txt            # Dependencias Python
├── alembic.ini                 # Configuración de Alembic
└── README.md                   # Este archivo
```

---

## �🐘 Base de datos (PostgreSQL con Docker)

La base de datos se ejecuta **exclusivamente en entorno local** usando Docker.

### Variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=technical_test
DB_USER=postgres
DB_PASSWORD=postgres
```

### Levantar PostgreSQL

```bash
docker compose up -d
```

Verificar que el contenedor esté corriendo:

```bash
docker ps
```

Para conectarse a la base de datos:

```bash
docker exec -it technical_test_postgres psql -U postgres -d technical_test
```

---

## ⚙️ Configuración del entorno

### 1️⃣ Crear entorno virtual

```bash
py -3.11 -m venv venv
```

### 2️⃣ Activar entorno virtual

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / Mac:**

```bash
source venv/bin/activate
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Ejecutar migraciones

```bash
alembic upgrade head
```

**Nota:** Al ejecutar las migraciones se crea un usuario por defecto:

- **Email:** `admin@example.com`
- **Contraseña:** `admin123`
