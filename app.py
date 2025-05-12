from fastapi import FastAPI

from services import package_service, truck_service
from db import initialize_db

initialize_db()
app = FastAPI()


@app.get("/")
def read_root():
    return "Hi Lennar, welcome to Hanil Zarbailov's truck loading simulator app! You can access the docs via /docs (usually http://127.0.0.1:8000/docs )"

@app.get("/package")
def get_all_packages():
    return package_service.get_all_packages()

@app.get("/package/{id}")
def get_package_by_id(id: int):
    res = package_service.get_package_by_id(id)
    if res is None:
        return f"Error: no package with id {id}"
    return res

@app.get("/truck")
def get_all_trucks():
    return truck_service.get_all_trucks()


@app.get("/truck/{id}")
def get_truck_by_id(id: int):
    res = truck_service.get_truck_by_id(id)
    if res is None:
        return f"Error: no truck with id {id}"
    return res

