from aws_cdk import Stack
from aws_cdk.aws_lambda_python_alpha import PythonFunction
from aws_cdk.aws_lambda import Runtime, FunctionUrlAuthType
from constructs import Construct


class CdkGitStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        fn = PythonFunction(
            self,
            "TestPythonLambda",
            entry="lambda",
            index="app.py",
            handler="handler",
            runtime=Runtime.PYTHON_3_11,
        )

        fn.add_function_url(
            auth_type=FunctionUrlAuthType.NONE
        )