import  boto3



client=boto3.client("s3")
result=client.create_bucket(Bucket="mangu")

print(result)


