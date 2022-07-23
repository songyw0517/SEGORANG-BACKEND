"""Response Shortcuts"""
""" Response 정의 """
from app.api import Response_metaclass
class Response(Response_metaclass):
    # 200~ : Success response
    @staticmethod
    def response_ok(result=None):
        return {
            'msg':'success',
            'status_code':200,
            'status_msg':'OK',
            'result': result
        }, 200

    @staticmethod
    def response_no_content(result=None):
        return {
            'msg':'success',
            'status_code':204,
            'status_msg':'No Content',
            'result': result
        }, 204
    
    @staticmethod
    def response_partial_content(result=None):
        return {
            'msg':'success',
            'status_code':206,
            'status_msg':'Partial Content',
            'result': result
        }, 206

    
    # 300~ : Redirection
    @staticmethod
    def response_moved_permanently(description=None):
        pass

    @staticmethod
    def response_found(description=None):
        pass

    @staticmethod
    def response_see_other(description=None):
        pass

    @staticmethod
    def response_not_modified(description=None):
        pass

    @staticmethod
    def response_temporary_redirect(description=None):
        pass

    # 400~ : Client Error
    @staticmethod
    def response_bad_request(description=None):
        return {
            'msg': 'fail',
            'status_code':400,
            'status_msg':'Bad Request',
            'description': description
        }, 400
    
    @staticmethod
    def response_unauthorized(description=None):
        return {
            'msg': 'fail',
            'status_code':401,
            'status_msg':'Unauthorized',
            'description': description
        }, 401


    @staticmethod
    def response_forbidden(description=None):
        return {
            'msg': 'fail',
            'status_code':403,
            'status_msg':'Forbidden',
            'description': description
        }, 403

    @staticmethod
    def response_not_found(description=None):
        return {
            'msg': 'fail',
            'status_code':404,
            'status_msg':'Not Found',
            'description': description
        }, 404

    @staticmethod
    def response_method_now_allowed(description=None):
        return {
            'msg': 'fail',
            'status_code':405,
            'status_msg':'Mothod Not Allowed',
            'description': description
        }, 405

    # 500~ : Server Error
    @staticmethod
    def response_internal_server_error(description=None):
        return {
            'msg': 'fail',
            'status_code':500,
            'status_msg':'Internal Server Error',
            'description': description
        }, 500
    
    @staticmethod
    def response_service_unavailable(description=None):
        return {
            'msg': 'fail',
            'status_code':503,
            'status_msg':'Service Unavailable',
            'description': description
        }, 503
    
    @staticmethod
    def response_gateway_timeout(description=None):
        return {
            'msg': 'fail',
            'status_code':504,
            'status_msg':'Gateway Timeout',
            'description': description
        }, 504
    
    @staticmethod
    def response_http_version_not_supported(description=None):
        return {
            'msg': 'fail',
            'status_code':505,
            'status_msg':'HTTP Version Not Supported',
            'description': description
        }, 505