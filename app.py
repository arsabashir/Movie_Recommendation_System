#importing dependencies
from flask import Flask, render_template, request, jsonify
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__) #creates web app, .app is now a server

#loading the data 
movie_data = pd.read_csv('movies.csv')

#filling the null values
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
for feature in selected_features:
    movie_data[feature] = movie_data[feature].fillna('') #fills empty cells so TF-IDF doesnt crash

#combining the features
#combining the selected features
combined_features = movie_data['genres']+ ' '+movie_data['keywords'] +' '+movie_data['tagline']+ ' '+movie_data['cast']+ ' '+movie_data['director']

#TF-ID Vectorizer
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

#Cosine similarity
similarity = cosine_similarity(feature_vectors)

#Movie title list
list_of_all_movies = movie_data['title'].tolist()
print(list_of_all_movies)

@app.route('/') #when someone visits the main URL, run the func below i.e., sends html file
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST']) #accepts data being sent to it, reads movie name from frontend and removes any acc spaces
def recommend():
    data = request.get_json()
    movie_name = data.get('movie_name', '').strip()
    if not movie_name:
        return jsonify({'error': 'Please enter a movie name'}),400
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_movies)
    if not find_close_match:
        return jsonify({'error': 'Movie not found. Try another title!'}), 400
    
    close_match = find_close_match[0]
    index_of_movie = movie_data[movie_data.title==close_match]['index'].values[0]
    similarity_score = list(enumerate(similarity[index_of_movie]))
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    recommendations = []
    i = 1
    for movie in sorted_similar_movies:
     index = movie[0]
     title_from_index = movie_data[movie_data.index==index]['title'].values[0]
     if (i < 30):
      recommendations.append(title_from_index)
      i+=1

    return jsonify({
       'matched': close_match,
       'recommendations': recommendations
    })

if __name__ == '__main__':
   app.run(debug=True)
