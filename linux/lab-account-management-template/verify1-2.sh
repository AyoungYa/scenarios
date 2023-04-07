#!/bin/bash

# Check if the bob user is created and home directory exists
(sudo grep -w 'bob' /etc/passwd) && [ -d /home/bob ]
