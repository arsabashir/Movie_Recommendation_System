# 🎬 Movie Recommendation System

A content-based movie recommendation system that takes a movie name as input and returns similar movies using cosine similarity on movie metadata.

---

## 📌 Overview

This project recommends movies similar to a user-provided title by analyzing movie features (such as genres, keywords, cast, etc.) from a dataset and computing similarity scores using machine learning techniques.

**How it works:**
1. User inputs a movie name
2. The system processes the movie's metadata
3. Cosine similarity is computed across all movies in the dataset
4. Top N most similar movies are returned as recommendations

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas & NumPy | Data loading and manipulation |
| Scikit-learn | TF-IDF vectorization & cosine similarity |
| CSV Dataset | Movie metadata |

---

## 📁 Project Structure

```
movie-recommendation-system/
│
├── dataset/
│   └── movies.csv            # Movie metadata dataset
│
├── recommendation.py         # Core recommendation logic
├── requirements.txt          # Python dependencies
└── README.md
```

> ⚠️ If your dataset is large (>50MB), add it to `.gitignore` and mention the source below instead.

---

## ⚙️ Setup & Usage

### 1. Clone the repository
```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the system
```bash
python recommendation.py
```

### 4. Enter a movie name when prompted
```
Enter a movie name: Inception
```

**Output:**
```
Movies similar to 'Inception':
1. Interstellar
2. The Prestige
3. Shutter Island
4. Memento
5. The Dark Knight
```

---

## 📊 Dataset

<!-- Replace with your actual dataset source -->
- **Source:** [TMDB 5000 Movie Dataset – Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- **Size:** ~5000 movies
- **Key columns used:** title, genres, keywords, cast, crew (adjust as per your dataset)

---

## 🧠 How the Recommendation Works

1. **Feature Extraction** – Relevant columns (genres, keywords, etc.) are combined into a single text "tag" per movie
2. **TF-IDF Vectorization** – Text is converted to numerical vectors using `TfidfVectorizer`
3. **Cosine Similarity** – Similarity scores between all movie pairs are computed
4. **Ranking** – Top matches (excluding the input movie) are returned

---

## 🔮 Future Improvements

- [ ] Add a web interface (Flask / Streamlit)
- [ ] Include collaborative filtering for personalized recommendations
- [ ] Integrate with TMDB API for live movie posters and details
- [ ] Deploy on Render / Hugging Face Spaces

---

## 🙋‍♂️ Author

**Arsa**  
AI Program Student | Aspiring Full-Stack Developer  
[GitHub](https://github.com/your-username) • [LinkedIn](https://linkedin.com/in/your-profile)

---

## 📄 License

This project is open source under the [MIT License](LICENSE).
