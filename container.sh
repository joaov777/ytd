#!/bin/bash

SCRIPT_FILE=$(readlink -f "$0") # script absolute path
SCRIPT_DIR=$(dirname "$SCRIPT_FILE") # script directory
PROJECT_DIR=$(dirname $(dirname $(dirname $SCRIPT_DIR))) #base file system (/)
CONTAINER_NAME="ytd"

# Uncomment this line for debugging
#echo -e "$SCRIPT_FILE\n$SCRIPT_DIR\n$PROJECT_DIR\n$CONTAINER_NAME" |

# retrieve all local container names
CONTAINER=$(docker ps -f name=$CONTAINER_NAME --format "{{.Names}}")

# delete potential existing container
[ $CONTAINER ] && docker rm -f $CONTAINER_NAME

# creates the container
docker run -it --rm --name $CONTAINER_NAME \
	-v $SCRIPT_DIR:/ytd \
	-w /ytd python:3.10.0 bash -c "pip install -r /ytd/requirements.txt && python /ytd/ytd.py"

