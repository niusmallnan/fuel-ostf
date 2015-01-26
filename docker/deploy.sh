#!/bin/bash
#
# The MIT License (MIT)
# Copyright (c) 2014 fishcried(tianqing.w@gmail.com)
#

image="neunn-ostf:v1.0"
password="Neunn@123"

# api
docker run -d -e "ROOT_PASS=$password" -p 8777:8777 -p 10022:22 --name neunn-ostf $image 
