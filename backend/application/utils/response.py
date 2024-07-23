import warnings
from enum import unique, Enum

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@unique
class ErrorCode(Enum):
    """
    api error code enumeration
    """
    # success code family
    SUCCESS = 200  # deprecated
    SUCCESS_CODE = 200_00

    # bad request family
    INVALID_REQUEST_ARGS = 400  # deprecated
    BAD_REQUEST_ERROR = 400_00
    INVALID_REQUEST_ARGUMENT_ERROR = 400_01
    REQUIRED_ARG_IS_NULL_ERROR = 400_02
    CANNOT_LOGIN_ERROR = 400_03

    # unauthorized family
    UNAUTHORIZED = 401  # deprecated
    UNAUTHORIZED_ERROR = 401_00
    INVALID_TOKEN_ERROR = 401_01

    # refuse family
    REFUSE_ACCESS = 403  # deprecated
    REFUSE_ACCESS_ERROR = 403_00

    # not found family
    ITEM_NOT_FOUND = 404  # deprecated
    NOT_FOUND_ERROR = 404_00

    # duplicated family
    ITEM_ALREADY_EXISTS = 409  # deprecated
    DUPLICATED_ERROR = 409_00


def _api_response(success, data) -> dict:
    """
    wrap an api response dict obj
    :param success: whether the request is handled successfully
    :param data: requested data
    :return: a dictionary object, like {'success': success, 'data': data}
    """
    return {'success': success, 'data': data}


def success_api_response(data) -> dict:
    """
    wrap a success response dict obj
    :param data: requested data
    :return: an api response dictionary
    """
    return _api_response(True, data)


def failed_api_response(code, error_msg=None) -> dict:
    """
    wrap an failed response dict obj
    :param code: error code, refers to ErrorCode, can be an integer or a str (error name)
    :param error_msg: external error information
    :return: an api response dictionary
    """
    if isinstance(code, str):
        code = ErrorCode[code]
    if isinstance(code, int):
        code = ErrorCode(code)
    assert isinstance(code, ErrorCode)
    assert isinstance(code.value, int)

    if code.value < 1000:
        # using simple http status code is deprecated
        warnings.warn("using simple http code {} is deprecated".format(code.name))
        code = ErrorCode(code.value * 100)  # set to new style error code

    assert code.value >= 10000

    if error_msg is None:
        error_msg = str(code)
    else:
        error_msg = str(code) + ': ' + error_msg

    status_code = code.value // 100
    detailed_code = code.value
    return _api_response(
        success=False,
        data={
            'code': status_code,
            'detailed_error_code': detailed_code,
            'error_msg': error_msg
        })


def response_wrapper(func):
    """
    decorate a given api-function, parse its return value from a dict to a HttpResponse
    :param func: a api-function
    :return: wrapped function
    """
    def _inner(*args, **kwargs):
        _response = func(*args, **kwargs)
        if isinstance(_response, dict):
            if _response['success']:
                _response = JsonResponse(_response['data'])
            else:
                status_code = _response.get("data").get("code")
                _response = JsonResponse(_response['data'])
                _response.status_code = status_code
        return _response

    return _inner
