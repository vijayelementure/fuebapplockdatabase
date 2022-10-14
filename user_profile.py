import boto3
import os
import uuid
from dotenv import load_dotenv
from datetime import datetime
import botocore.exceptions

load_dotenv()

def user_picture():
    try:
        dynamodb = boto3.resource('dynamodb',region_name = os.getenv('REGION_NAME'),aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
        table = dynamodb.Table('user_profile') 

        s3 = boto3.client('s3',region_name=os.getenv('REGION_NAME'),aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

        s3object = s3.generate_presigned_post('lockappuserprofile','god.png')

        objectkey = s3object.get('fields').get('key')

        region = s3.get_bucket_location(Bucket='lockappuserprofile')['LocationConstraint']

        data1 = "https://"
        data2 = "lockappuserprofile"
        data3 = ".s3."
        data4 = region
        data5 = ".amazonaws.com/"
        data6 = objectkey

        profileimage = data1+data2+data3+data4+data5+data6

        table.put_item(Item={
                      "email":"vijaybhaskarmyv@gmail.com",
                      "profile photo":profileimage,
                      "uuid":0,
                      "Created Date": str(datetime.now())
                      })
    except botocore.exceptions.ClientError as err:
        print(err)


if __name__=='__main__':
    user_picture()





















