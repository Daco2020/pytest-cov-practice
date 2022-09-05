from fastapi import FastAPI


app = FastAPI()


@app.get("/{name}")
async def root(name):
    return f"I'm great {name}!"


변수 = "우주평화가 멀지 않았다."
