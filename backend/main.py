from fastapi import FastAPI
from app.routes import task
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

print(config("FRONTED_URL"))
app = FastAPI()
origins = {
    config("FRONTED_URL")
}
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(task.router)


@app.get('/')
def welcome():
    return "welocome to fastapi"
