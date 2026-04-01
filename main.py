from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="InfraOps API Platform")


class Service(BaseModel):
    id: int
    name: str
    owner: str
    status: str


services = [
    {"id": 1, "name": "Email Gateway", "owner": "Infrastructure Team", "status": "active"},
]


@app.get("/")
def root():
    return {"message": "InfraOps API is running"}


@app.get("/services")
def get_services():
    return services


@app.post("/services")
def create_service(service: Service):
    services.append(service.dict())
    return service