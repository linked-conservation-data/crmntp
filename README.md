# Extension of the CIDOC CRM for typed and negative typed properties

CRMntp is an extension to the CIDOC-CRM ontology which allows the production of typed and negative typed statements.

It applies to RDFS implementations of the CIDOC-CRM and brings limited new semantics. An implementation in OWL, for example, does not require this extension.

The extension allows statements about:
* numerous individuals without them being recorded and
* absence of individuals of a given type.

In a typical scenario the following triples:

```
:a P :b
:b P2_has_type :t
```

where `P` is any CRM property and `:b` an individual which is not possible to record, we can write:

```
:a TP :t
```

to indicate at least that the type of a possible `:b` is `:t`.

We can also write:

```
:a NTP :t
```
to indicate that there is no `:b` of type `:t`.

This extension provide the `TP` and `NTP` properties alongside their basic axioms that allow them to be retrieved with queries of `P`:

```
TP a rdf:property ;
	H1 P ;
	H2 P2_has_type ;
	Hn false .

TP rdfs:domain Pd .

TP rdfs:range E55_Type .

```

where `Pd` is the domain of `P`.

A detailed analysis of this is included in a [paper under review and revision](http://semantic-web-journal.org/content/typed-properties-and-negative-typed-properties-dealing-type-observations-and-negative) for the Semantic Web Journal.

In this repository you will find:

* the RDFS file for typed and negative types properties for the CIDOC CRM [https://github.com/linked-conservation-data/crmntp/blob/main/cidoc-crm-typed.ttl](cidoc-crm-typed.ttl)
* a python script which downloads the latest CIDOC CRM RDFS file and creates the extension RDFS file automatically [https://github.com/linked-conservation-data/crmntp/blob/main/tp-ntp-rdf.py](tp-ntp-rdf.py)
* a CSV file with the labels of the extension properties [https://github.com/linked-conservation-data/crmntp/blob/main/negative-properties.csv](negative-properties.csv)

At the same time there is an ongoing effort to produce scope notes and examples for every property of the extension with the intention to produce a Word document.

* the python script `csv2md.py` produces the markdown files under the `source` directory from the CSV file, which contain the scope notes and examples
* the python script `ntp2docx.py` produces a Word document file based on the CRM SIG template `template.docx`
* the `demo.docx` file shows what the final result would be

Given that the semantics of the new properties are limited, the RDFS file can be used as is.
There is no correspondence between the `demo.docx` file and the `cidoc-crm-typed.ttl` file at the moment. 