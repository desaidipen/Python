import os
import sys
import yaml
import json
import argparse

rPath = "/Users/ddesai/Documents/k8s/kubernetes-charts/"

# Pass two Arguments: $ python ./YAML_FileRead.py -h web-heloc stage (#2: Chart Name -- #3: Environment)
parser = argparse.ArgumentParser(description='Read HELM Charat and Values Tag for an Environment')
parser.add_argument('chart', help='Chart Name')
parser.add_argument('env', help='Env Name')

# Parse Arguments
args = parser.parse_args(sys.argv[2:])
print ("Chart: {} --- Env: {}".format(args.chart, args.env))

# Read File (File context is in YAML format)
cValue = open(rPath + args.chart + "/" + "values_" + args.env + ".yaml", "r")
fRead = cValue.read()
cValue.close()

# Load YAML File and Get IMAGE.TAG
val = yaml.safe_load(fRead)
print ("Image Tag (YAML): {}".format(val["image"]["tag"]))

# Convert YAML into JSON Data and Get IMAGE.TAG
jRead = json.dumps(val)
val2 = json.loads(jRead)
print ("Image Tag (JSON): {}".format(val2["image"]["tag"]))