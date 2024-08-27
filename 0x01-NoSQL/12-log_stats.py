#!/usr/bin/env python3
'''Provides stats about Nginx logs stored in MongoDB.'''
from pymongo import MongoClient

def print_nginx_request_logs(nginx_collection):
    '''Prints stats about Nginx request logs.'''
    # Count total number of logs
    total_logs = nginx_collection.count_documents({})
    print(f'{total_logs} logs')

    # Count logs for each HTTP method
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        count = nginx_collection.count_documents({'method': method})
        print(f'\tmethod {method}: {count}')

    # Count status check logs
    status_check_count = nginx_collection.count_documents({
        'method': 'GET', 'path': '/status'
    })
    print(f'{status_check_count} status check')

def run():
    '''Provides some stats about Nginx logs stored in MongoDB.'''
    # Connect to MongoDB and select the logs.nginx collection
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    print_nginx_request_logs(nginx_collection)

if __name__ == '__main__':
    run()
