# Flask-EasyMDE - a Flask extension for EasyMDE
Flask-EasyMDE is a [Flask](https://flask.palletsprojects.com/en/1.1.x/) implementation for [EasyMDE Markdown Editor](https://easymde.tk/).

EasyMDE is itself a fork of abandoned SimpleMDE project which brings some changes and fix compatibility bugs.

Thank's to @Ionaru for his work on EasyMDE 🙏

This extension is based on [Flask-SimpleMDE](https://github.com/pyx/flask-simplemde) code which was the Flask implementation for SimpleMDE.

### How To Use? 
1. **Installation**

    ```zsh
    pip install Flask-EasyMDE
    ```

2. **Instantiate EasyMDE with your Flask app**

    ```python
    from flask import Flask
    from flask_easymde import EasyMDE

    app = Flask(__name__)
    mde = EasyMDE(app)
    ```

    Works with application factory pattern too trough `init_app()` method: 

    ```python
    from flask import Flask
    from flask_easymde import EasyMDE

    mde = EasyMDE()

    def create_app():
        app = Flask(__name__)
        mde.init_app(app)
    ```

3. **Load static files and EasyMDE editor directly in your template:**

    ```html
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>Flask-EasyMDE example</title>
            {{ easymde.css }}
            {{ easymde.js }}
        </head>
        <body>
            <textarea>
            Some Markdown Text Here
            </textarea>
            {{ easymde.load }}
        </body>
    </html>
    ```
### How It Works?
Once registered, this extension provides a template variable called `easymde`, it has:

- a property named `css` that will be rendered as HTML `<link>` tag to the EasyMDE stylesheet.

    `{{ easymde.css }}`

- a property named `js` that will be rendered as HTML `<script>` tag to the EasyMDE.

    `{{ easymde.js }}`

- a property named `load` that will be rendered as HTML `<script>` tag with javascript code that loads the EasyMDE Markdown Editor **for the first `<textarea>` tag found in the template.**

    ``{{ easymde.load }}``

- a method named `load_id` that when called with a string, will be rendered as HTML `<script>` tag with javascript code that loads the EasyMDE Markdown Editor with the `<textarea>` tag **which has the specified id attribute.**

```html
<textarea id="editor"></textarea>
...
{{ easymde.load_id("editor") }}
```
### License
BSD 2-Clause "Simplified" License
