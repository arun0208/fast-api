from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    name : str
    section : str
    position : str
    salary : int

class UpdateItem(BaseModel):
    name : Optional[str]=None
    section : Optional[str]=None
    position : Optional[str]=None
    salary : Optional[int]=None

inventory = {
    1:{
    "name":"Arun",
    "section":"K20PT",
    "position":"full-stack developer",
    "salary" : 1000000
    },
    2:{
    "name":"Roshan",
    "section":"K20PT",
    "position":"Frontend developer",
    "salary" : 250000
    },
    3:{
    "name":"Ayush",
    "section":"K20PT",
    "position":"backend developer",
    "salary" : 330000
    },
}

@app.get("/")
def Home():
    return{"Data":"Testing"}

@app.get("/about")
def About():
    return{"Name":"Arun Sharma"}

@app.get("/get-items/{item_id}")
def get_items(item_id:int):
    return inventory[item_id]

@app.get("/get-items")
def all_items():
    return inventory

@app.get("/get-by-name")
def get_item(name:str=None):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data":"Not Found"}


@app.post("/create-item/{item_id}")
def create_item(item_id:int,item:Item):
    if item_id in inventory:
        return{"Error":"Item already exists"}
    inventory[item_id]={"name":item.name,"section":item.section,"position":item.position,"salary":item.salary}
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id:int,item:UpdateItem):
    if item_id not in inventory:
        return{"Error":"Item does not exists"}
    if item.name != None:
        inventory[item_id].name=item.name

    if item.section != None:
        inventory[item_id].section=item.section

    if item.position != None:
        inventory[item_id].position=item.position

    if item.salary != None:
        inventory[item_id].salary=item.salary


@app.delete("/delete-item")
def delete_item(item_id:int):
    if item_id not in inventory:
        return{"Error":"Item not Found"}
    del inventory[item_id]
    return{"Success":"Item Deleted"}