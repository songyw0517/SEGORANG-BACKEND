from flask import Blueprint, request, jsonify
from sejong_univ_auth import auth, DosejongSession
class user:
    bp = Blueprint("user", __name__)

    # login API
    @bp.post("/login")
    def login():
        login_info = request.json
        result = auth(
                    id=login_info['id'], 
                    password=login_info['pw'], 
                    methods=DosejongSession)
        print(result)
        return jsonify(result)