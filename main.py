from fastapi import FastAPI

app = FastAPI(title="Slack Bot")

from routers import service
app.include_router(service.router)