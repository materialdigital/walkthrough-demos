# Comparison of the data-transformation methods

A comparison of the five approaches in `data-transformation/` that convert the same
tabular tensile-strength measurement data into RDF — based on the PMD / BFO / OBI / RO
modelling pattern.

> **Use case:** 2 measurements (`obj_1` = 520 MPa, `obj_2` = 550 MPa, unit QUDT `MegaPA`).
> Expected pattern per measurement: *a specimen has a tensile strength, determined in a
> measurement process with a value + unit.*

---

## 1. Overview: paradigm & setup

| Method | Paradigm | Runtime / dependencies | Input | Run |
|--------|----------|------------------------|-------|-----|
| **python-template** | String templating | Python (stdlib only) | CSV inline | `python map.py` |
| **python-rdflib** | Programmatic graph construction | Python + `rdflib` | CSV inline | `python map.py` |
| **ottr** | Declarative ontology templates | Java + Lutra (≈44 MB) | `.stottr` files | `sh map.sh` |
| **yarrrml / RML** | Declarative mapping rules | Docker *(or Node + rmlmapper ≈184 MB)* | CSV + YAML | `sh map.sh` |
| **robot** | Spreadsheet → OWL template | Java + ROBOT (≈83 MB) + ontology (pmdco) | TSV | `sh map.sh` |

---

## 2. Results (after bug fixes)

| Method | Status | #Triples | #Measurements | Value datatype | Example namespace |
|--------|--------|---------:|--------------:|----------------|-------------------|
| python-template | ✅ valid | 22 | 2 | `"520"` (string) | `example.com/ns#` |
| python-rdflib | ✅ valid | 22 | 2 | `"520"` (string) | `example.org/` |
| ottr (named) | ✅ valid | 22 | 2 | `520` (**integer**) | `example.com/ns#` |
| yarrrml | ✅ valid | 22 | 2 | `"520"` (string) | `example.com/` |
| robot | ✅ valid (OWL) | 68 | 2 | `"520"` (string) | `example.org/` |

Validated with `rdflib` 7.6.0; the yarrrml output is N-Triples, the rest Turtle.

---

## 3. Instance pattern per measurement (✓ = triple present)

| (Subject – Predicate – Object) | py-template | py-rdflib | ottr | yarrrml | robot |
|---|:--:|:--:|:--:|:--:|:--:|
| `qual a tensile_strength` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `obj has_quality qual` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `obj has_role role` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `datum a measurement_datum` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `datum has_value_specification spec` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `proc has_participant obj` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `spec has_measurement_unit_label MegaPA` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `proc realizes role` | ✓ | ✓ | ✓ | ✓ | **·** |
| `spec specifies_value_of qual` | ✓ | ✓ | ✓ | ✓ | **·** |
| `spec has_specified_numeric_value` (`OBI_0001937`) | ✓ | ✓ | ✓ | ✓ | **·** |
| `datum specified_output_of proc` | ✓ | **·** | ✓ | ✓ | **·** |
| `obj specified_output_of proc` | · | **✓ ⚠** | · | · | · |
| `datum specifies_value_of qual` | · | · | · | · | **✓ ⚠** |
| `spec has_specified_value` (`OBI_0002135`) | · | · | · | · | **✓ ⚠** |
| `obj a object` / `role a test_piece_role` / `proc a …process` / `spec a value_specification` | · | · | · | · | **✓** |

**Common core** (top 7 rows): identical across all methods. **python-template, ottr and
yarrrml** produce the full, consistent 11-triple pattern per measurement. **python-rdflib**
and **robot** deviate (see ⚠ and Section 5).

---

## 4. Bugs fixed

Errors found and corrected in the example files during the comparison:

### Fix 1 — `python-template/map.py` (output was invalid Turtle)
The prefix block did not declare `ex:` and `rdf:`, although the template uses them.
```diff
  prefix="""
+ @prefix ex: <http://example.com/ns#> .
+ @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
  @prefix tensile_strength: <https://w3id.org/pmd/tto/TTO_0000053> .
```
Before: parser aborted (`Bad syntax (Prefix "ex)`). After: 22 triples, valid.

### Fix 2 — `yarrrml/tensile.csv` (only 1 instead of 2 measurements)
```diff
  obj_id,value,unit
  1,520,http://qudt.org/vocab/unit/MegaPA
- #2,550,http://qudt.org/vocab/unit/MegaPA
+ 2,550,http://qudt.org/vocab/unit/MegaPA
```

### Fix 3 — `robot/map.sh` (download wrote a log file instead of the ontology)
`wget -o` = log file; the correct flag is `-O` = output file.
```diff
- wget "https://w3id.org/pmd/co/" -o pmdco.owl
+ wget --header="Accept: application/rdf+xml" -O pmdco.owl "https://w3id.org/pmd/co/"
```

### Fix 4 — `robot/template.tsv` (only covered 1 measurement)
Added six rows for the second measurement (`obj_2 … spec_2`, value `550`), matching the
27-column layout of measurement 1. The single `tensile strength` class definition
(`TTO_0000053`) is *not* duplicated. After: 68 triples, 2 measurements.

---

## 5. Remaining inconsistencies (not plain typos)

Substantive modelling differences that were **not** changed:

- **python-rdflib:** `specified_output_of` is attached to `obj` instead of `datum`
  (`g.add((obj, specified_output_of, proc))`).
- **robot:** uses `OBI_0002135` (*has specified value*) instead of `OBI_0001937`
  (*has specified numeric value*); attaches `specifies_value_of` to the `datum`;
  `realizes` and `specified_output_of` are missing (labels not resolved in pmdco).
- **Datatype:** only **ottr** types the value as `xsd:integer`; the others use `xsd:string`.
- **Namespaces:** inconsistent (`example.com/ns#`, `example.com/`, `example.org/`).

---

## 6. When to use which

| Method | Strengths | Weaknesses |
|--------|-----------|------------|
| **python-template** | trivial, no dependencies, full control | no validation → easily produces invalid RDF; scales poorly |
| **python-rdflib** | real graph object, guaranteed syntactically valid, good for logic/branching | imperative, pattern scattered across many `g.add()` calls |
| **ottr** | declarative, pattern defined *once*, compact data, datatype typing | Java tooling, custom stOTTR syntax |
| **yarrrml / RML** | W3C-aligned standard, declarative, works directly from CSV/JSON/DB, ETL-ready | heavy runtime (Docker / large jars), YAML learning curve |
| **robot** | produces a full OWL ontology, label→IRI resolution | tied to the OWL/ROBOT workflow, the spreadsheet gets unwieldy quickly |

**Conclusion:** all hit the same semantic core, but they are **not** triple-identical —
they differ in coverage, datatypes, OWL scaffolding and individual properties. For pure
**data→RDF transformation**, **ottr** (compact/declarative) or **yarrrml/RML** (standard,
ETL) are the cleanest; **python-rdflib** is the pragmatic all-purpose choice; **robot** is
the right tool when the goal is an **ontology** (not just instance data).
