import os
import json

cmd = "aws sts assume-role --role-arn arn:aws:iam::781641733284:role/dd-ec2-s3-read-only-access --role-session-name test --o json"
msg_id = os.popen(cmd)
jobj = json.loads(msg_id.read())
print (jobj)

cmd_access_key = "export AWS_ACCESS_KEY_ID={}".format(jobj["Credentials"]["AccessKeyId"])
cmd_secret_key = "export AWS_SECRET_ACCESS_KEY={}".format(jobj["Credentials"]["SecretAccessKey"])
cmd_session_token = "export AWS_SESSION_TOKEN={}".format(jobj["Credentials"]["SessionToken"])

# RUN A COMMAND TO SET THREE ENV VARS
msg_id = os.popen(cmd_access_key)
print ("1:{}".format(msg_id.read()))
msg_id = os.popen(cmd_secret_key)
print ("2:{}".format(msg_id.read()))
msg_id = os.popen(cmd_session_token)
print ("3:{}".format(msg_id.read()))

cmd = "aws sts get-caller-identity --o json"
msg_id = os.popen(cmd)
jobj = json.loads(msg_id.read())
print("Role Assumed: {}".format(jobj["Arn"].split(":")[-1]))