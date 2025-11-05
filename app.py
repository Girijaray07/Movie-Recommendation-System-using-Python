
import pickle
from flask import Flask, request, jsonify
import pandas as pd

try:
    with open('dataset_and_similarity.pkl', 'rb') as f:
        df, similarity, movies = pickle.load(f)
except FileNotFoundError:
    print("Error: 'dataset_and_similarity.pkl' not found. Make sure the file is in the same directory as app.py.")
    exit()

app = Flask(__name__)

@app.route('/recommend', methods=['GET'])
def recommend():
    movie_title = request.args.get('movie')
    if not movie_title:
        return jsonify({"error": "Missing 'movie' parameter"}), 400

    movie_title = movie_title.title()

    if movie_title not in df['title'].values:
        return jsonify({"error": f"Movie '{movie_title}' not found in the dataset."}), 404

    index = df[df['title'] == movie_title].index[0]
    distance_arr = list(enumerate(similarity[index]))
    sorted_distances = sorted(distance_arr, reverse=True, key=lambda x: x[1])[0:6]
    
    recommendations = []
    for i in sorted_distances:
        movie_id = df.iloc[i[0]].movie_id
        # Using the original 'movies' dataframe to get the homepage
        homepage = movies[movies['id'] == movie_id]['homepage'].values[0]
        recommendations.append({
            "title": df.iloc[i[0]].title,
            "homepage": homepage
        })

    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
