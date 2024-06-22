FROM ubuntu:latest
LABEL authors="Jose Adolfo"

FROM python:3.8-slim

ENV AIRFLOW_HOME=/airflow

RUN pip install apache-airflow

COPY ../dags/mi_primer_dag.py /airflow/dags/mi_primer_dag.py

EXPOSE 8080 5555
RUN airflow db init

CMD ["airflow", "webserver", "--port", "8080", "&", "airflow", "scheduler"]


ENTRYPOINT ["top", "-b"]