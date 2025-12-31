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

### 5️⃣ Ejecutar el servidor

```bash
fastapi dev app/main.py
```

El servidor estará disponible en `http://localhost:8000`

---

## 📚 Documentación de Rutas

### Autenticación

#### POST `/auth/login`
Inicia sesión y devuelve un token JWT.

**Body:**
```json
{
  "username": "admin@example.com",
  "password": "admin123"
}
```

**Response (200):**
```json
{
  "access_token": "eyJhbGc...",
  "token_type": "bearer"
}
```

---

### Usuarios

#### GET `/users/me`
Obtiene los datos del usuario actual autenticado.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
{
  "id": 1,
  "email": "admin@example.com",
  "is_active": true
}
```

#### GET `/users`
Lista todos los usuarios.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
[
  {
    "id": 1,
    "email": "admin@example.com",
    "is_active": true
  }
]
```

#### POST `/users`
Crea un nuevo usuario.

**Headers:** `Authorization: Bearer <token>`

**Body:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response (200):**
```json
{
  "id": 2,
  "email": "user@example.com",
  "is_active": true
}
```

#### GET `/users/{user_id}`
Obtiene un usuario por ID.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
{
  "id": 1,
  "email": "admin@example.com",
  "is_active": true
}
```

#### PUT `/users/{user_id}`
Actualiza un usuario.

**Headers:** `Authorization: Bearer <token>`

**Body:**
```json
{
  "email": "newemail@example.com",
  "is_active": true
}
```

**Response (200):**
```json
{
  "id": 1,
  "email": "newemail@example.com",
  "is_active": true
}
```

#### DELETE `/users/{user_id}`
Elimina un usuario.

**Headers:** `Authorization: Bearer <token>`

**Response (204)** - No Content

---

### Tareas

#### POST `/tasks`
Crea una nueva tarea.

**Headers:** `Authorization: Bearer <token>`

**Body:**
```json
{
  "title": "Hacer compras",
  "description": "Comprar leche, pan y huevos"
}
```

**Response (201):**
```json
{
  "id": 1,
  "title": "Hacer compras",
  "description": "Comprar leche, pan y huevos",
  "status": "pending"
}
```

#### GET `/tasks`
Lista todas las tareas con paginación.

**Headers:** `Authorization: Bearer <token>`

**Query Parameters:**
- `skip` (opcional): Número de registros a saltar (default: 0)
- `limit` (opcional): Máximo de registros a devolver (default: 100)

**Response (200):**
```json
[
  {
    "id": 1,
    "title": "Hacer compras",
    "description": "Comprar leche, pan y huevos",
    "status": "pending"
  }
]
```

#### GET `/tasks/{task_id}`
Obtiene una tarea por ID.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
{
  "id": 1,
  "title": "Hacer compras",
  "description": "Comprar leche, pan y huevos",
  "status": "pending"
}
```

#### PUT `/tasks/{task_id}`
Actualiza una tarea completa.

**Headers:** `Authorization: Bearer <token>`

**Body:**
```json
{
  "title": "Hacer compras actualizado",
  "description": "Comprar más cosas",
  "status": "in_progress"
}
```

**Response (200):**
```json
{
  "id": 1,
  "title": "Hacer compras actualizado",
  "description": "Comprar más cosas",
  "status": "in_progress"
}
```

#### PUT `/tasks/{task_id}/status`
Actualiza solo el estado de una tarea.

**Headers:** `Authorization: Bearer <token>`

**Body:**
```json
{
  "status": "completed"
}
```

**Response (200):**
```json
{
  "id": 1,
  "title": "Hacer compras",
  "description": "Comprar leche, pan y huevos",
  "status": "completed"
}
```

#### DELETE `/tasks/{task_id}`
Elimina una tarea.

**Headers:** `Authorization: Bearer <token>`

**Response (204)** - No Content

---

## ⚡ Estados de Tarea

Las tareas pueden tener los siguientes estados:

- `pending` - Pendiente
- `in_progress` - En progreso
- `completed` - Completada

