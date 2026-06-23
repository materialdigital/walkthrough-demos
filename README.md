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
* ROBOT template expansion into OWL using the ROBOT tool


The examples use a very simple CSV-based data set as an educational use case.

## Example data

All examples transform the same two tensile-strength measurements:

| obj_id | value | unit |
|--------|-------|------|
| 1 | 520 | `http://qudt.org/vocab/unit/MegaPA` |
| 2 | 550 | `http://qudt.org/vocab/unit/MegaPA` |

Each measurement is modelled with the PMD / BFO / OBI / RO pattern: a specimen *has a
quality* (tensile strength) whose value is captured by a *value specification*, produced
as the *measurement datum* of a *measurement process*.

## Prerequisites

Depending on the method you want to run:

| Method | Requirements |
|--------|--------------|
| `python-template` | Python 3 (standard library only) |
| `python-rdflib` | Python 3 + [`rdflib`](https://rdflib.readthedocs.io/) (`pip install rdflib`) |
| `ottr` | Java (JRE 8+); `map.sh` downloads [Lutra](https://ottr.xyz/) automatically |
| `yarrrml` | Docker; `map.sh` pulls the `rmlio/yarrrml-parser` and `rmlio/rmlmapper-java` images |
| `robot` | Java (JRE 8+); `map.sh` downloads [ROBOT](http://robot.obolibrary.org/) and the PMD core ontology automatically |

The `ottr`, `yarrrml` and `robot` examples require internet access on first run to fetch
their tooling. Downloaded tools and generated outputs are git-ignored.

## Methods

* **`python-template/`** — fills a plain string template per CSV row and prints Turtle.
  Simplest approach, no dependencies, but performs no validation.
* **`python-rdflib/`** — builds the graph programmatically with RDFLib and serialises it.
  Guaranteed to be syntactically valid; good when you need logic or branching.
* **`ottr/`** — defines the triple pattern once as a reusable [OTTR](https://ottr.xyz/)
  template and expands the data instances with Lutra. Two variants are provided: a named
  one (stable IRIs for every individual) and a blank-node one (`map-blank.sh`).
* **`yarrrml/`** — declarative [YARRRML](https://rml.io/yarrrml/) mapping rules that are
  compiled to RML and executed against the CSV with the RML Mapper.
* **`robot/`** — a [ROBOT](http://robot.obolibrary.org/) spreadsheet template (TSV) that is
  expanded into a full OWL ontology, resolving labels to IRIs via the PMD core ontology.

## Usage

Each folder contains a `map.sh` or `map.py` file which can be executed to run the example.

```
cd data-transformation/<folder>
sh map.sh
```

```
cd data-transformation/<folder>
python map.py
```

## Comparison

At a glance:

|  | python-template | python-rdflib | ottr | yarrrml | robot |
|--|-----------------|---------------|------|---------|-------|
| **Paradigm** | string templating | programmatic (RDFLib) | OTTR templates | YARRRML/RML rules | ROBOT template |
| **Runtime** | Python | Python + rdflib | Java (Lutra) | Docker | Java (ROBOT) |
| **Input** | CSV | CSV | stOTTR | CSV + YAML | TSV |
| **Output** | Turtle | Turtle | Turtle | N-Triples | OWL (Turtle) |
| **Produces** | instance data | instance data | instance data | instance data | OWL ontology |

### Comparison Table

| Criterion               | Python Templates | Python + RDFLib | YARRRML/RML | OTTR  | ROBOT |
| ----------------------- | ---------------- | --------------- | ----------- | ----- | ----- |
| Easy to start           | ⭐⭐⭐⭐⭐            | ⭐⭐⭐⭐            | ⭐⭐⭐         | ⭐⭐    | ⭐⭐    |
| RDF correctness         | ⭐⭐               | ⭐⭐⭐⭐⭐           | ⭐⭐⭐⭐⭐       | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐  |
| Reusability             | ⭐                | ⭐⭐              | ⭐⭐⭐⭐        | ⭐⭐⭐⭐⭐ | ⭐⭐⭐   |
| Maintainability         | ⭐⭐               | ⭐⭐⭐             | ⭐⭐⭐⭐        | ⭐⭐⭐⭐⭐ | ⭐⭐    |
| Non-programmer friendly | ⭐                | ⭐               | ⭐⭐⭐⭐        | ⭐⭐⭐   | ⭐⭐⭐⭐  |
| Standards-based         | ⭐                | ⭐⭐              | ⭐⭐⭐⭐⭐       | ⭐⭐⭐⭐  | ⭐⭐⭐⭐  |
| Large-scale KG projects | ⭐                | ⭐⭐⭐             | ⭐⭐⭐⭐⭐       | ⭐⭐⭐⭐  | ⭐⭐    |
| Learning RDF concepts   | ⭐⭐⭐⭐⭐            | ⭐⭐⭐⭐            | ⭐⭐⭐         | ⭐⭐⭐   | ⭐⭐⭐   |

### Strengths and weaknesses

| Method | Strengths | Weaknesses |
|--------|-----------|------------|
| python-template | trivial, no dependencies, full control | no validation → easily produces invalid RDF; scales poorly |
| python-rdflib | real graph object, guaranteed syntactically valid, good for logic/branching | imperative, pattern scattered across many `g.add()` calls |
| ottr | declarative, pattern defined once, compact data, datatype typing | Java tooling, custom stOTTR syntax |
| yarrrml / RML | W3C-aligned standard, declarative, works directly from CSV/JSON/DB, ETL-ready | heavy runtime (Docker / large jars), YAML learning curve |
| robot | produces a full OWL ontology, label→IRI resolution | tied to the OWL/ROBOT workflow, the spreadsheet gets unwieldy quickly |

### Practical Recommendation

For most real-world semantic data integration projects:

* YARRRML/RML is usually the best default choice because mappings are declarative, portable, and maintainable.
* Python + RDFLib is preferable when transformations involve substantial computation, data cleaning, external APIs, or complex business rules.
* OTTR is particularly valuable when the RDF model contains many recurring graph patterns and you want template reuse.
* ROBOT is the right choice when the goal is an OWL ontology (classes, axioms, labels) rather than just instance data, especially within the OBO / ontology-engineering ecosystem.
* Plain Python string templates are mainly useful for teaching, experimentation, and very small one-off transformations.

For a full side-by-side comparison — the RDF each one produces, the triple-level pattern,
and their differences — see
[`data-transformation/COMPARISON.md`](data-transformation/COMPARISON.md).
