# 🎬 CineMatch — Movie Recommender System

A content-based movie recommendation system that suggests 5 similar movies based on your selection, complete with posters fetched live from the TMDB API.

---

## ✨ Features

- Content-based filtering using **Cosine Similarity**
- **FastAPI** backend with auto-generated `/docs` (Swagger UI)
- Poster fetching via **TMDB API** with `lru_cache` to avoid repeat calls
- Clean Netflix-style dark UI with skeleton loading, hover effects, and chained recommendations
- Responsive grid — works on mobile too

---

## 🛠️ Tech Stack

| Layer      | Technology                        |
|------------|-----------------------------------|
| Backend    | FastAPI, Uvicorn                  |
| ML         | Scikit-learn (Cosine Similarity)  |
| Data       | Pandas, NumPy                     |
| Frontend   | HTML, CSS, Vanilla JS             |
| Poster API | TMDB API                          |

---

## 📁 Project Structure
movie_recommnder/

│

├── model/

│   ├── app.py                      # FastAPI backend

│   ├── fast.py                     # (notebook exports)

│   ├── frontend.html               # Frontend UI

│   ├── movie_list.pkl              # Preprocessed movie data

│   ├── similarity.pkl              # Cosine similarity matrix

│   ├── vectorizer.pkl              # TF-IDF vectorizer

│   ├── recommandation-system.ipynb # Training notebook

│   ├── tmdb_5000_movies.csv        # Raw dataset

│   └── tmdb_5000_credits.csv       # Raw dataset

│

└── README.md

---

## ▶️ How to Run

**1. Install dependencies**
```bash
pip install fastapi uvicorn requests numpy pandas
```

**2. Start the API**
```bash
cd model
uvicorn app:app --reload
```

**3. Open the frontend**

Just open `frontend.html` directly in your browser — no extra server needed.

**4. Verify the API is working**
http://localhost:8000/health   → API status

http://localhost:8000/movies   → All movies list

http://localhost:8000/docs     → Swagger UI (test endpoints here)

---

## 🔌 API Endpoints

| Method | Endpoint                  | Description                        |
|--------|---------------------------|------------------------------------|
| GET    | `/health`                 | Health check                       |
| GET    | `/movies`                 | List all available movies          |
| GET    | `/recommend/{movie_name}` | Get 5 recommendations for a movie  |
| GET    | `/recommend/{movie_name}?n=10` | Get custom number of results  |

---

## 📊 How It Works

1. Movie metadata (genres, cast, crew, keywords) is combined into a single **tags** column
2. **TF-IDF Vectorization** converts tags into numerical vectors
3. **Cosine Similarity** measures how close two movies are in vector space
4. Top 5 most similar movies (excluding itself) are returned
5. Posters are fetched live from the **TMDB API**

---

## 📸 Demo

> Search any movie → get 5 recommendations with posters instantly.
> Click any recommended movie card to chain recommendations.

---

## 🔑 TMDB API

This project uses the [TMDB API](https://www.themoviedb.org/documentation/api) to fetch movie posters.
Get your free API key at [themoviedb.org](https://www.themoviedb.org/settings/api).
