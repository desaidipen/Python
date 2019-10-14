import os
sep = {"h": "-", "v": "|"}

# QA32 VERSIONS *******************************************************************************************************************************************************
# process = os.popen("kubectl get pods --context web-qa -n qa32 -oyaml | grep -e 'image: docker.prosper.com' | sed 's|.*.com\/||g' | uniq")

# helm_Data = file.read(process)
# appVersion = helm_Data.split("\n")

# OR Using hard-coded versions
appVersion = ["conquer-quiz_back-end:latest", "conquer-quiz_front-end:latest", "spark:dc57233a46be7310a3bc227f33258316f491be5e", "web-account-v2:20", "web-account:0db34319ca150c19d004f3c99628fe71e73094ca", "web-borrower-dashboard:ff9f96480cb30283ae5a6fb6af88edc101632ac7", "web-borrower:12eb2abf4170b2b6411fe2db3b0e92d417131390", "web-graphql:720", "web-heloc:b4495e1073080b3e3c6d3f6ad36915f2c1865579", "web-home:e5dbb8d61c8be620757df467f913206595ea8adf", "web-hub-agentportal:137", "web-hub-assettransfer:164", "web-hub-auto-invest:338eb6c18e63ef6a74fa02ef04820a28298956c9", "web-hub-borrower:416500056e1ae5b6b77bfc2ee3687135a01452b1", "web-hub-capmarkets:17", "web-hub-dashboard:283", "web-hub-gatekeeper:84", "web-hub-heloc:212", "web-institutional:b0fe85994a4d4a61474d4a726aabbddbfab9aaa8", "web-investor-v2:81c3a3953a9e13ba0594d199b6c32aa84747f3ef", "web-investor:1f3aab182eb0a817a6e1898abbddabeae40a28f1", "web-offers:631", "web-plp:6d17f5f2dee1eb2afdfd8ae4248c143e0f899772", "web-static-assets:64", "web-static-pages:7f1f60197ed8b7663e10c36a1e81ca8a76524132", "web-verification:147"]

version_All = {}
for i in range(len(appVersion)-1):
  temp = appVersion[i].split(":")
  version_All[temp[0]] = [temp[1], "-8", "-8"]

# STAGE VERSIONS *******************************************************************************************************************************************************
# process = os.popen("kubectl get pods --context web-stage -n stage -oyaml | grep -e 'image: docker.prosper.com' | sed 's|.*.com\/||g' | uniq")

# helm_Data = file.read(process)
# appVersion = helm_Data.split("\n")

# OR Using hard-coded versions
appVersion = ["spark:dc57233a46be7310a3bc227f33258316f491be5e", "web-account-v2:20", "web-account:dc506466c6917c70bbfb650f54c35a2eb3e0f456", "web-borrower-dashboard:ff5ebf35cf385b41cddab259ba3dbf4f261908ae", "web-borrower:c763705c28e8247107891c8843e75e5a8a6813ab", "web-graphql:44050ee660cce409a35c83abb5e34f4e296e6c8d", "web-heloc:3a6d526fa101b84c414e72724a8985644a21e4c3", "web-home:e5dbb8d61c8be620757df467f913206595ea8adf", "web-hub-agentportal:137", "web-hub-assettransfer:164", "web-hub-borrower:25138fa01a0cec26db83216271d3348766cc6272", "web-hub-capmarkets:17", "web-hub-dashboard:283", "web-hub-gatekeeper:84", "web-hub-heloc:212", "web-institutional:3410d19edf0f0f311d7e3c9cfcaa4e79a50f813d", "web-investor-v2:3148707fbd375a5ed1cdda447c5af2b51e961bd3", "web-investor:1f3aab182eb0a817a6e1898abbddabeae40a28f1", "web-offers:631", "web-partner:dd19224cb1c4608c2f27dddc9d2051869d0e04a4", "web-plp:b897824a3469522e68593ef96bd43fab5f46fbfc", "web-static-assets:64", "web-static-pages:fe8cd4d731c3f215a0412c9bd0bc0804bbe91e53", "web-verification:147"]

for i in range(len(appVersion)-1):
  temp = appVersion[i].split(":")
  if (version_All.has_key(temp[0])):
    version_All[temp[0]][1] = temp[1]
  else:
    version_All[temp[0]] = ["-8", temp[1], "-8"]

# UAT VERSIONS *******************************************************************************************************************************************************
# process = os.popen("kubectl get pods --context web-uat -n uat -oyaml | grep -e 'image: docker.prosper.com' | sed 's|.*.com\/||g' | uniq")

# helm_Data = file.read(process)
# appVersion = helm_Data.split("\n")

# OR Using hard-coded versions
appVersion = ["spark:6077251c102f0e85224a14f354f3b1d6b57147e0", "web-account-v2:20", "web-account:a8ea2b7279bba077dafbf66414d3c73b565c8819", "web-borrower-dashboard:5f8b596d1bf38270e022efa46d0ec7b38ddba6e5", "web-borrower:a0c8ea1601410f5e6a121f7acd9965fbe5c99acc", "web-graphql:713", "web-heloc:9830f15772927721fd809a140ef0a7925e85a8f6", "web-home:e5dbb8d61c8be620757df467f913206595ea8adf", "web-hub-agentportal:136", "web-hub-assettransfer:164", "web-hub-capmarkets:16", "web-hub-dashboard:279", "web-hub-gatekeeper:83", "web-hub-heloc:203", "web-institutional:64d02d818591caeb9b370ea89cac5a6681d72973", "web-investor-v2:3148707fbd375a5ed1cdda447c5af2b51e961bd3", "web-investor:7de1fe5c8bec9c73983f6f6d3651f1185a9b716b", "web-offers:607", "web-partner:dd19224cb1c4608c2f27dddc9d2051869d0e04a4", "web-plp:b897824a3469522e68593ef96bd43fab5f46fbfc", "web-static-assets:64", "web-static-pages:290", "web-verification:786b7fe09daa5d2c2c1027550c912a499d378806"]

for i in range(len(appVersion)-1):
  temp = appVersion[i].split(":")
  if (version_All.has_key(temp[0])):
    version_All[temp[0]][2] = temp[1]
  else:
    version_All[temp[0]] = ["-8", "-8", temp[1]]

# PRINT TABLE *******************************************************************************************************************************************************
keys = sorted(version_All.keys())
max_len = len(max(keys, key=len)) + 1

for i in range(len(keys) + 2):
  c = ""
  j = i - 2
  if (i == 1):
    c = sep["v"] + "  APPLICATION" + " "*(max_len-11) + sep["v"] + "  QA32" + " "*(38) + sep["v"] + "  STAGE" + " "*(37) + sep["v"] + "  UAT" + " "*(39) + sep["v"]
    print(c)
  elif (i > 1):
    c = sep["v"] + "  " + keys[j] + " "*(max_len - len(keys[j])) + sep["v"] + "  " + version_All[keys[j]][0] + " "*(42-len(version_All[keys[j]][0])) + sep["v"] + "  " + version_All[keys[j]][1] + " "*(42-len(version_All[keys[j]][1])) + sep["v"] + "  " + version_All[keys[j]][2] + " "*(42-len(version_All[keys[j]][2])) + sep["v"]
    print(c)
  
  print (sep["v"] + sep["h"]*(max_len+2) + sep["v"] + sep["h"]*44 + sep["v"] + sep["h"]*44 + sep["v"] + sep["h"]*44 + sep["v"])

print ("\n\n\n ********** DIFFERENT TABLE FORMATTING ********** \n\n\n")

for i in range(len(keys) + 3):
  if (i == 0 or i == 2):
    c = sep["v"] + sep["h"]*(max_len+2) + sep["v"] + sep["h"]*44 + sep["v"] + sep["h"]*44 + sep["v"] + sep["h"]*44 + sep["v"]
  elif (i == 1):
    c = sep["v"] + "  APPLICATION" + " "*(max_len-11) + sep["v"] + "  QA32" + " "*(38) + sep["v"] + "  STAGE" + " "*(37) + sep["v"] + "  UAT" + " "*(39) + sep["v"]
  else:
    c = sep["v"] + "  " + keys[i-3] + " "*(max_len - len(keys[i-3])) + sep["v"] + "  " + version_All[keys[i-3]][0] + " "*(42-len(version_All[keys[i-3]][0])) + sep["v"] + "  " + version_All[keys[i-3]][1] + " "*(42-len(version_All[keys[i-3]][1])) + sep["v"] + "  " + version_All[keys[i-3]][2] + " "*(42-len(version_All[keys[i-3]][2])) + sep["v"]
    
  print(c)

print (sep["v"] + sep["h"]*(max_len+2) + sep["v"] + sep["h"]*44 + sep["v"] + sep["h"]*44 + sep["v"] + sep["h"]*44 + sep["v"])