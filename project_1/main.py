from fastapi import FastAPI
import json

# create a object of the FastAPI class to define endpoints
app = FastAPI()


def load_data():  # A function to retrieve data from the json file
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


# defining a root for endpoint
@app.get("/")
def hello():
    return {"message": "Patient Management System API"}


@app.get("/about")
def new():
    return {"message": "A fully functional API for managing patient records"}


# to initialize your web server run "uvicorn main:app --reload" which gives requests and ctrl+C to end
# while you can run your local server like http://127.0.0.1:8000, this is created when i run the command.
# if you change the command to http://http://127.0.0.1:8000/about it will show the second message.
# if you change the command to http://http://127.0.0.1:8000/docs it will give you the documentation of your FastAPI


@app.get("/view")
def view():
    print("--- Inside /view endpoint ---")
    data = load_data()
    return data
