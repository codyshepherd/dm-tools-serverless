import json


def http_response(object):
    try:
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "text/plain",
                "Access-Control-Allow-Origin": "*",
            },
            "body": json.dumps(object),
        }
    except Exception:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
            },
            "body": "It's not you, it's us. :(",
        }
