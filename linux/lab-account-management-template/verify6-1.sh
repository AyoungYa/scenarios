#!/bin/bash

# Check if the bob user has been deleted and the user directory is still saved.
if [[ -d /home/bob ]]; then
  sudo grep -w 'bob' /etc/passwd || echo "pass"
fi
