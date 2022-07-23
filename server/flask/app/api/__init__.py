"""
API Request Handler and util
"""
from abc import ABCMeta, abstractmethod


def init_app(app):
    
    ####################### HTTP request handling ########################
    # 앱이 기동되고 나서 첫번째 HTTP 요청에만 응답한다.
    @app.before_first_request
    def before_first_request():
        print("0. 앱이 기동되고 나서 첫 번째 HTTP 요청에만 응답")
    
    # 매 HTTP 요청이 처리되기 전에 실행된다.
    @app.before_request
    def before_request():
        print("1. 매 HTTP 요청이 처리되기 전에 실행")

    # 매 HTTP 요청이 처리되고 나서 실행된다.
    @app.after_request
    def after_request(response):
        print("2. 매 HTTP 요청이 처리되고 나서 실행")
        return response
    
    # 매 HTTP요청의 결과가 브라우저에 응답하고 나서 호출된다.
    @app.teardown_request
    def teardown_request(exception):
        print("3. 매 HTTP요청의 결과가 브라우저에 응답하고 나서 호출")

    # HTTP요청의 어플리케이션 컨텍스트가 종료될 때 실행된다.
    @app.teardown_appcontext
    def teardown_appcontext(exception):
        print("4. HTTP요청의 어플리케이션 컨텍스트가 종료될때 실행")
        print("*"*30)


"""
Response metaclass (interface)
"""
class Response_metaclass(metaclass=ABCMeta):
    # 200~
    @abstractmethod
    def response_ok(result=None):
        pass

    @abstractmethod
    def response_no_content(result=None):
        pass
    @abstractmethod
    def response_partial_content(result=None):
        pass

    
    # 300~ : Redirection
    @abstractmethod
    def response_moved_permanently(description=None):
        pass

    @abstractmethod
    def response_found(description=None):
        pass

    @abstractmethod
    def response_see_other(description=None):
        pass

    @abstractmethod
    def response_not_modified(description=None):
        pass

    @abstractmethod
    def response_temporary_redirect(description=None):
        pass


    # 400~ : Client Error
    @abstractmethod
    def response_bad_request(description=None):
        pass
    
    @abstractmethod
    def response_unauthorized(description=None):
        pass

    @abstractmethod
    def response_forbidden(description=None):
        pass

    @abstractmethod
    def response_not_found(description=None):
        pass

    @abstractmethod
    def response_method_now_allowed(description=None):
        pass

    # 500~ : Server Error
    @abstractmethod
    def response_internal_server_error(description=None):
        pass
    
    @abstractmethod
    def response_service_unavailable(description=None):
        pass

    @abstractmethod
    def response_gateway_timeout(description=None):
        pass

    @abstractmethod
    def response_http_version_not_supported(description=None):
        pass