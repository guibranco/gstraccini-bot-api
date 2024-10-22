from flask import Flask
from .debugger_options import debugger_options_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(debugger_options_bp)
