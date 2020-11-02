import os
import random
import time

err_no = random.randint(1, 25)

for i in range (40):
    rl = random.randint(1, 25)
    if rl == err_no:
        rl = str(rl) + "_error"
    shell_command = "aws sqs send-message --region us-east-1 --queue-url https://sqs.us-east-1.amazonaws.com/781641733284/dd-one-queue --message-body {}".format(rl)
    msg_id = os.popen(shell_command)
    print('Random No: {0} --- Msg ID: {1}'.format(shell_command, msg_id.read()))
    time.sleep(random.randint(1, 15))
