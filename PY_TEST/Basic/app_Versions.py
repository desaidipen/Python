import os
sep = {"h": "-", "v": "|"}

def find_k8s_version(context, namespace):
  command = "kubectl get pods --context "+context+" -n "+namespace+" -oyaml | grep -e 'image: docker.prosper.com' | sed 's|.*.com\/||g' | uniq"
  process = os.popen(command)

  helm_Data = file.read(process)
  return helm_Data.split("\n")

def find_app_version(host):
  command = "ssh "+host+" sudo docker inspect --format='{{.Config.Image}}' $(ssh "+host+" sudo docker ps | grep -v NAMES | awk '{print $NF}') | sed 's|.*/||g' | sort | uniq"
  process = os.popen(command)

  helm_Data = file.read(process)
  return helm_Data.split("\n")

def assign_Version(env, envList, version_All):
  for i in range(len(envList)-1):
    temp = envList[i].split(":")

    if (env == "qa"):
      ee = 0
    elif (env == "stage"):
      ee = 1
    else:
      ee = 2

    if (temp[0] not in version_All):
      version_All[temp[0]] = ["-8", "-8", "-8"]
    
    version_All[temp[0]][ee] = temp[1]
  return version_All

def print_table(version_All):
  keys = sorted(version_All.keys())
  max_len = len(max(keys, key=len)) + 1

  for i in range(len(keys) + 3):
    if (i == 0 or i == 2):
      c = sep["v"] + sep["h"]*(max_len+2) + sep["v"] + sep["h"]*44 + sep["v"] + sep["h"]*44 + sep["v"] + sep["h"]*44 + sep["v"]
    elif (i == 1):
      c = sep["v"] + "  APPLICATION" + " "*(max_len-11) + sep["v"] + "  QA32" + " "*(38) + sep["v"] + "  STAGE" + " "*(37) + sep["v"] + "  UAT" + " "*(39) + sep["v"]
    else:
      c = sep["v"] + "  " + keys[i-3] + " "*(max_len - len(keys[i-3])) + sep["v"] + "  " + version_All[keys[i-3]][0] + " "*(42-len(version_All[keys[i-3]][0])) + sep["v"] + "  " + version_All[keys[i-3]][1] + " "*(42-len(version_All[keys[i-3]][1])) + sep["v"] + "  " + version_All[keys[i-3]][2] + " "*(42-len(version_All[keys[i-3]][2])) + sep["v"]
      
    print(c)

  print (sep["v"] + sep["h"]*(max_len+2) + sep["v"] + sep["h"]*44 + sep["v"] + sep["h"]*44 + sep["v"] + sep["h"]*44 + sep["v"])


version_All = {}
version_All = assign_Version("qa", find_k8s_version("web-qa", "qa32"), version_All)
version_All = assign_Version("stage", find_k8s_version("web-stage", "stage"), version_All)
version_All = assign_Version("uat", find_k8s_version("web-uat", "uat"), version_All)
print_table(version_All)

version_All = {}
version_All = assign_Version("qa", find_app_version("app-docker02.qa32.uc1.pspr.co"), version_All)
version_All = assign_Version("stage", find_app_version("app-docker01.stage.phd1.pspr.co"), version_All)
version_All = assign_Version("uat", find_app_version("app-docker001.prod.lvd1.pspr.co"), version_All)
print_table(version_All)