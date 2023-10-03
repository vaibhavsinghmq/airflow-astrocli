from airflow.decorators import dag,task
from pendulum import datetime

from airflow.operators.bash import BashOperator

@dag(
    start_date=datetime(2023,1,1),
    schedule='@daily',
    tags=['bash'],
    catchup=False
)


def start_bash_activity():
    @task(task_id='printbash_date')
    def print_date():
        # Task using BashOperator
        bash = BashOperator(
            task_id='print_date',
            bash_command='date',
        )
        bash.execute({})

    print_date()

start_bash_activity()