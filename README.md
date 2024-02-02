# Simple GPS data simulator

## Description

This is a simple data-generator mocking a GPGGA data source. The datasource is then proccessed to an kafka-server (`hiwi-test-kafka-1:29092`)

## Task
Please provide a service which subscribes to the Kafka topic `location_topic` and visualize the data on a map. An containerized solution is preffered. You may extend the service to provide additional features like filtering, some additional visualization etc. You may use any programming language, any framework, any library. 

AC:
* [ ] The service need to use the data from the kafka topic `location_topic`
* [ ] The service should decode the protobuf data messages 
* [ ] The service should be able to visualize the data on a map
* [ ] The service should be containerized

Question to be answered:
* What an object can be expected moving on the map?

## Installation

### Building the project

* Dependencees
  * docker
  * protobuf (for decoding the data)

* Building the project:

```
docker compose up -d
```

### Usage

* For a better interaction with docker you can use the VSCode docker extension: https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker

* If the docker containers are running, you may find the kafka-UI (kafka-drop) at [http://localhost:9000/](http://localhost:9000/)


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

### Known issues
* Error while running the kafka broker (i.e. `unable to allocate file descriptor table - out of memory`):

-> Solution: as often can provide [stackoverflow](https://stackoverflow.com/questions/68776387/docker-library-initialization-failed-unable-to-allocate-file-descriptor-tabl)

(!) Please open an issue if you find any problem.

