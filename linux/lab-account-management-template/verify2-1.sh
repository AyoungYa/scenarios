#!/bin/bash

# Check if the fly user is created and the group exists
(sudo grep -w 'fly' /etc/passwd) && (sudo grep -w 'fly' /etc/group)
