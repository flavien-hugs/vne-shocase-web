import os
import logging as lg

from app import create_app, db

from dotenv import load_dotenv
from flask_migrate import Migrate, upgrade


dotenv_path = os.path.join(os.path.dirname(__file__), ".flaskenv")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

app = create_app(os.getenv("FLASK_CONFIG") or "dev")
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    pass


@app.cli.command("init_db")
def init_db():
    pass


if __name__ == "__main__":
    app.run(threaded=True)
