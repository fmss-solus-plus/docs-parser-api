from dotenv import load_dotenv

import os
import boto3

load_dotenv('.env')

def get_env_variable(name):
    """Fetch environment variables locally or from AWS Parameter Store based on the environment."""
    # If running in 'DEV' or 'PROD', fetch from AWS Parameter Store
    try:
        ssm = boto3.client("ssm", region_name="ap-southeast-2")  # Adjust region
        response = ssm.get_parameter(
            #TODO: make the /dev/ dynamic
            Name=f"/solus_plus/dev/{name}", WithDecryption=True
        )
        return response["Parameter"]["Value"]
    except Exception as e:
        print(f"Error fetching {name} from AWS: {e}")
        return None  # Return None if the parameter is not found

def check_env():
    # Detect environment: Default to 'LOCAL' if not set
    env = os.getenv("APP_ENV", 'LOCAL').upper() 
    print(f"Running in {env} environments")	

    if env == 'LOCAL':
        return 'backend.settings'
    elif env == 'DEV_AWS':
        return 'backend.aws_deployment'
    elif env == 'DEV_AZURE':
        return 'backend.azure_deployment'