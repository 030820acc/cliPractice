#!/bin/sh

echo "Welcome to Pretty Print"
echo "Which file should I print for you?"
read FILE

echo "==============================================================="
cat $FILE
echo "==============================================================="
echo "^^^THERES YOUR FILE. You're welcome."
