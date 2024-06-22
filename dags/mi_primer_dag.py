from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def my_function():
    print("Ejecutando mi función dentro del DAG")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Creamos el DAG
dag = DAG(
    'mi_dag_diario',
    default_args=default_args,
    description='Un DAG simple para la tercera entrega del curso de CODERHOUSE',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
)

# Definimos la tarea usando un PythonOperator
tarea = PythonOperator(
    task_id='ejecutar_funcion',
    python_callable=my_function,
    dag=dag,
)

tarea

globals()['dag'] = dag
