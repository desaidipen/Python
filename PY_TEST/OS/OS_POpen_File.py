import os

# process = os.popen("helm ls --namespace=qa32 --kube-context web-qa | grep -v NAME | awk '{print $1, $10}' | sed 's/qa32-//g' | sort") # >> Separated by space
process = os.popen("kubectl get pods --context web-qa -n qa32 -oyaml | grep -e 'image: docker.prosper.com' | sed 's|.*.com\/||g' | sort | uniq") # >> Separated by :
helmLS = file.read(process)

app_Ver = helmLS.split("\n")
for i in range(len(app_Ver)-1):
  temp = app_Ver[i].split(":") # Check command to select split types " " or ":"
  print ("{}-----{}".format(temp[0], temp[1]))