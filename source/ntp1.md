# NTP1 is not identified by appellation of type

## Domain: 

E1 CRM Entity

## Range: 

E55 Type

## Superproperty of: 

E1 CRM Entity. [NTP48](#ntp48) does not have preferred identifier of type: E55 Type
E71 Human-Made Thing. [NTP102](#ntp102) does not have title of type: E55 Type

## Quantification: 

todo

## Scope note: 

This property connects an instance of E1 CRM Entity with a type (E55 Type) which is valid for the class E41 Appellation. 
The domain instance is not identified by any instances of E41 Appellation of that type.

## Examples: 

* Sinai MS Greek 418 (E22) _is not identified by appellation type_ ISBN (E55). [The book does not have an ISBN number]

## In First Order Logic: 

NTP1(x,y) ⇒ E1(x)
NTP1(x,y) ⇒ E55(y)

