from utils.deploy import deploy_layer

def main():
    print("Starting full deployment (Bronze -> Silver -> Gold)...\n")
    
    deploy_layer("bronze")
    deploy_layer("silver")
    deploy_layer("gold")

    print("🎉 All layers deployed successfully.")

if __name__ == "__main__":
    main()
