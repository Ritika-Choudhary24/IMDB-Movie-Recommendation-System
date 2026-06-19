# 🎬 IMDb Movie Recommendation System


This project aims to build a content-based movie recommendation system that not only suggests films you'll love, but also lets you compare how different algorithms arrive at those suggestions.
It leverages three similarity techniques — **Jaccard Similarity** for genre set overlap, **TF-IDF Cosine Similarity** for weighted genre relevance, and **Gower KNN** for a multi-feature composite score across genre, year, rating, and runtime.
All three algorithms run in parallel on a dataset of **16,000+ IMDb movies (1980–2026)**, and their scores are averaged to produce a final, balanced recommendation.
The result is an interactive **Streamlit** web app where you can explore recommendations and visually compare algorithm performance side by side.

---

## 🚀 Live Demo

👉 **[Try the App Here](https://imdb-movie-recommendation-system-cegpa4wlqgdohnlwwvdmx3.streamlit.app/)**

---

## 📌 Features

- Search and select from 16,000+ IMDb movies by title and year
- Get the **top 5 personalized recommendations** based on your chosen movie
- Compare three recommendation algorithms side-by-side with a bar chart
- Clean, modern dark UI with a gradient background
- Fully deployed and accessible via browser — no installation needed

---

## 🧠 How It Works

This is a **content-based filtering** system. When you select a movie, the app computes similarity scores between it and every other movie in the dataset using three different algorithms, then averages them to produce a final ranked recommendation list.

### Algorithms

| Algorithm | What it measures |
|---|---|
| **Jaccard Similarity** | Overlap between genre sets (e.g. both are Action + Thriller) |
| **TF-IDF Cosine Similarity** | Weighted genre importance using term frequency–inverse document frequency |
| **Gower KNN** | A composite score combining genres (55%), release year (20%), IMDb rating (15%), and runtime (10%) |

The final recommendation score is the **average of all three algorithms**, giving a balanced result that considers both content overlap and contextual features.

---

## 🗂️ Project Structure

```
IMDB-Movie-Recommendation-System/
│
├── Recommend.py                    # Main Streamlit application
├── IMDB_movie_recommend.ipynb      # Exploratory data analysis notebook
├── imdb_top_movies_1980_2026.csv   # Dataset (16,000+ IMDb movies)
└── requirements.txt                # Python dependencies
```

---

## 📊 Dataset

The dataset `imdb_top_movies_1980_2026.csv` contains movies from **1980 to 2026** with the following fields used in the recommendation engine:

- `imdb_id` — Unique movie identifier
- `title` — Movie title
- `year` — Release year
- `genres` — Comma-separated genre tags
- `average_rating` — IMDb user rating
- `runtime_minutes` — Movie duration

---

## 🛠️ Tech Stack

- **Python** — Core language
- **Streamlit** — Web app framework
- **Pandas / NumPy** — Data processing
- **scikit-learn** — TF-IDF vectorization and cosine similarity
- **Streamlit Cloud** — Deployment

---

## ⚙️ Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ritika-Choudhary24/IMDB-Movie-Recommendation-System.git
   cd IMDB-Movie-Recommendation-System
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the app**
   ```bash
   streamlit run Recommend.py
   ```

4. Open your browser at `http://localhost:8501`

---

## 📸 App Preview

The app features:
- A **movie search box** with autocomplete
- A **Recommend** button that triggers all three algorithms
- A **results table** showing top 5 picks with title, year, genres, IMDb rating, and similarity score
- A **bar chart** comparing the average similarity score each algorithm assigned to the recommendations

---

## 👩‍💻 Author

**Ritika Choudhary**

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
