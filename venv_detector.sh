#!/bin/bash
activate () {
	. venv/bin/activate
}

if [ ! -f ./venv/bin/activate ]; then
	echo "NO VENV"
	exec virtualenv venv -p python3.6
fi

if [ -z "$VIRTUAL_ENV" ]; then
	# Undefined VIRTUAL_ENV
	echo "UNDEFINED"
	activate
fi
