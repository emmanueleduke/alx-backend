from flask import Flask, request, g
from flask_babel import Babel, _
from babel import Locale

app = Flask(__name__)
babel = Babel(app)

# Supported locales
supported_locales = ["en", "fr"]

@babel.localeselector
def get_locale():
    # Check if the 'locale' parameter is in the request's query string
    locale = request.args.get("locale")

    if locale in supported_locales:
        return locale  # Use the provided locale
    else:
        # Resort to the default behavior or fallback to the user's preferred locale
        return request.accept_languages.best_match(supported_locales)

@app.route('/')
def index():
    return _("This is a level 1 heading")

if __name__ == '__main__':
    app.run(host='0.0.0.0')

