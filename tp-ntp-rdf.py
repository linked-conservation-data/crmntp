from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import SKOS, RDF, RDFS, XSD
import csv

def getpropid(prop): #gets the property id based on a RDF node
    propid = str(prop).split('_')[0].split('/')
    propid = propid[len(propid) - 1]  # get the property id
    return propid

def gettpprop(propid, splabels): #gets the tpprop of the corresponding prop
    for splabel in splabels:
        if splabel[0] == propid:
            return splabel
    return False

# Prepare namespaces
namespaces = []
CRM = Namespace('http://www.cidoc-crm.org/cidoc-crm/')
CRMT = Namespace('http://www.cidoc-crm.org/extensions/crmntp/')
namespaces.append(('crm',CRM))
namespaces.append(('crmt',CRMT))

# collect RDF files for which we need TPs and NTPs
extensions = []
extensions.append(('cidoc-crm', 'https://cidoc-crm.org/rdfs/7.1.1/CIDOC_CRM_v7.1.1.rdfs'))

# collect the TP and NTP labels and examples from the csv file and enter them in the splabels array [p, label, domain, range]
tplabels = []
ntplabels = []
with open('negative-properties.csv', newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',', quotechar='"')
    header = next(rows)
    for row in rows:
        if not row[7] == '':
            tplabels.append((row[0], row[7] + " " + row[8], row[2], row[4]))
            ntplabels.append((row[0], row[15] + " " + row[16], row[2], row[4]))

for extension in extensions:
    g = Graph() # original extension
    g.parse(extension[1],format='xml')
    gp = Graph() # extension's TPs and NTPs
    # bind namespaces
    for namespace in namespaces:
        g.bind(namespace[0], namespace[1])
        gp.bind(namespace[0], namespace[1])
    for prop in g.subjects(RDF.type, RDF.Property):
        if not str(prop).split('_')[0].endswith('i'): # if it is not an inverse property (i.e. ignore the inverse properties)
            propid = getpropid(prop)
            tplabel = gettpprop(propid,tplabels)
            ntplabel = gettpprop(propid, ntplabels)
            if tplabel and ntplabel:
                tpprop = CRMT[tplabel[1].replace(" ","_")]
                ntpprop = CRMT[ntplabel[1].replace(" ", "_")]
                gp.add((tpprop,RDF.type,RDF.Property))
                gp.add((ntpprop, RDF.type, RDF.Property))
                for domain in g.objects(prop, RDFS.domain):
                    gp.add((tpprop, RDFS.domain, domain)) # the domain ot TP is the same as the domain of P
                    gp.add((ntpprop, RDFS.domain, domain))  # the domain ot NTP is the same as the domain of P
                gp.add((tpprop, RDFS.range, CRM['E55_Type']))  # the range ot TP is E55
                gp.add((ntpprop, RDFS.range, CRM['E55_Type']))  # the range ot TP is E55
                gp.add((tpprop,RDFS.label,Literal(tplabel[1], lang="en")))
                gp.add((ntpprop, RDFS.label, Literal(ntplabel[1], lang="en")))
                gp.add((tpprop, CRMT['H1'], prop))
                gp.add((ntpprop, CRMT['H1'], prop))
                gp.add((tpprop, CRMT['H2'], CRM['E55_Type']))
                gp.add((ntpprop, CRMT['H2'], CRM['E55_Type']))
                gp.add((tpprop, CRMT['Hn'], Literal("false", datatype=XSD.boolean)))
                gp.add((ntpprop, CRMT['Hn'], Literal("true", datatype=XSD.boolean)))
                for superproperty in g.objects(prop,RDFS.subPropertyOf):
                    superpropertyid = getpropid(superproperty)
                    supertplabel = gettpprop(superpropertyid, tplabels)
                    superntplabel = gettpprop(superpropertyid, ntplabels)
                    if supertplabel and superntplabel:
                        supertpprop = CRMT[supertplabel[1].replace(" ", "_")]
                        superntpprop = CRMT[superntplabel[1].replace(" ", "_")]
                        gp.add((tpprop, RDFS.subPropertyOf, supertpprop))
                        gp.add((ntpprop, RDFS.subPropertyOf, superntpprop))

    gp.serialize(destination=extension[0] + '-typed.ttl', format='turtle', encoding="utf-8")

    # props = g.query(
    #     """
    #     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    #     PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    #     PREFIX owl:<http://www.w3.org/2002/07/owl#>
    #     SELECT ?p
    #     WHERE {
    #         ?p a rdf:Property .
    #         FILTER NOT EXISTS { ?p owl:inverseOf ?pp }
    #
    #     }
    #     """
    # )
    #
    # for row in props:
    #     print(row)


