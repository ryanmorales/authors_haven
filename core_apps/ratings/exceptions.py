from rest_framework.exceptions import APIException


class YouhaveAlreadyRated(APIException):
    status_code = 400
    default_detail = "Have already rated this articla."
    default_code = "bad_request"
