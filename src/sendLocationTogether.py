import time
import serial
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from confluent_kafka import Producer
import location_pb2  # Import the generated Protobuf module

# Delivery report for Kafka
def delivery_report(err, msg):
    """Delivery callback for Kafka produce."""
    if err is not None:
        print(f'Message delivery to Kafka failed: {err}')
    else:
        print(f'Message delivered to Kafka to {msg.topic()} [{msg.partition()}]')

# # Serial configuratipn for GPS data
# ser = serial.Serial(
# port='/dev/ttyACM0',
# baudrate=38400,
# parity=serial.PARITY_NONE,
# stopbits=serial.STOPBITS_ONE,
# bytesize=serial.EIGHTBITS,
# timeout=1
# )

# Kafka broker configuration
bootstrap_servers = '10.241.201.234:9092' 
producer = Producer({'bootstrap.servers': bootstrap_servers}) # Create a Kafka producer
location = location_pb2.location() # Create a position instance

# # InfluxDB connection details
# influxdb_url = "http://10.241.149.191:8086" # Laptop: 10.144.201.234
# influxdb_token = "BbgCTulbtyngf1TzbDVcdiWq4L8SQ1E5E1Zm8CD6vubjEoTH_ze_MAE8hnk4bxjjHUTY8gujW9kmM2reCQjaaw==" #"VogVu7KZwVamVJbK_sZ6sZkifYQmcneIUYRxbbpXNAds5jkNrGEHyFBZ17Y9ki6dvFdvt5j4yy6OzsgKKXw9Eg=="
# org = "ap" #"Trial"
# bucket = "rtk" #"RTK_Bucket"
# # username: aaryaapg
# # password: Kleps8vds

# # Initialize the InfluxDB client
# client = InfluxDBClient(url=influxdb_url, token=influxdb_token, org=org)
# write_api = client.write_api(j=SYNCHRONOUS)

while 1:
  # x=ser.readline( ).decode('latin-1').strip()
  # if x.startswith('$GNGGA'):
  #   print(x)
    # data_fields = x.split(',')
    # if len(data_fields) >= 15:
      location.utc_time      = float(data_fields[1])
      location.latitude      = data_fields[2][:2] + ' ' + data_fields[2][2:]
      location.lat_direction = data_fields[3]
      location.longitude     = data_fields[4][:3] + ' ' + data_fields[4][3:]
      location.lon_direction = data_fields[5]
      location.quality       = int(data_fields[6])
      location.num_sats      = int(data_fields[7])
      location.hdop          = float(data_fields[8])
      location.altitude      = float(data_fields[9])
      location.alt_units     = data_fields[10]
      location.undulation    = float(data_fields[11])
      location.und_units     = data_fields[12]
      location.age           = 0 if data_fields[13]=="" else float(data_fields[13])
      location.stn_id        = data_fields[14]

      # # Send the extracted fields to InfluxDB
      # point = (
      #     Point("gps_data")
      #     .field("utc_time"  , location.utc_time)
      #     .field("latitude"  , location.latitude)
      #     .field("longitude" , location.longitude)
      #     .field("quality"   , location.quality)
      #     .field("num_sats"  , location.num_sats)
      #     .field("hdop"      , location.hdop)
      #     .field("altitude"  , location.altitude)
      #     .field("alt_units" , location.alt_units)
      #     .field("undulation", location.undulation)
      #     .field("und_units" , location.und_units)
      #     .field("age"       , location.age)
      #     .field("stn_id"    , location.stn_id)
      # )
      # write_api.write(bucket=bucket, org=org, record=point)
      # print("Sent to InfluxDB \n")
      # print("UTC Time:", location.utc_time, ": ", location.latitude, ", ", location.longitude)

      # Send the extracted fields to Kafka
      serialized_location = location.SerializeToString()
      # readable_message = f"Latitude: {location.latitude}, Longitude: {location.longitude}, Altitude: {location.altitude}"
      topic = 'location_topic'  
      producer.produce(topic=topic, key="rover", value=serialized_location, callback=delivery_report)
      #producer.produce(topic, value=readable_message.encode('utf-8'), callback=delivery_report)      
      producer.flush() # Flush messages and close producer