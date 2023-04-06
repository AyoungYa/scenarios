#!/bin/bash

# Check if password is set for joker user
[[ $(sudo grep -w joker /etc/shadow | awk -F: '{print $2}' | awk '{print length($0)}') -gt 6 ]]
