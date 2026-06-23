

prefix="""
@prefix ex: <http://example.com/ns#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix tensile_strength: <https://w3id.org/pmd/tto/TTO_0000053> .
@prefix has_quality: <http://purl.obolibrary.org/obo/RO_0000086> .
@prefix has_role: <http://purl.obolibrary.org/obo/RO_0000087> .
@prefix has_value_specification: <http://purl.obolibrary.org/obo/OBI_0001938> .
@prefix specifies_value_of: <http://purl.obolibrary.org/obo/OBI_0001927> .
@prefix has_participant: <http://purl.obolibrary.org/obo/RO_0000057> .
@prefix specified_output_of: <http://purl.obolibrary.org/obo/OBI_0000312> . 
@prefix realizes: <http://purl.obolibrary.org/obo/BFO_0000055> .
@prefix has_specified_numeric_value: <http://purl.obolibrary.org/obo/OBI_0001937> .
@prefix has_measurement_unit_label: <http://purl.obolibrary.org/obo/IAO_0000039> .
@prefix measurement_datum: <http://purl.obolibrary.org/obo/IAO_0000109> .
"""

template = """
ex:qual_{id}   rdf:type   tensile_strength: .
ex:proc_{id}   has_participant:  ex:obj_{id} .
ex:datum_{id}  has_value_specification:  ex:spec_{id} .
ex:spec_{id}   has_specified_numeric_value:  {val} .
ex:obj_{id}    has_role:  ex:role_{id} .
ex:datum_{id}  rdf:type   measurement_datum:.
ex:datum_{id}  specified_output_of:  ex:proc_{id} .
ex:spec_{id}   has_measurement_unit_label:  <http://qudt.org/vocab/unit/{unit}> .
ex:proc_{id}   realizes:  ex:role_{id} .
ex:spec_{id}   specifies_value_of:  ex:qual_{id} .
ex:obj_{id}    has_quality:  ex:qual_{id} .
"""

csv="""obj_id,value,unit
1,520,MegaPA
2,550,MegaPA"""

print (prefix)
for row in csv.split("\n")[1:]:  # this is just an example; please use a proper CSV reader lib
	r=row.split(",")
	id = r[0]
	value = r[1]
	unit = r[2]
	print (template.format(id=id, val=value, unit=unit))








