from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import json
import pandas as pd

bucket_name = "itscoe-bucket"

client = InfluxDBClient(url="http://172.30.222.54:8086", token="its-all-about-the-computer-engineering", org="coe-psu")

write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

## using Table structure
query_str = f'''from(bucket: "{bucket_name}")
  |> range(start: -10m)
  |> filter(fn: (r) => r["_measurement"] == "environment")
  |> filter(fn: (r) => r["_field"] == "humidity" or r["_field"] == "light" or r["_field"] == "raindrop" or r["_field"] == "temperature")
  |> aggregateWindow(every: 1m, fn: mean, createEmpty: false)
  |> yield(name: "mean")
  '''

print(query_str)

tables = query_api.query(query_str)
results = []

for table in tables:
  for record in table.records:
    results.append((record.get_time(), record.get_field(), record.get_value()))

df = pd.DataFrame(results, columns=["time", "field", "value"])
print(results)
print(df)
print(df[df["field"] == "temperature"])
