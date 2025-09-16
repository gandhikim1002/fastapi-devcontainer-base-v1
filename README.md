
### directory structure
* project-name
  * app
    * src
      * domain
      * internal
      * routers
    * resources
    * test


### step command
* make directory
* add main.py
``` python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
```

* code .
* >dev containers: add dev container configuration files
* add configuration to workspace
* python3 & postgreSQL
* 3.11-bullseye(default)
* modify Dockerfile
``` 
# ENV PYTHONUNBUFFERED 1
```
* pip install --upgrade pip

* pip install uvicorn
* pip install fastapi
* pip install sqlmodel
* pip install psycopg2
* pip install PyJWT
* pip install pydantic[email]
* requirements.txt.1
* pip install "passlib[bcrypt]"
* requirements.txt.2
** error
ersion = _bcrypt.__about__.__version__ 
>> version = _bcrypt.__version__
* pip install validators
* requirements.txt.5
* pip install python-telegram-bot


### todo list
* test module hero OK
* add logger holding
* fake_hashed_password OK
* schedulers
* BackgroundTasks
* Celery

* https://jnikenoueba.medium.com/chatbots-and-fastapi-c0e3d933b30f
``` python
    from fastapi import FastAPI, Request
    from telegram import Bot, Update
    from telegram.ext import Application, CommandHandler, MessageHandler, filters
    import asyncio

    TOKEN = "YOUR_TELEGRAM_BOT_API_TOKEN" # Replace with your bot token
    WEBHOOK_URL = "https://yourdomain.com/webhook" # Replace with your public URL

    app = FastAPI()
    bot = Bot(TOKEN)
    application = Application.builder().token(TOKEN).build()

    async def start(update: Update, context: Application):
        await update.message.reply_text("Hello! I'm your FastAPI Telegram bot.")

    async def echo(update: Update, context: Application):
        await update.message.reply_text(update.message.text)

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    @app.on_event("startup")
    async def startup_event():
        await application.bot.set_webhook(WEBHOOK_URL)
        await application.start()

    @app.on_event("shutdown")
    async def shutdown_event():
        await application.stop()
        await application.bot.delete_webhook()

    @app.post("/webhook")
    async def webhook_handler(request: Request):
        update = Update.de_json(await request.json(), bot)
        await application.process_update(update)
        return {"status": "ok"}
```