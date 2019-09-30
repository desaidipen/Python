import os
process = os.popen("helm ls --kube-context=web-uat --namespace=uat")
b = file.read(process)

b1 = b.split("\n")[1:]
for i in range(len(b1)-1):
  c = b1[i].split("\t")
  print ("{}-----{}-----{}".format(c[0].strip(" "), c[4].strip(" ").split("-")[-1], c[5]))