from flask import Blueprint, jsonify, request
from werkzeug.exceptions import HTTPException
from app.api.response import not_found, bad_request

class error_handler:
    bp = Blueprint("error_handler", __name__)

    @bp.app_errorhandler(400)
    def bad_request_error(error: HTTPException):
        """400 Error Handler"""
        return bad_request(error.description)


    @bp.app_errorhandler(404)
    def not_found_error(error: HTTPException):
        """404 Error Handler"""
        return not_found


    @bp.app_errorhandler(500)
    def internal_server_error(error):
        """500 Error Handler (production only)"""
        return jsonify(msg=str(error)), 500