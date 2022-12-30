import os
from urllib.parse import urlparse

from flask import (
    render_template,
    request,
    current_app,
    send_from_directory,
    make_response,
    Response,
)

from . import main
from .. import pages


@main.route("/", methods=["GET"], strict_slashes=False)
def home_page():
    page_title = "Acceuil"
    return render_template("index.html", **locals())


@main.route("/<path:path>/", methods=["GET"], strict_slashes=False)
def page(path):
    page = pages.get_or_404(path)
    template = page.meta.get('template', 'page.html')
    return render_template("page/page.html", page=page)


@main.route("/sitemap/", strict_slashes=False)
@main.route("/sitemap.xml/", strict_slashes=False)
def sitemap():

    host_components = urlparse(request.host_url)
    host_base = host_components.scheme + "://" + host_components.netloc

    static_urls = list()
    for rule in current_app.url_map.iter_rules():
        if (
            not str(rule).startswith("/contact/")
            and not str(rule).startswith("/favicon.png")
            and not str(rule).startswith("/sitemap/")
            and not str(rule).startswith("/sitemap.xml")
        ):
            if "GET" in rule.methods and len(rule.arguments) == 0:
                url = {
                    "loc": f"{host_base}{str(rule)}",
                    "changefreq": "weekly",
                    "priority": "0.9",
                }
                static_urls.append(url)

    xml_sitemap = render_template(
        "sitemap.xml", static_urls=static_urls, host_base=host_base
    )
    response = make_response(xml_sitemap)
    response.headers["Content-Type"] = "application/xml"

    return response


@main.route("/robots.txt/", methods=["GET"], strict_slashes=False)
def noindex():
    def Disallow(string):
        return f"Disallow: {string}"

    r = Response(
        "User-Agent: *\n{0}\n".format("\n".join([Disallow("/contact/")])),
        status=200,
        mimetype="text/plain",
    )
    r.headers["Content-Type"] = "text/plain; charset=utf-8"
    return r


@main.route("/favicon.png", methods=["GET"])
def favicon():
    return send_from_directory(
        os.path.join(current_app.root_path, "static"), "img/logo/favicon.png"
    )
