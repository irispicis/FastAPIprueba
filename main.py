

from fastapi import FastAPI
import uvicorn

from openaitest import Document, inference


app = FastAPI()

@app.get("/")git
def read_root():
    return {"Hola": "Bienvenido"}


@app.post('/inference', status_code=200)
def inference_endpoint(doc: Document):
    response = inference(doc.prompt)
    return {
        'inference': response[0],
        'usage': response[1]
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9045)
