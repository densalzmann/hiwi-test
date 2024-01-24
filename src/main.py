import time
from datetime import datetime,timezone
from confluent_kafka import Producer
from gen import location_pb2  # Import the generated Protobuf module

# Delivery report for Kafka
def delivery_report(err, msg):
    """Delivery callback for Kafka produce."""
    if err is not None:
        print(f'Message delivery to Kafka failed: {err}')
    else:
        print(f'Message delivered to Kafka to {msg.topic()} [{msg.partition()}]')

# Kafka broker configuration
bootstrap_servers = 'hiwi-test-kafka-1:29092' 
producer = Producer({'bootstrap.servers': bootstrap_servers}) # Create a Kafka producer
location = location_pb2.location() # Create a position instance

while 1:
  location.utc_time      = datetime.now(timezone.utc).timestamp()
  location.latitude      = "18" + ' ' + "1908.00"
  location.lat_direction = "N"
  location.longitude     = "070" + ' ' + "44.3966270"
  location.lon_direction = "W"
  location.quality       = 4
  location.num_sats      = 13
  location.hdop          = 1.0
  location.altitude      = 495.144
  location.alt_units     = "M"
  location.undulation    = 29.200
  location.und_units     = "M"
  location.age           = 0.0
  location.stn_id        = "0000"
  
  print(location)
  
  # Send the extracted fields to Kafka
  serialized_location = location.SerializeToString()
  topic = 'location_topic'  
  producer.produce(topic=topic, key="rover", value=serialized_location, callback=delivery_report)    
  producer.flush() # Flush messages and close producer

  time.sleep(1)