import boto3
import uuid


class DynamoModule:

    def __init__(self):
        self.dynamo_client = boto3.client('dynamodb', region_name='us-east-1')

    def create_item(self, username, epoch_date, file_type, file_size):
        item_id = str(uuid.uuid1())
        self.dynamo_client.put_item(
            TableName='CerebroOutputs',
            Item={
                'item_id': {
                    'S': item_id
                },
                'username': {
                    'S': username
                },
                'created': {
                    'S': epoch_date
                },
                'file_type': {
                    'S': file_type
                },
                'file_size': {
                    'N': file_size
                },
                'decoded_output': {
                    'S': ""
                }
            }
        )
        return item_id

    def add_output(self, item_id, username, decoded_output):
        response = self.dynamo_client.update_item(
            TableName='CerebroOutputs',
            Key={
                'item_id': {
                    'S': item_id
                },
                'username': {
                    'S': username
                }
            },
            UpdateExpression='SET decoded_output = :decoded_output',
            ExpressionAttributeValues= {
                ':decoded_output': {
                    'S': decoded_output
                }
             }
        )
        return response
