# TP1 is identified by appellation type

## Domain: 

E1 CRM Entity

## Range: 

E55 Type

## Superproperty of: 

todo

## Subproperty of: 

todo

## Quantification: 

todo

## Scope note: 

This property is a shortcut of the fully developed path: E1 CRM Entity, _P1 is identified by (identifies)_, E41 Appellation, _P2 has type_, E55 Type

## Examples: 

* book is identified by an ISBN number

## In First Order Logic: 

TP1(x,y) ⇒ E1(x)
TP1(x,y) ⇒ E55(y)
TP1(x,y) ⇔ (∃ z)[E41(z) ∧ P1(x,z) ∧ P2(z,y)]

