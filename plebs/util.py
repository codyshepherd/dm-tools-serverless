import json


def http_response(object):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain"},
        "body": json.dumps(object),
    }
