import os
import random
import time
import json

err_no = random.randint(1, 25)

for i in range (40):
    rl = random.randint(1, 25)
    if rl == err_no:
        rl = str(rl) + "_error"
    
    # Running AWS SQS Command
    shell_command = "aws sqs send-message --region us-east-1 --queue-url https://sqs.us-east-1.amazonaws.com/781641733284/dd-one-queue --message-body {}".format(rl)
    msg_id = os.popen(shell_command)
    print("\nSQS >> Random No: {0} --- Msg ID: {1}\n\n".format(shell_command, msg_id.read()))

    # Running AWS API GW Command
    data_dict = {"Records": [{"messageId": "aws_sqs_api_python", "body": str(rl) }]}
    data_str = json.dumps(data_dict)
    shell_command = 'curl --location --request POST "https://xvci46fg84.execute-api.us-east-1.amazonaws.com/stage/" --header "Content-Type: application/json" --data-raw \'{}\''.format(data_str)
    msg_id = os.popen(shell_command)
    print("\nAPI GW >> Random No: {0} --- Msg ID: {1}\n\n".format(shell_command, msg_id.read()))

    time.sleep(random.randint(3, 5))
