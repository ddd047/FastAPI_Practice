from fastapi import FastAPI  # type: ignore[import]

# create a object of the FastAPI class to define endpoints
app = FastAPI()


# defining a root for endpoint
@app.get("/")
def hello():
    return {"message": "HELLO WORLD !"}


@app.get("/about")
def new():
    return {"message": "I am Himanshu. And I am Learning FastAPI"}


# to initialize your web server run "uvicorn main:app --reload" which gives requests and ctrl+C to end
# while you can run your local server like http://127.0.0.1:8000, this is created when i run the command.
# if you change the command to http://http://127.0.0.1:8000/about it will show the second message.
# if you change the command to http://http://127.0.0.1:8000/docs it will give you the documentation of your FastAPI
