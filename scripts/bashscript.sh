#!/bin/bash

echo "Hello, $USER!"
sleep 0.5
if [ "$LANGUAGE" = "All" ]; then
	echo "You chose to execute all languages, what a curious!"
else
    echo "You chose to execute $LANGUAGE script, Great choise!"
fi
echo "Your location is:"
pwd
echo "Your IP adress is:"
hostname -I
echo "Cya next time!"

