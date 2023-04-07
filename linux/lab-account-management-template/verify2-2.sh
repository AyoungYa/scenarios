#!/bin/bash

# Check if the joker user was created through the public group
(sudo grep -w 'bill' /etc/passwd) && (sudo grep -w 'public' /etc/group)
