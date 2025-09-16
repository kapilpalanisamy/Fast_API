from fastapi import FastAPI

app=FastAPI()

#if we hit /docs it will give the documentation

@app.get("/")
def hello():
    return {'message':'Hello World'}

@app.get("/about")
def about():
    return {"message":"kapil is the person who is studying at Jain university"}