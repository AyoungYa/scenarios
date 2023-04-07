#!/bin/bash

# Check if the joker  user's home directory is changed.
sudo grep -w 'joker' /etc/passwd | grep -w '/home/shiyanlou'
