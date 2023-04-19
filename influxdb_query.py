from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "all_about"

client = InfluxDBClient(url="http://localhost:8086", token="UMKY6z06AaMyL7tQlX8_mqfNuY4r_S99wqzwX7sPtbD4-PXmcjxTdwcHJDLUWj8RnEtYrXUzR7K1QePDorDzOg==", org="psu")

write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

## using Table structure
tables = query_api.query(f'from(bucket:"{bucket}") |> range(start: -1m)')

for table in tables:
    print(table)
    for row in table.records:
        print (row.values)
