# Simple GPS data simulator
## Description
This is a simple data-generator mocking GPGGA signal data. The datasource is then proccessed to an kafka-server()

### Protobuf

* Generating python descriptors (Win64)

```
    protoc -I="." --python_out=src/gen ./location.proto
```

* Generating kafkadrop descriptors (Ubuntu)

```
    sudo apt install -y kafkacat protobuf-compiler
    protoc -o descriptors/location.desc location.proto
    
```