import boto3

AWS_REGION = "sa-east-1"
access_key_id = 'ASIA47CR3NANS6TBDDHD'
secret_access_key = 'i8kNAiehwSC3GsCJTXty+qauvcZc62fTnCtz9fs9'

client = boto3.client("s3",
                      verify=False,
                      region_name=AWS_REGION,
                      aws_access_key_id=access_key_id,
                      aws_secret_access_key=secret_access_key
                      )
response = client.list_buckets(Bucket='bucket-mastercard-data-load-orchestration-dev')
print("Listing Amazon S3 Buckets:")
for bucket in response['Buckets']:
    print(f"-- {bucket['Name']}")

