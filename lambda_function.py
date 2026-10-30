
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCount')

def lambda_handler(event, context):

    try:
        # Get visitor name from request
        body = event.get('body')

        if isinstance(body, str):
            body = json.loads(body)
        elif not isinstance(body, dict):
            body = {}

        name = body.get('name', 'Guest')

        # Increment visitor count atomically
        response = table.update_item(
            Key={'id': 'visitors'},
            UpdateExpression='ADD #count :inc',
            ExpressionAttributeNames={
                '#count': 'count'
            },
            ExpressionAttributeValues={
                ':inc': 1
            },
            ReturnValues='UPDATED_NEW'
        )

        visitor_count = int(response['Attributes']['count'])

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': f'Hello, {name}! Welcome to my website.',
                'count': visitor_count
            })
        }

    except Exception as e:
        print("Error:", str(e))

        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Internal server error'
            })
        }
