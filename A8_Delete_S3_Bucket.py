#!/usr/bin/python

import boto3

s3_resource = boto3.resource('s3')

bucket_name = 'mybucket102410244'

bucket = s3_resource.Bucket(bucket_name)

# Emptying S3 Bucket
bucket.objects.all().delete()

# Deleting S3 Bucket
bucket.delete()