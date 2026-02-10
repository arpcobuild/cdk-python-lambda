from inngest import Inngest
from inngest.handlers.aws_lambda import inngest_lambda_handler

# Create Inngest app
inngest = Inngest(app_id="cdk-git-test")

# Define a test function
@inngest.create_function(
    fn_id="hello-world",
    trigger={"event": "demo.hello"},
)
def hello_world(ctx):
    ctx.step("log", lambda: print("From Inngest Lambda"))
    return {"ok": True}

# IMPORTANT: This is the Lambda handler now
handler = inngest_lambda_handler(inngest)