from flask import Flask
from .label_settings import label_settings_bp

app = Flask(__name__)
app.register_blueprint(label_settings_bp)
