from flask import render_template

from . import main
from .. import pages


@main.route("/", strict_slashes=False)
def home_page():
    page_title = "Acceuil"
    return render_template("index.html", **locals())
