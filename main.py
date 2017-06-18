from flask import Flask
import random

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()
    tomorrowsmovie = get_random_movie()

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"

    content += "<h1>Tomorrow's Movie</h1>"
    content += "<ul>"
    content += "<li>" + tomorrowsmovie + "</li>"
    content += "</ul>"

    return content

def get_random_movie():
    movies = ["Memento","Amelie","Schindler's List","Toy Story","Robots","Inception"]
    return random.choice(movies)

app.run()
