from os import urandom, environ, path


BASE_DIR = path.abspath(path.dirname(__file__))


class Config:

    DEBUG = False
    DEVELOPMENT = False

    SECRET_KEY = environ.get("SECRET_KEY", urandom(24))
    SITE_NAME = "Venone"
    EMAIL_ADDRESS = "support@venone.app"
    EMAIL_ADDRESS_CONTACT = "contact@venone.app"
    PHONE_NUMBER = "(+225) 01 0137 6322"
    PHONE_NUMBER_TWO = "(225) 07 5795 0079"
    PHONE_NUMBER_THREE = "(225) 01 7121 0836"
    FLATPAGES_EXTENSION = ".md"
    FLATPAGES_MARKDOWN_EXTENSIONS = ["codehilite"]
    SLOW_DB_QUERY_TIME = 0.5
    WEBSITE_BUILDER = "https://www.venone.app"

    CRM_BUILDER = "https://gestion.venone.app"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = environ.get(
        "DEV_DATABASE_URL"
    ) or "sqlite:///" + path.join(BASE_DIR, "dev.sqlite3")


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL") or "sqlite:///" + path.join(
        BASE_DIR, "prod.sqlite3"
    )

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    "prod": ProductionConfig,
    "dev": DevelopmentConfig,
}
