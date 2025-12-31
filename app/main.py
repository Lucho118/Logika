from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.routes import auth, users, tasks

app = FastAPI(title="Technical Test API")

app.include_router(health_router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(tasks.router)
