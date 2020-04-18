#!/usr/bin/env python2

# Prints application versions across all environments
# Command: $ python ..../version.py {type} {application}
# E.g. 
#   $ python ./version.py web web-graphql
#   $ python ./version.py web all
#   $ python ./version.py app svc-heloc-application
#   $ python ./version.py app all
#   $ python ./version.py app gds

import os
import sys
import argparse

sep = {"h": "-", "v": "|"}

class version(object):
  def __init__(self):
    self.version_All = {}
    self.version_Length = []
    parser = argparse.ArgumentParser()
    parser.add_argument("type")
    args=parser.parse_args(sys.argv[1:2])

    if (args.type == 'all'):
      print ("K8S-WEB")
      self.web()
      print ("\nK8S-APP")
      self.app()
    else:
      getattr(self, args.type)()

  # K8S VERSIONS *******************************************************************************************************************************************************
  def find_k8s_version(self, context, namespace):
    self.version_All["APPLICATION"].append("{}/{}".format(context, namespace))
    self.version_Length.append(len(" {}/{} ".format(context, namespace)))

    parser = argparse.ArgumentParser()
    parser.add_argument('app')
    args = parser.parse_args(sys.argv[2:])

    grep_value = ""
    if (args.app != "all"):
      grep_value = " | grep " + args.app

    # command = "kubectl get pods --context "+context+" -n "+namespace+" -oyaml | grep -e 'image: docker.prosper.com' | sed 's|.*.com\/||g' | uniq" + grep_value
    command = "kubectl get pods --context "+context+" -n "+namespace+" -o jsonpath='{.items[*].spec.containers[*].image}' | tr -s '[[:space:]]' '\n' | sed 's/docker.prosper.com\///g' | sort | uniq" + grep_value
    # command = "kubectl get pods --context "+context+" -n "+namespace+" -o jsonpath='{.items[*].status.containerStatuses[*].image}' | sed 's/docker.prosper.com\///g' | tr -s '[[:space:]]' '\n'  | sort | uniq" + grep_value
    process = os.popen(command)

    helm_Data = file.read(process)
    return helm_Data.split("\n")

  # PARSE VERSIONS *******************************************************************************************************************************************************
  def assign_Version(self, appVersions):
    ee = len(self.version_All["APPLICATION"]) - 1

    for i in range(len(appVersions)-1):
      temp = appVersions[i].split(":")
      
      if (temp[0] not in self.version_All):
        self.version_All[temp[0]] = ["-X-", "-X-", "-X-", "-X-", "-X-"]
      try:
        self.version_All[temp[0]][ee] = temp[1]
        if (len(temp[1]) >= self.version_Length[ee]):
          self.version_Length[ee] = len(temp[1]) + 1
      except:
        NotImplemented

  # PRINT TABLE *******************************************************************************************************************************************************
  def print_table(self):
    keys = sorted(self.version_All.keys())
    max_len = len(max(keys, key=len)) + 1
    tc = 0    # temp_count (looping for version_All directory keys)

    envCount = len(self.version_All["APPLICATION"])

    for i in range(len(keys) + 3):
      if (i == 0 or i == 2 or (i - (len(keys) + 2)) == 0):
        c = sep["v"] + sep["h"]*(max_len+2) + sep["v"]
        for x in range(0, envCount):
          c = c + sep["h"]*(self.version_Length[x]+2) + sep["v"]
      else:
        c = sep["v"] + "  " + keys[tc] + " "*(max_len - len(keys[tc])) + sep["v"]
        for x in range(0, envCount):
          c = c + "  " + self.version_All[keys[tc]][x] + " "*(self.version_Length[x]-len(self.version_All[keys[tc]][x])) + sep["v"]
        tc += 1
    
      print(c)
  
  # RESET VERSIONS *******************************************************************************************************************************************************
  def reset_All(self):
    self.version_All = {"APPLICATION": []}
    self.version_Length = []

  # def function_call(self, envList):
  #   self.reset_All()
  #   for key in envList.keys():
  #     self.assign_Version(self.find_k8s_version(key, envList[key]))
  #   self.print_table()

  # def web(self):
  #   envList = {"web-qa": "qa32", "np": "stage", "web-uat": "uat", "web-prod": "prod"}
  #   self.function_call(envList)

  # def app(self):
  #   envList = {"app-qa": "qa32", "app-stage": "stage", "app-uat": "uat", "app-prod": "prod"}
  #   self.function_call(envList)

  def web(self):
    self.reset_All()
    self.assign_Version(self.find_k8s_version("web-qa", "qa32"))
    # self.assign_Version(self.find_k8s_version("web-stage", "stage"))
    self.assign_Version(self.find_k8s_version("np", "stage"))
    self.assign_Version(self.find_k8s_version("web-uat", "uat"))
    self.assign_Version(self.find_k8s_version("web-prod", "prod"))
    self.print_table()

  def app(self):
    self.reset_All()
    self.assign_Version(self.find_k8s_version("app-qa", "qa32"))
    self.assign_Version(self.find_k8s_version("app-stage", "stage"))
    self.assign_Version(self.find_k8s_version("app-uat", "uat"))
    self.assign_Version(self.find_k8s_version("app-prod", "prod"))
    self.print_table()

version()