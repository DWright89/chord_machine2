from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from server.routes.v1.root_router import root_router
from server.routes.v1.user_router import user_router
from server.routes.v1.chord_router import chord_router
from server.utils.db_manager import init_db
from uvicorn import run

app = FastAPI(
    title="Chord Machone",
    description="Service to silence the musical demons in dennys brain",
    docs_url='/docs',
    openapi_url="/api/v1/openapi.json",
)


@app.on_event("startup")
async def startup_events() -> None:
    init_db(app)

origins = ["*"]

# middleware
app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"], allow_credentials=True
)

app.include_router(root_router, tags=["root", "v1"])
app.include_router(user_router, tags=["user", "v1"])
app.include_router(chord_router, tags=["chords", "v1"])


if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=8080)