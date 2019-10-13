import os
sep = {"h": "-", "v": "|"}
# header = "APPLICATION"

# process = os.popen("helm ls --namespace=qa32 --kube-context web-qa | grep -v NAME | awk '{print $1, $10}' | sed 's/qa32-//g' | sort") # >> Separated by space
process = os.popen("kubectl get pods --context web-qa -n qa32 -oyaml | grep -e 'image: docker.prosper.com' | sed 's|.*.com\/||g' | sort | uniq") # >> Separated by :

helm_Data = file.read(process)
appVersion = helm_Data.split("\n")

version_All = {}
for i in range(len(appVersion)-1):
  temp = appVersion[i].split(":")
  version_All[temp[0]] = [temp[1], "-8", "-8"]

process = os.popen("kubectl get pods --context web-stage -n stage -oyaml | grep -e 'image: docker.prosper.com' | sed 's|.*.com\/||g' | sort | uniq") # >> Separated by :

helm_Data = file.read(process)
appVersion = helm_Data.split("\n")

for i in range(len(appVersion)-1):
  temp = appVersion[i].split(":")
  if (version_All.has_key(temp[0])):
    version_All[temp[0]][1] = temp[1]
  else:
    version_All[temp[0]] = ["-8", temp[1], "-8"]


process = os.popen("kubectl get pods --context web-uat -n uat -oyaml | grep -e 'image: docker.prosper.com' | sed 's|.*.com\/||g' | sort | uniq") # >> Separated by :

helm_Data = file.read(process)
appVersion = helm_Data.split("\n")

for i in range(len(appVersion)-1):
  temp = appVersion[i].split(":")
  if (version_All.has_key(temp[0])):
    version_All[temp[0]][2] = temp[1]
  else:
    version_All[temp[0]] = ["-8", "-8", temp[1]]


keys = version_All.keys()

for i in range(len(keys) + 3):
  if (i == 0 or i == 2):
    c = sep["v"] + sep["h"]*32 + sep["v"] + sep["h"]*44 + sep["v"] + sep["h"]*44 + sep["v"] + sep["h"]*44 + sep["v"]
  elif (i == 1):
    c = sep["v"] + "  APPLICATION" + " "*(19) + sep["v"] + "  QA32" + " "*(38) + sep["v"] + "  STAGE" + " "*(37) + sep["v"] + "  UAT" + " "*(39) + sep["v"]
  else:
    c = sep["v"] + "  " + keys[i-3] + " "*(30 - len(keys[i-3])) + sep["v"] + "  " + version_All[keys[i-3]][0] + " "*(42-len(version_All[keys[i-3]][0])) + sep["v"] + "  " + version_All[keys[i-3]][1] + " "*(42-len(version_All[keys[i-3]][1])) + sep["v"] + "  " + version_All[keys[i-3]][2] + " "*(42-len(version_All[keys[i-3]][2])) + sep["v"]
    
  print(c)

print (sep["v"] + sep["h"]*32 + sep["v"] + sep["h"]*44 + sep["v"] + sep["h"]*44 + sep["v"] + sep["h"]*44 + sep["v"])