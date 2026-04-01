import os
from fastapi import FastAPI
from pydantic import BaseModel

app_name = os.getenv("APP_NAME", "InfraOps API Platform")
app_env = os.getenv("APP_ENV", "development")

app = FastAPI(title=app_name)


class Service(BaseModel):
    id: int
    name: str
    owner: str
    status: str


services = [
    {"id": 1, "name": "Email Gateway", "owner": "Infrastructure Team", "status": "active"},
    {"id": 2, "name": "VMware Cluster", "owner": "Cloud Operations", "status": "active"},
]


@app.get("/")
def root():
    return {
        "message": f"{app_name} is running",
        "environment": app_env
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "app": app_name,
        "environment": app_env
    }


@app.get("/services")
def get_services():
    return services


@app.post("/services")
def create_service(service: Service):
    services.append(service.dict())
    return {"message": "Service created", "service": service}