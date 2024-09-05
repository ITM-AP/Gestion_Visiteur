#!/bin/bash

TAG=$1
IMAGE_NAME=antoineitm/gestion_visiteur

docker build -t $IMAGE_NAME:$TAG -t $IMAGE_NAME:latest .

docker push $IMAGE_NAME:$TAG
docker push $IMAGE_NAME:latest