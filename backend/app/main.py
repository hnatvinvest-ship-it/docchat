from fastapi import FastAPI

app = FastAPI(title="docchat")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
