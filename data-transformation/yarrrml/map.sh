#!/bin/bash
# Usage:
# - run in the directory where this script is located
# - supply the YARRRML file as the one and only argument
#
# Example:
#   ./map.sh tensile.yml

YARRRML_FILE=tensile.yml
RML_FILE=temp.rml.ttl

docker run --rm -it -v $(pwd):/data rmlio/yarrrml-parser:1.10.0 -i /data/${YARRRML_FILE} -o /data/${RML_FILE}
docker run --rm -it -v $(pwd):/data rmlio/rmlmapper-java:v7.3.3 -m /data/${RML_FILE}