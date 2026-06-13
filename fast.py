import pickle
import numpy as np
import requests
import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from functools import lru_cache

app = FastAPI(title="Movie Recommender API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

movies     = pickle.load(open("movie_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

TMDB_API_KEY = "8265bd1679663a7ea12ac168da84d2e8"
PLACEHOLDER  = "https://placehold.co/500x750/1a1a1a/888888?text=No+Poster"


@lru_cache(maxsize=512)
def fetch_poster(movie_id: int) -> str:
    try:
        url  = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
        data = requests.get(url, timeout=5).json()
        path = data.get("poster_path")
        return f"https://image.tmdb.org/t/p/w500{path}" if path else PLACEHOLDER
    except requests.RequestException:
        return PLACEHOLDER


@app.get("/health")
def health():
    return {"status": "ok", "total_movies": len(movies)}


@app.get("/movies")
def list_movies():
    return {"movies": movies["title"].tolist()}


@app.get("/recommend/{movie_name}")
def recommend(movie_name: str, n: int = 5):
    if movie_name not in movies["title"].values:
        raise HTTPException(status_code=404, detail=f"Movie '{movie_name}' not found.")

    idx     = movies[movies["title"] == movie_name].index[0]
    indices = np.argsort(similarity[idx])[::-1][1: n + 1]

    results = []
    for i in indices:
        row = movies.iloc[i]
        results.append({
            "title":  row["title"],
            "poster": fetch_poster(int(row["id"])),
        })

    return {"movie": movie_name, "recommendations": results}