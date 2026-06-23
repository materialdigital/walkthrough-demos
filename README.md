# Walkthrough Demos

## Data transformation 

A collection of educational examples demonstrating different approaches for transforming structured data into RDF using semantic web technologies.

The repository is intended for tutorials, workshops, and experimentation with mapping techniques based on the Platform MaterialDigital (PMD) ontology and related RDF vocabularies.

Repository Structure

```
walkthrough-demos/
├── data-transformation/
│   ├── yarrrml/            # YARRRML/RML mapping example
│   ├── ottr/               # OTTR template-based transformation example
│   ├── robot/              # Robot template-based transformation example
│   ├── python-rdflib/      # RDF generation using Python and RDFLib
│   └── python-template/    # Python template-based RDF generation example
└── README.md
```

## Overview

The **data-transformation** examples illustrate multiple strategies for generating RDF representations from **tabular** measurement data, including:

* Python template generation using simple string templates
* Python + RDFLib programmatic graph construction
* YARRRML/RML mappings executed with the RML Mapper
* OTTR template expansion using Lutra


The examples use a very simple CSV-based data as a simple educational use case.

## Usage

Each folder contains a `map.sh` or `map.py` file which can be executed to run the scripts. 

```
cd data-transformation/<folder> 
sh run.sh
```
```
cd data-transformation/<folder> 
python map.py
```

## Comparison Table

| Criterion               | Python Templates | Python + RDFLib | YARRRML/RML | OTTR  |
| ----------------------- | ---------------- | --------------- | ----------- | ----- |
| Easy to start           | ⭐⭐⭐⭐⭐            | ⭐⭐⭐⭐            | ⭐⭐⭐         | ⭐⭐    |
| RDF correctness         | ⭐⭐               | ⭐⭐⭐⭐⭐           | ⭐⭐⭐⭐⭐       | ⭐⭐⭐⭐⭐ |
| Reusability             | ⭐                | ⭐⭐              | ⭐⭐⭐⭐        | ⭐⭐⭐⭐⭐ |
| Maintainability         | ⭐⭐               | ⭐⭐⭐             | ⭐⭐⭐⭐        | ⭐⭐⭐⭐⭐ |
| Non-programmer friendly | ⭐                | ⭐               | ⭐⭐⭐⭐        | ⭐⭐⭐   |
| Standards-based         | ⭐                | ⭐⭐              | ⭐⭐⭐⭐⭐       | ⭐⭐⭐⭐  |
| Large-scale KG projects | ⭐                | ⭐⭐⭐             | ⭐⭐⭐⭐⭐       | ⭐⭐⭐⭐  |
| Learning RDF concepts   | ⭐⭐⭐⭐⭐            | ⭐⭐⭐⭐            | ⭐⭐⭐         | ⭐⭐⭐   |



## Practical Recommendation

For most real-world semantic data integration projects:

* YARRRML/RML is usually the best default choice because mappings are declarative, portable, and maintainable.
* Python + RDFLib is preferable when transformations involve substantial computation, data cleaning, external APIs, or complex business rules.
* OTTR is particularly valuable when the RDF model contains many recurring graph patterns and you want template reuse.
* Plain Python string templates are mainly useful for teaching, experimentation, and very small one-off transformations.
