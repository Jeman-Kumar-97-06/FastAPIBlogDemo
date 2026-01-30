from enum import Enum
from fastapi import FastAPI
app = FastAPI()

#This means, we can define a set of string constants to represent different model names. 
#The path parameter should be one of these predefined model names.
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

fast_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get('/')
async def root():
    return {"message": "Hello, World!"}

@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    #Conditional Responses Based on Enum Values
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    elif model_name == ModelName.resnet:
        return {"model_name": model_name, "message": "Residuals are cool!"}
    elif model_name == ModelName.lenet:
        return {"model_name": model_name, "message": "LeNet is the best!"}
    return {"model_name": model_name, "message": "Unknown model"}

#Only allows file paths that can include slashes:
@app.get('/custom/{file:path}')
async def read_custom_file(file: str):
    return {"file_path": file}

@app.get('/fast-items/')
async def read_item(skip: int = 0, limit: int = 10):#skip means how many items to skip before starting to collect the result set. skip=0 means start from the beginning.
    return fast_items_db[skip : skip + limit]