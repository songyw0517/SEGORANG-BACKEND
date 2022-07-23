from flask import Blueprint, render_template

from app.api.response import Response

class index:
    bp = Blueprint('index', __name__)

    @bp.route('/')
    def index():
        return render_template('index.html')

    @bp.route('/response_test')
    def res_test():
        return Response.response_200()