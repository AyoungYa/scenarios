#!/bin/bash

if [[ ! -d /home/joker5 ]]; then
  sudo cat /etc/passwd | grep -w joker5
  [ $? -ne 0 ] && echo "pass"
fi
