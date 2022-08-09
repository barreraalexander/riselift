from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server import models
from server.database import engine
from server.routers import user, auth, worksession, exercise

# models.Base.metadata.create_all(bind=engine)

def create_app():
    origins = [
        "http://localhost:3000",
        "http://localhost:3000/?",
        "http://localhost:8080",
        "http://localhost:8080/?",
    ]


    app = FastAPI()

    app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"])

    app.include_router(user.router)
    app.include_router(auth.router)
    app.include_router(worksession.router)
    app.include_router(exercise.router)

    @app.get("/")
    def root():
        return {"message" : "Hello World"}


    return app