import os
from flask import Flask, request, redirect, render_template, url_for
from lib.database_connection import get_flask_database_connection
from lib.album import Album
from lib.album_repository import AlbumRepository
from lib.artist import Artist
from lib.artist_repository import ArtistRepository
from lib.album_parameters_validator import AlbumParametersValidator
from lib.artist_parameters_validator import ArtistParametersValidator

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


@app.route("/")
def get_main():
    return render_template("main.html")

@app.route("/about")
def get_about():
    return render_template("about.html")

@app.route('/albums')
def get_all_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template("albums/index.html", albums=albums)


# @app.route('/albums/<id>')
# def get_the_artist_for_album(id):
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     album = repository.find(id)
#     artist_id = album.artist_id
#     artist_repository = ArtistRepository(connection)
#     artist = artist_repository.find(artist_id)
#     return render_template("albums/one_album.html", one_album=album, artist_name=artist)


@app.route('/albums/<id>')
def get_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id)
    return render_template("albums/show.html", album=album)

@app.route('/artists')
def get_all_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template("artists/index.html", artists=artists)

@app.route('/artists/<id>')
def get_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = repository.find(id)
    return render_template("artists/show.html", artist=artist)

@app.route('/albums/new', methods=['GET'])
def get_album_new():
    return render_template("albums/new.html")

@app.route('/albums', methods=['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    validator = AlbumParametersValidator(
        request.form['title'],
        request.form['release_year']
    )

    if not validator._is_valid():
        errors = validator.generate_errors()
        return render_template("albums/new.html", errors=errors)
    album = Album(
        None,
        validator.get_valid_title(),
        validator.get_valid_release_year(),
        1)
    repository.create(album)

    return redirect(f"/albums/{album.id}")


@app.route('/albums/<int:id>/delete', methods=['POST'])
def delete_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    repository.delete(id)
    return redirect(url_for('get_all_albums'))


@app.route('/artists', methods=['POST'])
def create_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    validator = ArtistParametersValidator(
        request.form['name'],
        request.form['genre']
    )

    if not validator._is_valid():
        errors = validator.generate_errors()
        return render_template("artists/new.html", errors=errors)
    artist = Artist(
        None,
        validator.get_valid_name(),
        validator.get_valid_genre()
        )
    repository.create(artist)

    return redirect(f"/artists/{artist.id}")




# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
# from example_routes import apply_example_routes
# apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
