from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_gcs import GCSToGCSOperator

default_args = {
    'owner': 'Thadeu Guimaraes',
    'start_date': datetime(2025, 7, 23),
    'schedule_interval': '@daily'
}

with DAG(
        dag_id = 'move_gcs_files',
        default_args =default_args,
        schedule_interval=None,
        catchup=False,
        tags =['gcs', 'meetup_cncf']
) as dag:
    
    move_files_to_bkp = GCSToGCSOperator(
        task_id='move_files_to_bkp',
        source_bucket='staging-meetup_cncf',
        source_object='*',
        destination_bucket = 'processed-files-meetup_cncf',
        destination_object='',
        move_object = True
    )

    move_files_to_bkp