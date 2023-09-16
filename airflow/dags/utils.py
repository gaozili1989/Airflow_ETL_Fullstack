from datetime import timedelta, datetime
import psycopg2
import boto3
rds_client = boto3.client('rds')

def generate_file_name(origin, destination, departure_date_str):
    date_str = datetime.strptime(departure_date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
    return f"{origin}-{destination}-{date_str}.json"

def generate_departure_date(departureDate = None, days = 14):
    if not departureDate:
        delta = timedelta(days=days)
        departureDate = datetime.today() + delta
    return departureDate



def get_endpoint():
    instance_identifier = "flights-db"
    response = rds_client.describe_db_instances(
        DBInstanceIdentifier=instance_identifier
    )
    return response['DBInstances'][0]['Endpoint']['Address']

def build_conn(db_name):
    endpoint = get_endpoint()
    conn = psycopg2.connect(
    host=endpoint,
    port=5432,
    dbname=db_name,
    user='jigsaw',
    password='jigsawlabs')
    return conn