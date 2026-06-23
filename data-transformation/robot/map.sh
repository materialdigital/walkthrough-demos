#!/bin/bash

# download robot utility
if [ ! -f robot.jar ]; then
    wget "https://github.com/ontodev/robot/releases/download/v1.9.10/robot.jar"
fi

# download recent pmdco
if [ ! -f pmdco.owl ]; then
    wget --header="Accept: application/rdf+xml" -O pmdco.owl "https://w3id.org/pmd/co/"
fi

java -jar robot.jar template --input pmdco.owl  --template template.tsv --output result.ttl

cat result.ttl