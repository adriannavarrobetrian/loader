import json
import boto3
import os

sqs = boto3.client('sqs', region_name=os.environ['eu-west-1'])

queue_url = os.environ['https://sqs.eu-west-1.amazonaws.com/646390474080/movies_to_parse']

def sendMovie(movie):
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=(json.dumps(movie)))
    return response['MessageId']

with open('movies.json') as json_file:
    data = json.load(json_file)
    for movie in data:
        print('Name: ' + movie['title'])
        message = sendMovie(movie)
        print('Message ID: ' + message)