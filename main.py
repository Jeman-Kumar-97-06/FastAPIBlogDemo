from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts : list[dict] = [
    {
        "id":1,
        "author":"Corey Schafer",
        "title":"Fast API is awesome",
        "content":"This framework is really easy to use and super fast",
        "date_posted":"April 10, 2025",
    },
    {
        "id":2,
        "author":"Jane Doe",
        "title":"Python is Great for Web Dev",
        "content":"Python is a great lang for web dev dawg!",
        "date_posted":"April 21, 2025",
    }
]

@app.get('/',response_class=HTMLResponse,include_in_schema=False)
def home():
    return f"<h1>Hello WOrld!</h1>"

@app.get('/api/posts')
@app.get('/api/posts_yo')
def get_posts():
    return posts