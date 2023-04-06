#!/bin/bash

# Check if the joker user's uid is changed.
sudo grep -w 'joker' /etc/passwd | grep -w '8888'
