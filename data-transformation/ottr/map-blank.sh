#!/bin/bash


if [ ! -f lutra-v0.6.20.jar ]; then
    wget "https://ottr.xyz/downloads/lutra/lutra-v0.6.20.jar"
fi

java -jar lutra-v0.6.20.jar --mode expand --library tensile-template-blank.stottr --libraryFormat stottr --fetchMissing --inputFormat stottr tensile-data-blank.stottr
