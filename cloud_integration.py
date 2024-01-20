import boto3

session = boto3.session.Session()

s3 = session.client('s3')

# List all buckets
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')
