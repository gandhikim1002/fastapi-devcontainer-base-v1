from fastapi import APIRouter
from starlette.responses import StreamingResponse
from .qr_code_generator import generate_qr_code_image


router = APIRouter()


@router.get("")
def test_get():
    return {"message": "OK"}

# echo test
# web hook test

@router.get("/{msg}")
async def get_qr_code(msg: str):
    image_buffer = generate_qr_code_image(msg)
    return StreamingResponse(image_buffer, media_type="image/png")


@router.post("")
def get_qr_code(message: str):
    image_buffer = generate_qr_code_image(message)
    return StreamingResponse(image_buffer, media_type="image/png")

