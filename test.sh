#!/bin/bash

IP=$(curl http://localhost:2375/info)

echo "$IP"

curl -X POST -d "data=$IP" -d "key=drishya" http://localhost:5000/postdata

CNT=$(curl http://localhost:2375/containers/json?all=1)

echo "$CNT"

curl -X POST -d "data=$CNT" -d "key=drishya" http://localhost:5000/containers

VER=$(curl http://localhost:2375/version)

echo "$VER"

curl -X POST -d "data=$VER" -d "key=drishya" http://localhost:5000/version