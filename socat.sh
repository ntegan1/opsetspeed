#!/bin/bash

optool=/data/media/optool

source ${optool}/env.sh

socat TCP-LISTEN:80,fork TCP:127.0.0.1:3000

