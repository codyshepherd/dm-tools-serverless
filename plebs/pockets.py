from plebs import gen_items
from util import http_response


def pockets_handler(event, context):
    params = event["queryStringParameters"]
    if params is None:
        params = {}
    return http_response(_pockets(int(params.get("number", "1"))))


def _pockets(number: int):
    return gen_items(**{"num_items": number})
