from utils.runner import run_scripts_in_order

def deploy_layer(layer_name):
    manifest_path = f"manifests/{layer_name}_order.yml"
    print(f"🚀 Deploying {layer_name.capitalize()} Layer...")
    run_scripts_in_order(manifest_path)
    print(f"🎯 Finished deploying {layer_name.capitalize()} Layer.\n")
