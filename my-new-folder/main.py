from fastapi import FastAPI

# create a object of the FastAPI class to define endpoints
app = FastAPI()


# defining a root for endpoint
@app.get("/")
def hello():
    return {"message": "HELLO WORLD !"}


@app.get("/about")
def new():
    return {"message": "I am Himanshu. And I am Learning FastAPI"}
