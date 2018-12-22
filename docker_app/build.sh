#!/bin/bash

docker build -t zmeigen/app . && docker push zmeigen/app && ssh root@genius-apps.com docker pull zmeigen/app