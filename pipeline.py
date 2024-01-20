from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def my_etl_job():
    pass

dag = DAG('my_etl_pipeline', start_date=datetime(2021, 1, 1))

task = PythonOperator(
    task_id='run_etl',
    python_callable=my_etl_job,
    dag=dag,
)
