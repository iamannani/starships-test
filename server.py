from flask import Flask, jsonify, make_response
import requests
import json


app = Flask(__name__)


@app.route("/starships")
def get_movies():
    # Collect all movie names and hyperdrive_rating
    movies = []
    movie_without_hyperdrive = []
    movie_with_hyperdrive = []
    # Grab the search results
    paginated_movies, data = fetch_data("https://swapi.co/api/starships/")
    if (paginated_movies, data) == (None, None):
        return make_response(jsonify({'error': 'swapi might be down'}), 400)
    movies = movies + paginated_movies
    # While data['next'] isn't empty, let's download the next page, too
    while data['next'] is not None:
        paginated_movies, data = fetch_data(data['next'])
        movies = movies + paginated_movies
    for movie in movies:
        if movie["hyperdrive"] != "unknown":
            movie_with_hyperdrive.append(movie)
        else:
            movie_without_hyperdrive.append(movie)
    movie_with_hyperdrive = sorted(movie_with_hyperdrive, key=lambda k: k['hyperdrive']) 
    response = [{"starships": movie_with_hyperdrive}, {"starships_unknown_hyperdrive": movie_without_hyperdrive}]
    return jsonify({"results": response})


def fetch_data(url):
    response = requests.get(url)
    try:
        data = response.json()
        paginated_movies = [{"name":movie["name"], "hyperdrive": movie["hyperdrive_rating"]} for movie in data["results"]]
    except json.decoder.JSONDecodeError:
        return None, None
    return paginated_movies, data


if __name__ == '__main__':
    app.run(debug=True)