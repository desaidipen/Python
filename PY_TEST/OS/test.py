import os
import random

for i in range (10):
    rl = random.randint(1, 25)
    shell_command = "aws sqs send-message --region us-east-1 --queue-url https://sqs.us-east-1.amazonaws.com/781641733284/dd-one-queue --message-body {}".format(rl)
    msg_id = os.popen(shell_command)
    print('Random No: {0} --- Msg ID: {1}'.format(shell_command, msg_id.read()))