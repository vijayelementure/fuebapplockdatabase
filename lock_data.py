import boto3
import os
import uuid
from dotenv import load_dotenv
from datetime import datetime
import botocore.exceptions


load_dotenv()


def lock_data():
    try:
        dynamodb = boto3.resource('dynamodb',region_name = os.getenv('REGION_NAME'),aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
        table = dynamodb.Table('lock_data')   

        table.put_item(Item={
            "email":"vijaybhaskarmyv@gmail.com",
            "hubid":"",
            "lockid":"",
            "access":"",
            "parent":"",
            "uuid device":"",
            "device access id":"",
            "account created": str(datetime.now())
                })
    except botocore.exceptions.ClientError as err:
        print(err)
    
if __name__=='__main__':
    lock_data()