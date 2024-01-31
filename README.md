# Simple GPS data simulator
## Description
This is a simple data-generator mocking GPGGA signal data. The datasource is then proccessed to an kafka-server()

### Building the project
* Dependencees
    * docker
    * protobuf
* Building the project:
```
    docker compose up -d
```
* If the docker containers are running, you may find the kafka-UI (kafka-drop)

### Protobuf

* Install protobuf
```
    sudo apt install -y kafkacat protobuf-compiler
```

* Generating python descriptors
```
    protoc -I="." --python_out=src/gen ./location.proto
```

* Generating kafkadrop descriptors (Ubuntu)
```
    protoc -o descriptors/location.desc location.proto
    
```