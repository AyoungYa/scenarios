#!/bin/bash

# Check if the glen system user is created and the home directory not exists
(sudo grep -w 'glen' /etc/passwd | grep -w 'nologin') && [[ ! -d /home/glen ]]
