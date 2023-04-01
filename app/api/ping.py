from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
async def pong() -> dict[str, str]:
    return {"ping": "pong"}
