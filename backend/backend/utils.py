from dotenv import load_dotenv

import os
import boto3

load_dotenv('.env')

def get_env_variable(name):
    """Fetch environment variables locally or from AWS Parameter Store based on the environment."""

    # Detect environment: Default to 'LOCAL' if not set
    ENV = os.getenv("APP_ENV").upper()

    # If running locally, fetch from system environment
    if ENV == "LOCAL":
        return os.getenv(name)

    # If running in 'DEV' or 'PROD', fetch from AWS Parameter Store
    try:
        ssm = boto3.client("ssm", region_name="us-east-1")  # Adjust region
        print('SSM: ', ssm)
        response = ssm.get_parameter(
            #TODO: make the /dev/ dynamic
            Name=f"/solus_plus/dev/{name}", WithDecryption=True
        )
        print("REPONSEE: ", response)
        return response["Parameter"]["Value"]
    except Exception as e:
        print(f"Error fetching {name} from AWS: {e}")
        return None  # Return None if the parameter is not found
