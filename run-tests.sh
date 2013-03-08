#!/bin/bash

# this script runs tests, assuming we have unit2 in a virtualenv or path

if which unit2 &>/dev/null; then
	UNIT2=`which unit2`
else
	MYDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
	UNIT2=`find $MYDIR -name unit2`
fi

CMD="$UNIT2 discover -s pybrid"

echo $CMD

$CMD
