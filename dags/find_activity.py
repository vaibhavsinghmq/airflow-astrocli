from airflow.decorators import dag, task
from pendulum import datetime
from airflow.models import Variable

import requests

API="https://www.boredapi.com/api/activity"


@dag(
    start_date=datetime(2023,1,1),
    schedule="@daily",
    tags=["learn"],
    catchup=False
)

def find_activity():
    
    @task
    def get_acitivity():
        req = requests.get(API,timeout=10)
        return req.json()
    
    @task
    def write_to_file(response):
        filepath = Variable.get("acitivity_file")
        with open(filepath,"a") as f:
            f.write(f"Today you will : {response['activity']}\r\n")
        return filepath
    
    @task
    def read_file(filepath):
        with open(filepath,"r") as f:
            print(f.read())

    response = get_acitivity()
    filepath = write_to_file(response)
    read_file(filepath)


find_activity()