# import random
# import time

# tot = 0
# for _ in range(10):
#     y = random.randint(1, 9)
#     time.sleep(1)
#     print (y)
#     tot = tot + y

# print(">> {}".format(tot))


import os
import random
import time

for i in range (40):
    shell_command = 'curl -I http://k8s-nginxapp-nginxkub-179f17d859-96884885.us-east-1.elb.amazonaws.com'
    msg_id = os.popen(shell_command)
    print('Tried: {}'.format(i))
    time.sleep(random.randint(3, 5))
