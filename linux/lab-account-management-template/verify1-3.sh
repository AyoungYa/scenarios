#!/bin/bash

# Check if the jack user is created and home directory exists
(sudo grep -w 'jack' /etc/passwd) && [ -d /home/adam ]
