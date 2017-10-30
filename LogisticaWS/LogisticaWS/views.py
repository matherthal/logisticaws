"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from LogisticaWS import app
try:
    # for Python 2.x
    from StringIO import StringIO
except ImportError:
    # for Python 3.x
    from io import StringIO
import csv


class Distance:
    def __init__(self, origin, destination, distance):
        self.origin = origin
        self.destination = destination
        self.distance = distance


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/mapa/<name>', methods = ['POST'])
def mapa(name):
    data = str(request.data, encoding="utf-8") 

    print(name)
    print(data)

    distances = []

    f = StringIO(data)
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        print('\t'.join(row))
        distances.append(Distance(row[0], row[1], row[2]))

    return distances


