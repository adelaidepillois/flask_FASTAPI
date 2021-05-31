# This is a sample Python script.
import fastapi
import uvicorn
import movie_data
from models.movie_model import MovieModel

app = fastapi.FastAPI()

@app.get('/')
async def index():
    return{
        "message": "Hello world",
        "usage": "Call /api/movie/{title} to use the API"
    }

@app.get("/api/movie/{title}", response_model=MovieModel)
async def movie_search(title: str):
    movie = await movie_data.get_movie(title)
    if not movie:
        raise fastapi.HTTPException(status_code=404)

    return movie.dict()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run(app)

