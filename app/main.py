from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# content of test_sample.py
def inc(x):
    return x + 1

def test_answer():
    return True

