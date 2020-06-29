from flask import Blueprint, Markup, url_for


CSS = 'easymde.min.css'
CSS_LINK_TEMPLATE = '<link rel="stylesheet" href="{}">'

JS = 'easymde.min.js'
JS_LINK_TEMPLATE = '<script src="{}"></script>'

JS_LOAD = """<script> 
var easymde = new EasyMDE();
</script>
"""

JS_LOAD_WITH_ID = """<script>
var easymde = new EasyMDE({{element: document.getElementById("{}")}});
</script>
"""

EXTENSION = 'easymde'
STATIC_ENDPOINT = EXTENSION + '.static'


class EasyMDE(object):
    """Flask-EasyMDE extension"""

    def __init__(self, app=None):
        self.app = app

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Create and register a blueprint with the Flask application."""

        easymde = Blueprint(
            EXTENSION,
            __name__,
            static_folder='static',
            static_url_path=app.static_url_path + '/' + EXTENSION)

        app.register_blueprint(easymde)

        if not hasattr(app, 'extensions'):
            app.extensions = {}

        app.extensions[EXTENSION] = self
        app.context_processor(lambda: {EXTENSION: self})

    @property
    def css(self):
        """Link for CSS file"""
        return Markup(CSS_LINK_TEMPLATE.format(url_for(STATIC_ENDPOINT, filename=CSS)))

    @property
    def js(self):
        """Link for JS file"""
        return Markup(JS_LINK_TEMPLATE.format(url_for(STATIC_ENDPOINT, filename=JS)))

    @property
    def load(self):
        """Renders JavaScript loading code for the first textarea found in your html file"""
        return Markup(JS_LOAD)

    def load_id(self, id):
        """Renders JavaScript loading code for a specific id"""
        return Markup(JS_LOAD_WITH_ID.format(id))
