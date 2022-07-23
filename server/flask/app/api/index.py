from flask import Blueprint, render_template
class index:
    bp = Blueprint('index', __name__)

    @bp.route('/')
    def index():
        return render_template('index.html')