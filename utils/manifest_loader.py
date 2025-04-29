import yaml

def load_manifest(manifest_path):
    with open(manifest_path, 'r') as file:
        scripts = yaml.safe_load(file)
    return scripts
