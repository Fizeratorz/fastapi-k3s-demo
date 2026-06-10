from fastapi import FastAPI

app = FastAPI(title="FastAPI + k3s Demo")

@app.get("/")
def root():
    return {"message": "Hello from Kubernetes!", "env": "production"}

@app.get("/health")
def health():
    return {"status": "ok"}