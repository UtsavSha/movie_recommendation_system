# Movie Recommender System 🎬

A modern, AI-powered web application that provides personalized movie recommendations. Simply search for a movie you love, and the system will suggest 5 similar films based on content analysis, genre, cast, and crew.

## 🚀 Live Demo
Check out the live application here: **[https://movie-recommendation-system-xg7i.onrender.com/]**

---

## 🛠 Features
*   **Intelligent Recommendations:** Uses Cosine Similarity to find movies with similar plot overviews, genres, keywords, cast, and directors.
*   **Modern UI:** Built with a custom "Glassmorphism" interface for a premium, cinematic experience.
*   **Search & Discover:** Includes a robust search bar with real-time autocomplete to help you find movies in the database instantly.
*   **Full Library Browser:** A dedicated modal to browse the entire movie library alphabetically.
*   **Dynamic Poster Fetching:** Automatically retrieves real-time movie posters using The Movie Database (TMDB) API.

---

## 🏗 Technology Stack
*   **Backend:** Python, Flask, Gunicorn
*   **Frontend:** HTML5, CSS3 (Outfit Font), JavaScript
*   **Data Processing:** Pandas, NumPy, Scikit-Learn
*   **Deployment:** Render
*   **API:** TMDB API (The Movie Database)

---

## 📂 Project Structure
```text
movie-recommender/
├── app.py                 # Main Flask application logic
├── requirements.txt       # Dependencies
├── movies.pkl             # Serialized movie data
├── similarity.pkl         # Precomputed cosine similarity matrix
├── templates/
│   └── index.html         # Frontend interface
└── static/
    └── image.png          # Default fallback image
```

---


## ⚙️ How it works
*   **Data Preprocessing:** The system merges movie metadata and credits, then cleans the data by removing null values and duplicates[cite: 1].
*   **Tag Engineering:** It creates a "tag" for each movie by combining its overview, genres, keywords, cast, and director[cite: 1].
*   **Vectorization:** It uses CountVectorizer to convert these tags into numerical vectors, limiting features to the top 5,000 words[cite: 1].
*   **Recommendation Engine:** It calculates the cosine similarity between movie vectors to find the most closely related films[cite: 1].

## 🔧 Installation & Running Locally
1. Clone this repository:
   ```bash
   git clone [https://github.com/your-username/movie-recommender.git](https://github.com/your-username/movie-recommender.git)

   
Install the required dependencies:
```bash
pip install -r requirements.txt
```

Run the application:
```bash
python app.py
```

🤝 Contributing
Contributions are welcome! If you find a bug or have an idea for an improvement, feel free to open an issue or submit a pull request.

Built by [Utsav Sharma]
