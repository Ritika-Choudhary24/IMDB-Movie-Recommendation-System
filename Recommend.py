import numpy as np
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Recommend & compare", page_icon="🎬")
st.markdown("""
<style>
.stApp{background:linear-gradient(135deg,#050505,#260116);color:white}
h1,h2,h3,p,label{color:white!important}
.stButton>button{background:#ff2d95;color:white;border:0;border-radius:10px}
[data-testid="stDataFrame"]{border:1px solid #ff2d95;border-radius:10px}
.footer{text-align:center;margin-top:35px;color:#ff83bf;font-weight:700}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv("imdb_top_movies_1980_2026.csv").dropna(
        subset=["title","year","genres","average_rating","runtime_minutes"]
    ).drop_duplicates("imdb_id").reset_index(drop=True)
    df["label"] = df["title"] + " (" + df["year"].astype(int).astype(str) + ")"
    return df

df = load_data()
matrix = TfidfVectorizer().fit_transform(df["genres"].str.replace(",", " "))

def scores(i):
    genres = df["genres"].str.split(",").apply(set)
    j = genres.apply(lambda x: len(x & genres[i]) / len(x | genres[i])).to_numpy()
    t = cosine_similarity(matrix[i], matrix).ravel()
    year = 1 - abs(df["year"] - df.loc[i,"year"]) / max(df["year"].max()-df["year"].min(),1)
    rating = 1 - abs(df["average_rating"]-df.loc[i,"average_rating"]) / 10
    runtime = 1 - abs(df["runtime_minutes"]-df.loc[i,"runtime_minutes"]) / max(df["runtime_minutes"].max()-df["runtime_minutes"].min(),1)
    g = .55*j + .20*year + .15*rating + .10*runtime
    return {"Jaccard":j, "TF-IDF Cosine":t, "Gower KNN":g}

st.title("🎬 Movie Recommender")
st.write("Type a movie name or select one from the list.")

movie = st.selectbox(
    "Movie",
    sorted(df["label"]),
    index=None,
    placeholder="Start typing a movie name..."
)

if st.button("Recommend", use_container_width=True):
    if not movie:
        st.warning("Please select a movie.")
    else:
        i = df.index[df["label"] == movie][0]
        s = scores(i)
        combined = np.mean(list(s.values()), axis=0)
        top = np.argsort(combined)[::-1]
        top = top[top != i][:5]

        result = df.loc[top, ["title","year","genres","average_rating"]].copy()
        result["Similarity"] = (combined[top] * 100).round(1).astype(str) + "%"
        result.columns = ["Movie","Year","Genres","IMDb Rating","Similarity"]

        st.subheader("Recommended Movies")
        st.dataframe(result, hide_index=True, use_container_width=True)

        comparison = pd.DataFrame({
            "Algorithm": s.keys(),
            "Average Similarity": [
                np.mean(np.sort(v[v < 0.999])[::-1][:5]) * 100 for v in s.values()
            ]
        }).set_index("Algorithm")

        st.subheader("Algorithm Similarity Comparison")
        st.bar_chart(comparison, y="Average Similarity", color="#ff2d95")

st.markdown('<div class="footer">Built with ❤️ by Ritika Choudhary</div>', unsafe_allow_html=True)
