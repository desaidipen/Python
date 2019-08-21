import yaml

# Define Path and Environment Variables
envs = ["qa32", "stage", "uat", "prod"]

# Read Actual Version Data
with file("YAML_TagInput.yaml", "r") as fr:
  val = yaml.safe_load(fr.read())

# Read new formatted yaml file
with file("YAML_TagOutput.yaml", "r") as fr2:
  val2 = yaml.safe_load(fr2.read())

# Match keys (app-name) and update versions
for eenv in envs:
  for key in val[eenv]:
    if key in val2:
      val2[key]["version"][eenv] = val[eenv][key]

# Write back information
with file("YAML_TagOutput.yaml", "w") as fw:
  yaml.dump(val2, fw, allow_unicode=True, default_flow_style=False)