#!/bin/bash

# Check if the joker user's shell is changed.
sudo grep -w 'joker' /etc/passwd | grep -w 'bash'
