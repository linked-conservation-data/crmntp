import csv

with open('negative-properties.csv', newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',', quotechar='"')
    header = next(rows)
    for row in rows:
        # TP property
        if row[7] != "":
            file = open("source/" + row[7].lower() + ".md", "w")
            file.write("# " + row[7] + " " + row[8] + '\n\n') # e.g. "# TP56 bears feature of type (is type of feature found on)"
            file.write("## Domain: " + '\n\n') # e.g. "# Domain:"
            file.write(row[2] + " " + row[3] + '\n\n') # e.g. "E19 Physical Thing"
            file.write("## Range: " + '\n\n') # e.g. "## Range:"
            file.write("E55 Type" + '\n\n') # always E55
            file.write("## Superproperty of: " + '\n\n')  # e.g. "## Superproperty of"
            file.write("todo" + '\n\n')  # e.g. todo manually
            file.write("## Subproperty of: " + '\n\n')  # e.g. "## Subproperty of"
            file.write("todo" + '\n\n')  # e.g. todo manually
            file.write("## Quantification: " + '\n\n')  # e.g. "## Quantification"
            file.write("todo" + '\n\n')  # e.g. todo manually
            file.write("## Scope note: " + '\n\n')  # e.g. "## Scope note"
            file.write(row[13] + '\n\n')  # e.g. This property is a shortcut of the fully developed path: E1 CRM Entity, _P1 is identified by (identifies)_, E41 Appellation, _P2 has type_, E55 Type
            file.write("## Examples: " + '\n\n')  # e.g. "## Scope note"
            if row[9] != "":
                file.write("* " + row[9] + '\n\n')  # e.g. book is identified by an ISBN number
            else:
                file.write("* todo" + '\n\n')  # e.g. book is identified by an ISBN number
            file.write("## In First Order Logic: " + '\n\n')  # e.g. "## In First order Logic:"
            file.write(row[10] + '\n' + row[11] +'\n' + row [12] + '\n\n')  # e.g. TP1(x,y) ⇒ E1(x)	TP1(x,y) ⇒ E55(y)	TP1(x,y) ⇔ (∃ z)[E41(z) ∧ P1(x,z) ∧ P2(z,y)]
            file.close()
        # NTP property
        if row[15] != "":
            file = open("source/" + row[15].lower() + ".md", "w")
            file.write("# " + row[15] + " " + row[16] + '\n\n') # e.g. "# TP56 bears feature of type (is type of feature found on)"
            file.write("## Domain: " + '\n\n') # e.g. "# Domain:"
            file.write(row[2] + " " + row[3] + '\n\n') # e.g. "E19 Physical Thing"
            file.write("## Range: " + '\n\n') # e.g. "## Range:"
            file.write("E55 Type" + '\n\n') # always E55
            file.write("## Superproperty of: " + '\n\n')  # e.g. "## Superproperty of"
            file.write("todo" + '\n\n')  # e.g. todo manually
            file.write("## Subproperty of: " + '\n\n')  # e.g. "## Subproperty of"
            file.write("todo" + '\n\n')  # e.g. todo manually
            file.write("## Quantification: " + '\n\n')  # e.g. "## Quantification"
            file.write("todo" + '\n\n')  # e.g. todo manually
            file.write("## Scope note: " + '\n\n')  # e.g. "## Scope note"
            file.write("scope note goes here" + '\n\n')  # e.g. This property is a shortcut of the fully developed path: E1 CRM Entity, _P1 is identified by (identifies)_, E41 Appellation, _P2 has type_, E55 Type
            file.write("## Examples: " + '\n\n')  # e.g. "## Scope note"
            if row[17] != "":
                file.write("* " + row[17] + '\n\n')  # e.g. book is identified by an ISBN number
            else:
                file.write("* todo" + '\n\n')  # e.g. book is identified by an ISBN number
            file.write("## In First Order Logic: " + '\n\n')  # e.g. "## In First order Logic:"
            file.write(row[18] + '\n' + row[19] + '\n\n')  # e.g. TP1(x,y) ⇒ E1(x)	TP1(x,y) ⇒ E55(y)	TP1(x,y) ⇔ (∃ z)[E41(z) ∧ P1(x,z) ∧ P2(z,y)]
            file.close()