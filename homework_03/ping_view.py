from fastapi import APIRouter

router = APIRouter(
    prefix="/ping",
)


@router.get("/")
def ping():
    return {
        "message": "pong"
    }