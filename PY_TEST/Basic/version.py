#!/usr/bin/env python2
import os
import sys
import argparse

sep = {"h": "-", "v": "|"}

class version(object):
  def __init__(self):
    self.version_All = {}
    parser = argparse.ArgumentParser(description="definition", usage="usage")
    parser.add_argument("ver", help="Available sum")
    args=parser.parse_args(sys.argv[1:2])
    getattr(self, args.ver)()

  # K8S VERSIONS *******************************************************************************************************************************************************
  def find_k8s_version(self, context, namespace):
    # command = "kubectl get pods --context "+context+" -n "+namespace+" -oyaml | grep -e 'image: docker.prosper.com' | sed 's|.*.com\/||g' | uniq"
    command = "kubectl get pods --context "+context+" -n "+namespace+" -o jsonpath='{.items[*].spec.containers[*].image}' | tr -s '[[:space:]]' '\n' | sed 's/docker.prosper.com\///g' | sort | uniq"
    # command = "kubectl get pods --context "+context+" -n "+namespace+" -o jsonpath='{.items[*].status.containerStatuses[*].image}' | sed 's/docker.prosper.com\///g' | tr -s '[[:space:]]' '\n'  | sort | uniq"
    process = os.popen(command)

    helm_Data = file.read(process)
    return helm_Data.split("\n")

  # DOCKER APP VERSIONS *******************************************************************************************************************************************************
  def find_app_version(self, host):
    command = "ssh "+host+" sudo docker inspect --format='{{.Config.Image}}' $(ssh "+host+" sudo docker ps | grep -v NAMES | awk '{print $NF}') | sed 's|.*/||g' | uniq"
    process = os.popen(command)

    helm_Data = file.read(process)
    return helm_Data.split("\n")

  # PARSE VERSIONS *******************************************************************************************************************************************************
  def assign_Version(self, env, envList):
    for i in range(len(envList)-1):
      temp = envList[i].split(":")

      if (env == "qa"):
        ee = 0
      elif (env == "stage"):
        ee = 1
      elif (env == "uat"):
        ee = 2
      else:
        ee = 3

      if (temp[0] not in self.version_All):
        self.version_All[temp[0]] = ["-X-", "-X-", "-X-", "-X-"]
      try:
        self.version_All[temp[0]][ee] = temp[1]
      except:
        NotImplemented

  # PRINT TABLE *******************************************************************************************************************************************************
  def print_table(self):
    keys = sorted(self.version_All.keys())
    max_len = len(max(keys, key=len)) + 1

    for i in range(len(keys) + 3):
      if (i == 0 or i == 2 or (i - (len(keys) + 2)) == 0):
        c = sep["v"] + sep["h"]*(max_len+2) + sep["v"] + (sep["h"]*44 + sep["v"])*4
      elif (i == 1):
        c = sep["v"] + "  APPLICATION" + " "*(max_len-11) + sep["v"] + "  QA32" + " "*(38) + sep["v"] + "  STAGE" + " "*(37) + sep["v"] + "  UAT" + " "*(39) + sep["v"] + "  PROD" + " "*(38) + sep["v"]
      else:
        c = sep["v"] + "  " + keys[i-3] + " "*(max_len - len(keys[i-3])) + sep["v"] + "  " + self.version_All[keys[i-3]][0] + " "*(42-len(self.version_All[keys[i-3]][0])) + sep["v"] + "  " + self.version_All[keys[i-3]][1] + " "*(42-len(self.version_All[keys[i-3]][1])) + sep["v"] + "  " + self.version_All[keys[i-3]][2] + " "*(42-len(self.version_All[keys[i-3]][2])) + sep["v"] + "  " + self.version_All[keys[i-3]][3] + " "*(42-len(self.version_All[keys[i-3]][3])) + sep["v"]
        
      print(c)

  def k8s_web(self):
    self.assign_Version("qa", self.find_k8s_version("web-qa", "qa32"))
    self.assign_Version("stage", self.find_k8s_version("web-stage", "stage"))
    self.assign_Version("uat", self.find_k8s_version("web-uat", "uat"))
    self.assign_Version("prod", self.find_k8s_version("web-prod", "prod"))
    self.print_table()

  def k8s_app(self):
    self.version_All = {}
    self.assign_Version("qa", self.find_k8s_version("app-qa", "qa32"))
    self.assign_Version("stage", self.find_k8s_version("app-stage", "stage"))
    self.assign_Version("uat", self.find_k8s_version("app-uat", "uat"))
    self.assign_Version("prod", self.find_k8s_version("app-prod", "prod"))
    self.print_table()

  def docker(self):
    self.assign_Version("qa", self.find_app_version("app-docker02.qa32.uc1.pspr.co"))
    self.assign_Version("stage", self.find_app_version("app-docker01.stage.phd1.pspr.co"))
    self.assign_Version("uat", self.find_app_version("app-docker001.prod.lvd1.pspr.co"))
    self.assign_Version("prod", self.find_app_version("app-docker001.prod.phd1.pspr.co"))
    self.print_table()

version()