import os as os
import commands

# hosts = ["web-docker01.qa32.uc1.pspr.co", "web-docker001.stage.phd1.pspr.co", "web-docker001.prod.lvd1.pspr.co", "web-docker01.prod.phd1.pspr.co"]
hosts =["app-docker01.qa32.uc1.pspr.co", "app-docker01.stage.phd1.pspr.co", "app-docker001.prod.lvd1.pspr.co", "app-docker001.prod.phd1.pspr.co"]
# hosts = ["app-docker01.qa32.uc1.pspr.co", "app-docker01.stage.phd1.pspr.co"]
# hosts = ["web-docker001.stage.phd1.pspr.co", "app-docker01.stage.phd1.pspr.co"]
# hosts =["app-docker01.qa32.uc1.pspr.co", "web-docker01.qa32.uc1.pspr.co", "app-docker01.stage.phd1.pspr.co", "web-docker001.stage.phd1.pspr.co", "app-docker001.prod.lvd1.pspr.co", "web-docker001.prod.lvd1.pspr.co", "app-docker001.prod.phd1.pspr.co", "web-docker01.prod.phd1.pspr.co"]

d = {}

for i in range(len(hosts)):
  print("HOST: {0}".format(hosts[i]))
  
  b = commands.getoutput("ssh %s sudo docker inspect --format='{{.Config.Image}}' $(ssh %s sudo docker ps | grep -v NAMES | awk '{print $NF}') | sed 's|.*/||g' | uniq | sort"%(hosts[i],hosts[i]))
  ll = b.splitlines()

  print("*******")
  for l in ll:
    if (l[:4] != "Warn"):
      av = l.split(":")
      # print("APP: {0} >> VER: {1}".format(av[0],av[1]))

      if av[0] in d.keys():
        d[av[0]][i] = av[1]
      else:
        d[av[0]] = [0, 0, 0, 0]
        d[av[0]][i] = av[1]
  print("*******")

print(d)


# # Sample shell Script
# for host in $hosts
# do
#   echo "\n\n\n>>>>> $host"
# #  ssh $host 'bash -s' < /Users/ddesai/Documents/docker/docker_inspect.sh
#   ssh ${host} sudo docker inspect --format='{{.Config.Image}}' $(ssh ${host} sudo docker ps | grep -v NAMES | awk '{print $NF}') | sed 's|.*/||g' | uniq | sort
# done