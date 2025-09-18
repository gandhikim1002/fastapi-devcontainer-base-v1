from fastapi import APIRouter
from starlette.responses import StreamingResponse
from fastapi import BackgroundTasks
from .bot import updater, bot, TOKEN

router = APIRouter()


@router.get("")
def test_get():
    return {"message": "OK"}

# echo test
# web hook test


@router.post("")
def send_message_webhook(message: str) -> str:
    return "OK"


@router.get("/startup")
async def startup_event():
    updater.start_polling()


@router.post("/webhook")
async def webhook(update: dict, background_tasks: BackgroundTasks):
    updater.dispatcher.process_update(update)
    return "ok"


@router.get("/")
async def read_root():
    return {"message": "Hello, this is the FastAPI Chatbot server."}




"""
/CommandHandler > fastapi > action > return 

row http webhook

webhook api
    fastapi > action > meg

init start

api start

"""