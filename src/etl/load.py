import json
import os
from sqlalchemy import create_engine, inspect
import pika


def push_message_to(amqp_url, message, queue_name):

    url_params = pika.URLParameters(amqp_url)

    connection = pika.BlockingConnection(url_params)
    channel = connection.channel()

    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_publish(
        exchange="",
        routing_key=queue_name,
        body=json.dumps(message),
        properties=pika.BasicProperties(delivery_mode=2),
    )
    print(" [x] Message Sent to " + queue_name)
    connection.close()


def load_to_db(df, table, pg_url):

    if pg_url:
        engine = create_engine(pg_url)

    if check_if_table_exists(engine, table):
        with engine.connect() as conn:
            df.to_sql(table, conn, if_exists="replace", method="multi")
    else:
        with engine.connect() as conn:
            df.to_sql(table, conn, method="multi")


def check_if_table_exists(engine, table_name):
    if table_name in inspect(engine).get_table_names():
        print(table_name + " exists in the DB!")
        return True
    else:
        print(table_name + " does not exist in the DB!")
        return False
