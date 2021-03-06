#! /usr/bin/env python3

import os
import requests
import json

# put the IP_ADDRESS here
IP_ADDRESS = '127.0.0.1'

def get_temp_location_for_code():
    temp_location = __file__
    return os.path.split(temp_location)[0]

home = get_temp_location_for_code()
feedback_path = "{}/data/feedback/".format(home)
post_data_keys = ['title', 'name', 'date', 'feedback']
corpweb_feedback_url = 'http://{}/feedback/'.format(IP_ADDRESS)

def process_feedback(filename):

    post_data = {}
    with open(filename, 'r') as fb:
        lines = fb.readlines()

        for k, line in zip(post_data_keys, lines):
            post_data.update({k: line})

    response = requests.post(corpweb_feedback_url, json=post_data)
    response.raise_for_status()

def process_feedbacks():
    
    for feedback in os.listdir(feedback_path):
        process_feedback(os.path.join(feedback_path, feedback))

def main():
    
    print('Posting feedbacks from {} folder'.format(feedback_path))
    print('Posting feedbacks to {}'.format(corpweb_feedback_url))
    
    process_feedbacks()

    print('Done... Exiting')

if __name__ == '__main__':
    main()
