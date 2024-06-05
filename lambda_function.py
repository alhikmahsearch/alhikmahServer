import json
import os

def lambda_handler(event, context):
    # TODO implement
    apikey = os.environ.get('OPENAI_API_KEY')
    print("printing openai api key:", apikey)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
