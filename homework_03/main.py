import uvicorn
from fastapi import FastAPI

from ping_view import router as ping_router

app = FastAPI()
app.include_router(ping_router)


@app.get("/")
def index():
    return {
        "message": "FastAPI on Docker",
    }


if __name__ == " __main__":
    uvicorn.run(
        "main:app",
        reload=True,
    )