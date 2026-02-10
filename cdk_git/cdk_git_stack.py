from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
)
from constructs import Construct


class CdkGitStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        fn = lambda_.Function(
            self,
            "TestPythonLambda",
            runtime=lambda_.Runtime.PYTHON_3_11,
            handler="app.handler",
            code=lambda_.Code.from_asset("lambda"),
        )

        # 👇 THIS IS THE IMPORTANT PART FOR INNGEST
        fn.add_function_url(
            auth_type=lambda_.FunctionUrlAuthType.NONE
        )