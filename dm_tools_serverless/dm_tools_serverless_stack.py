import os

from aws_cdk import (
    aws_apigateway as apigateway,
    aws_lambda as lambda_,
    core,
)
from constructs import Construct


class DmToolsServerlessStack(core.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pockets = lambda_.Function(
            self,
            "pockets_lambda",
            code=lambda_.Code.from_asset(
                "./plebs",
                bundling=core.BundlingOptions(
                    image=lambda_.Runtime.PYTHON_3_9.bundling_image,
                    command=[
                        "bash",
                        "-c",
                        "pip install -r requirements.txt -t /asset-output && cp -au . /asset-output",
                    ],
                ),
            ),
            function_name="pockets",
            handler="pockets.pockets_handler",
            runtime=lambda_.Runtime.PYTHON_3_9,
        )

        plebs = lambda_.Function(
            self,
            "plebs_lambda",
            code=lambda_.Code.from_asset(
                "./plebs",
                bundling=core.BundlingOptions(
                    image=lambda_.Runtime.PYTHON_3_9.bundling_image,
                    command=[
                        "bash",
                        "-c",
                        "pip install -r requirements.txt -t /asset-output && cp -au . /asset-output",
                    ],
                ),
            ),
            function_name="plebs",
            handler="plebs.plebs_handler",
            runtime=lambda_.Runtime.PYTHON_3_9,
        )

        taverns = lambda_.Function(
            self,
            "taverns_lambda",
            code=lambda_.Code.from_asset(
                "./plebs",
                bundling=core.BundlingOptions(
                    image=lambda_.Runtime.PYTHON_3_9.bundling_image,
                    command=[
                        "bash",
                        "-c",
                        "pip install -r requirements.txt -t /asset-output && cp -au . /asset-output",
                    ],
                ),
            ),
            function_name="taverns",
            handler="taverns.taverns_handler",
            runtime=lambda_.Runtime.PYTHON_3_9,
        )

        api = apigateway.RestApi(self, "dm-tools-api")

        pockets_endpoint = api.root.add_resource("pockets")
        pockets_endpoint.add_method(
            "GET",
            apigateway.LambdaIntegration(
                pockets,
                allow_test_invoke=True,
            ),
            api_key_required=True,
        )

        plebs_endpoint = api.root.add_resource("plebs")
        plebs_endpoint.add_method(
            "GET",
            apigateway.LambdaIntegration(
                plebs,
                allow_test_invoke=True,
            ),
            api_key_required=True,
        )

        taverns_endpoint = api.root.add_resource("taverns")
        taverns_endpoint.add_method(
            "GET",
            apigateway.LambdaIntegration(
                taverns,
                allow_test_invoke=True,
            ),
            api_key_required=True,
        )
