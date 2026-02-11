import logging

from inngest import Inngest
from inngest.handlers.aws_lambda import inngest_lambda_handler

# Basic logging (helps CloudWatch visibility)
logging.basicConfig(level=logging.INFO)

# Create Inngest app
inngest = Inngest(app_id="cdk-git-test")

# Define a test Inngest function
@inngest.create_function(
    fn_id="hello-world",
    trigger={"event": "demo.hello"},
)
def hello_world(ctx):
    ctx.step("log", lambda: logging.info("from lambdaaa!!!!!"))
    return {"ok": True}

# IMPORTANT:
# This is the AWS Lambda entrypoint used by CDK (handler = app.handler)
handler = inngest_lambda_handler(inngest)