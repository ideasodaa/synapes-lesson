from fastapi import FastAPI,Path,body
import uvicorn
from pydantic import BaseModel, Field

app = FastAPI(title="Sample FastAPI",
              description="For education", version="1.0")


data = {1: "John", 2: "jane"}

@app.get("/api/people")
def get_peoples():
    return data

@app.get("/api/people/{id}")
def get_one_people(id: int = Path()):
    return data[id]

class People(BaseModel):
    id: int = Field(..., description="first name")
    name: str = Field("None", description="last name")
    
@app.post("/api/people-add")
def add_one_people(data: People):
    print(data)
    return data

data={1:"Yuta",2:"Gigi"}

class people(BaseModel):
    id:int =Field(..., descripyion="first_name")
    name:str= Field(None, descripyion="last_name")

@app.get("/api/hello")
def read_root():
    return data

@app.post("api/people-add")
def add_one_people(data:people):
    print(data)
    return data

@app.get("/api/hello_") #protocol to update
def read_root(id:int):
    return id,data[id]

if __name__ == "__main__":
	uvicorn.run("app:app", port=5000, log_level="info", reload=True, host="0.0.0.0")