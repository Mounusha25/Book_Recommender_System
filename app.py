import streamlit as st
import pickle
import numpy as np
from pathlib import Path

# ────────────────────────── CONFIG ──────────────────────────
st.set_page_config(
    page_title="NextPage Guru ▸ Book Recommender",
    page_icon="📚",
    layout="centered",
)

# ────────────────────────── STYLE  ──────────────────────────
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
        background: radial-gradient(circle at 10% 30%, #fefcff 0%, #e6efff 100%);
    }

    .title-gradient {
        display:flex;gap:0.5rem;align-items:center;font-size:2.4rem;font-weight:700;
        background:linear-gradient(90deg,#ff8a00,#e52e71,#7b00ff);
        -webkit-background-clip:text;-webkit-text-fill-color:transparent;
        margin-bottom:1.2rem;
    }

    .card{background:#fff;border-radius:14px;box-shadow:0 6px 18px rgba(0,0,0,.06);padding:0.8rem;text-align:center;animation:fadeIn .6s ease both;}
    .card img{width:140px;height:auto;border-radius:10px;box-shadow:0 3px 8px rgba(0,0,0,.1);}
    .card .book-title{font-size:0.9rem;font-weight:600;color:#333;margin-top:0.6rem;}

    @keyframes fadeIn{from{transform:translateY(25px);opacity:0;}to{transform:translateY(0);opacity:1;}}
    </style>
    """,
    unsafe_allow_html=True,
)

# ────────────────────────── HEADER ──────────────────────────
st.markdown(
    '<div class="title-gradient">📚 NextPage Guru Book Recommender</div>',
    unsafe_allow_html=True,
)
st.subheader("Find your next favorite book!")

# ────────────────────────── LOAD DATA ───────────────────────
ARTIFACT_PATH = Path("artifacts")
model = pickle.load(open(ARTIFACT_PATH / "model.pkl", "rb"))
books_name = pickle.load(open(ARTIFACT_PATH / "books.pkl", "rb"))
final_ratings = pickle.load(open(ARTIFACT_PATH / "final_rating.pkl", "rb"))
book_pivot = pickle.load(open(ARTIFACT_PATH / "book_pivot.pkl", "rb"))

selected_books = st.selectbox("Select a book to get recommendations:", books_name)

# ────────────────────────── HELPERS ─────────────────────────


def fetch_poster(suggestions):
    poster_url = []
    for idx in suggestions[0]:
        title = book_pivot.index[idx]
        match = final_ratings.loc[final_ratings["title"] == title, "image_url"]
        poster_url.append(match.values[0] if not match.empty else "")
    return poster_url


def recommend_books(book_name, n_recommendations=5):
    book_id = np.where(books_name == book_name)[0][0]
    distances, suggestions = model.kneighbors(
        book_pivot.iloc[book_id, :].values.reshape(1, -1),
        n_neighbors=n_recommendations + 1,
    )
    posters = fetch_poster(suggestions)
    titles = [book_pivot.index[i] for i in suggestions.flatten()]
    return titles[1:], posters[1:]  # skip the first (input book)


# ────────────────────────── MAIN ACTION ─────────────────────
if st.button("Show Recommendations 🚀"):
    with st.spinner("Literary gems incoming…"):
        rec_titles, rec_posters = recommend_books(selected_books)

    st.success("Your recommendations:")

    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]
    for col, title, poster in zip(columns, rec_titles, rec_posters):
        with col:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.image(poster, width=140)
            st.markdown(
                f'<div class="book-title">{title}</div>', unsafe_allow_html=True
            )
            st.markdown("</div>", unsafe_allow_html=True)

    st.balloons()
