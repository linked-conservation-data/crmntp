# NTP4 does not have time-span of type

## Domain: 

E2 Temporal Entity

## Range: 

E55 Type

## Quantification: 

todo

## Scope note: 

This property connects an instance of E2 Temporal Entity with a type (E55 Type). The domain instance does not have an instance of E52 Time-Span of that type.

## Examples: 

* The 50th CIDOC-CRM meeting (E7) _does not have time-span of type_ week (E55). [The meeting duration was a few days, i.e. less than a week]

## In First Order Logic: 

NTP4(x,y) ⇒ E2(x)
NTP4(x,y) ⇒ E55(y)

