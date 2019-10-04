#!/usr/bin/python

import boto3

filename = 'index.html'
bucket_name = 'mybucket102410244'

s3 = boto3.client('s3')

# Creating S3 Bucket
s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})

# Pushing file to above Created Bucket
s3.upload_file(filename, bucket_name, filename)