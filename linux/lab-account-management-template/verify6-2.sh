#!/bin/bash

# Check if the jack user and his home diectory has been deleted.
if [ ! -d /home/adam ]; then
  sudo grep -w 'jack' /etc/passwd || echo "pass"
fi
