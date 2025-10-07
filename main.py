from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {'message': 'patient management system API'}

@app.get("/about")
def about():
    return {'message': 'A fully functional API to manage patients records.'}