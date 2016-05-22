#!/bin/bash
# bash generate random alphanumeric string
#

# bash generate random 32 character alphanumeric string (upper and lowercase) and
key=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 64 | head -n 1)
echo $key > app/secret_key.txt
