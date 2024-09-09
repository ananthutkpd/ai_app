from fastapi import FastAPI
from controller.openai_controller import router as openai_router

app = FastAPI()

app.include_router(openai_router, prefix="/openai", tags=["OpenAI"])

@app.get("/")
def read_root() -> dict:
    """
    Root endpoint that returns a welcome message.

    Returns:
        dict: A dictionary containing a welcome message.
    """
    return {"message": "Welcome to the OpenAI FastAPI application!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)