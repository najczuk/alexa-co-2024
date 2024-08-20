import logging
import os
import boto3
from botocore.exceptions import ClientError
import random
import json


def create_presigned_url(object_name):
    """Generate a presigned URL to share an S3 object with a capped expiration of 60 seconds

    :param object_name: string
    :return: Presigned URL as string. If error, returns None.
    """
    s3_client = boto3.client('s3',
                             region_name=os.environ.get('S3_PERSISTENCE_REGION'),
                             config=boto3.session.Config(signature_version='s3v4',s3={'addressing_style': 'path'}))
    try:
        bucket_name = os.environ.get('S3_PERSISTENCE_BUCKET')
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=60*1)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response

questions:dict = None


def load_questions() -> list:
    global questions
    if not questions:
        # Open the JSON file
        with open('flashcards.json', 'r') as file:
            # Load the JSON data into a dictionary
            questions = json.load(file)
    
    return questions

def draw_question_entry() -> dict:
    random_question = random.choice(load_questions())
    
    return random_question


def compare_slots(slots, correct_answer):
    """Compare slot value to the value provided."""
    for _, slot in slots.items():
        if slot.value is not None:
            return slot.value.lower() == correct_answer.lower()
    else:
        return False