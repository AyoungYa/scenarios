#!/bin/bash

if [[ -d /home/joker ]]; then
  sudo cat /etc/passwd | grep -w joker
  [ $? -ne 0 ] && echo "pass"
fi
