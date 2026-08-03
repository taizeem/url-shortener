from fastapi import FastAPI

app = FastAPI(
    title = "Url Shortener",
    version = "1.0.0"
)

@app.get("/")
def root():
    return {
     "message":"Welcome to the url shortener api"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
