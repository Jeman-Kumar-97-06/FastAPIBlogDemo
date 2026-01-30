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
#in the above example, limit specifies the maximum number of items to return. it's a query parameter with a default value of 10.
#So, if you call /fast-items/?skip=1&limit=2, it will skip the first item and return the next two items from the fast_items_db list.
#If you call /fast-items/ without any query parameters, it will return the first 10 items from the list.

@app.get('/items/{item_id}')
async def read_it(item_id:str, q: str| None = None, short: bool = False): #'q' should be treated as an optional query parameter. 
                                                                          # If the client includes it in the request, 
                                                                          # its value will be passed to the function; otherwise, it will be None.
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item