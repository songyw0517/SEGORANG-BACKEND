from flask import Blueprint, jsonify, request
from werkzeug.exceptions import HTTPException
from app.api.response import Response

class error_handler:
    bp = Blueprint("error_handler", __name__)

    @bp.app_errorhandler(400)
    def bad_request_error(error: HTTPException):
        """400 Error Handler"""
        return Response.response_bad_request(error.description)


    @bp.app_errorhandler(404)
    def not_found_error(error: HTTPException):
        """404 Error Handler"""
        return Response.response_not_found(error.description)


    @bp.app_errorhandler(500)
    def internal_server_error(error):
        """500 Error Handler (production only)"""
        return Response.response_internal_server_error(error)