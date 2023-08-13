#!/bin/bash

echo "# List of contributors to the repository:" > AUTHORS
echo >> AUTHORS

while IFS= read -r contributor; do
    echo "$contributor" >> AUTHORS
done < contributors.txt

echo "AUTHORS file generated."

