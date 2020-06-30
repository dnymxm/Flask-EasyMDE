import flask

import pytest

from flask_easymde import EasyMDE

TEMPLATE = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Flask-EasyMDE</title>
    {{ easymde.css }}
    {{ easymde.js }}
  </head>
  <body>
    {{ easymde.load }}
    {{ easymde.load_id("editor") }}
  </body>
</html>
"""

STATIC_CSS = '/static/easymde/easymde.min.css'
STATIC_JS = '/static/easymde/easymde.min.js'


def create_client():
    app = flask.Flask(__name__)
    app.config['TESTING'] = True

    EasyMDE(app)

    @app.route('/')
    def index():
        return flask.render_template_string(TEMPLATE)

    return app.test_client()

def test_serve_static_simplemde_css_file():
    client = create_client()
    response = client.get(STATIC_CSS)
    assert response.status_code == 200


def test_serve_static_simplemde_js_file():
    client = create_client()
    response = client.get(STATIC_JS)
    assert response.status_code == 200