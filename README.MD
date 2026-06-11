# 🎬 Movie Recommender System

A simple machine learning-based movie recommendation system built using **Streamlit** and **Cosine Similarity**. It suggests movies similar to the one selected by the user and displays their poster images.

---

## 🚀 Features
- Content-based movie recommendations using cosine similarity
- Clean and intuitive Streamlit UI
- Fetch movie posters dynamically using TMDB API
- Fast inference with precomputed similarity matrix
- Graceful error handling with fallback images

---

## 🛠️ Tech Stack
- **Python** — Core language
- **Pandas** — Data manipulation
- **Scikit-learn** — Similarity calculations (cosine similarity)
- **Streamlit** — Web UI framework
- **Requests** — HTTP requests for TMDB API
- **python-dotenv** — Environment variable management

---

## 📋 Prerequisites
- Python 3.8 or higher
- TMDB API Key (get one free at [https://www.themoviedb.org/settings/api](https://www.themoviedb.org/settings/api))

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/CaffineDuck67/movie-recommender-system.git
cd movie-recommender-system
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the project root and add your TMDB API key:
```
TMDB_API_KEY=your_api_key_here
```

You can use `.env.example` as a template:
```bash
cp .env.example .env
```

### 5. Run the application
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 🎯 How to Use
1. Open the application in your browser
2. Select a movie from the dropdown menu
3. Click the "Show Recommendation" button
4. View 5 similar movies with their posters

---

## 📁 Project Structure
```
movie-recommender-system/
├── app.py                           # Main Streamlit application
├── recommandation-system.ipynb      # Jupyter notebook with ML model training
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment variables template
├── movie_list.pkl                   # Pickled movie dataset (generated)
├── similarity.pkl                   # Precomputed similarity matrix (generated)
└── README.MD                        # This file
```

---

## 🔒 Security Notes
- **Never commit your `.env` file** with actual API keys to version control
- The `.env` file is listed in `.gitignore` for safety
- Your TMDB API key is loaded securely from environment variables
- For Streamlit Cloud deployment, add secrets in the Streamlit dashboard instead of `.env`

---

## 🚀 Deployment

### Deploy to Streamlit Cloud
1. Push your code to GitHub
2. Go to [https://share.streamlit.io](https://share.streamlit.io)
3. Connect your repository and select this branch
4. In the Streamlit Cloud dashboard, add your TMDB API key under **Secrets**

---

## 📊 Model Details
- **Algorithm**: Cosine Similarity on content features
- **Data Source**: Movie dataset with various features (genres, keywords, overview, etc.)
- **Features Used**: Genres, keywords, cast, crew, and overview (preprocessed and vectorized)
- **Training**: See `recommandation-system.ipynb` for the complete ML pipeline

---

## 🐛 Troubleshooting

**Issue**: `ModuleNotFoundError: No module named 'streamlit'`
- Solution: Run `pip install -r requirements.txt`

**Issue**: `KeyError: movie_list.pkl not found`
- Solution: Ensure you're running the app from the project root directory

**Issue**: Posters not loading (showing placeholder images)
- Solution: Check your TMDB API key is valid and your internet connection is working

**Issue**: `.env` file not being read
- Solution: Ensure the file is in the project root and named exactly `.env`

---

## 📝 License
This project is open source and available under the MIT License.

---

## 🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 👤 Author
**CaffineDuck67** — [GitHub Profile](https://github.com/CaffineDuck67)

---

## ⭐ Show your support
If you found this helpful, please give it a star!
