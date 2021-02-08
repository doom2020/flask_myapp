from flask import Blueprint
from .action import HandlerGetMovies

movie = Blueprint('movie_api', __name__)


@movie.route('/movie', methods=['GET'])
def handler_movie_get():
    handler_get_movies = HandlerGetMovies()
    handler_get_movies.get_page_html()
    return 'get movies'


@movie.route('/movie', methods=['POST'])
def handler_movie_post():
    return 'post movies'
