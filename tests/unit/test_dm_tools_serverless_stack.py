import aws_cdk as core
import aws_cdk.assertions as assertions

from dm_tools_serverless.dm_tools_serverless_stack import DmToolsServerlessStack

# example tests. To run these tests, uncomment this file along with the example
# resource in dm_tools_serverless/dm_tools_serverless_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DmToolsServerlessStack(app, "dm-tools-serverless")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
