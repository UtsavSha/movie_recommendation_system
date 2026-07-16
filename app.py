from flask import Flask, render_template, request, jsonify
import pickle
import requests
import os
import gdown

app = Flask(__name__)

# --- Load Data ---
movies_df = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_df['title'].values.tolist()

# Download similarity matrix if it doesn't exist
if not os.path.exists("similarity.pkl"):
    url = "https://drive.google.com/uc?id=1OEEfJPAv05eiyTdk0K_jkRJTPhrIcnT0"
    gdown.download(url, "similarity.pkl", quiet=False)

with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{
        movie_id}?api_key=bf790a5e0dde40a0296ff4b6dda0c997&language=en-US"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if data.get("poster_path"):
            return "https://image.tmdb.org/t/p/w500" + data["poster_path"]

    except Exception as e:
        print(f"Poster Error ({movie_id}): {e}")

    # Return local default image
    return "/static/image.png"


def get_recommendations(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),
                        reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        movie_id = movies_df.iloc[i[0]].movie_id
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies_df.iloc[i[0]].title)

    return recommended_movies, recommended_movies_posters

# --- Routes ---


@app.route('/')
def index():
    # Renders the HTML and passes the movie list for the dropdown
    return render_template('index.html', movies=movies_list)


@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    movie_name = data.get('movie')

    try:
        names, posters = get_recommendations(movie_name)
        return jsonify({'status': 'success', 'names': names, 'posters': posters})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
