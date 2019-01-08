import sys

def populate(table):
    td = "<td>\n" \
         "  <h4>{0}</h4>\n" \
         "  <ul style='list-style-type:none'>\n" \
         "      <li>#{1}</li>\n" \
         "      <li class='symbol'>{2}</li>\n" \
         "      <li>{3}</li>\n" \
         "  </ul>\n" \
         "</td>\n"

    special="<td>\n" \
            "   <h4>{0}</h4>\n" \
            "   <h4>{1}</h4>\n" \
            "</td>\n"

    row="</tr>\n" \
        "<tr>\n"

    space = "<td id='space' colspan='{0}'></td>\n"

    colspan = [1, 4, 12, 56, 88]
    lant = range(57,72)
    act = range(89,104)
    col = [1, 1, 10, 10, 16]
    str_lant = ""
    str_act = ""

    with open("mendeleiv.html", "a") as file:
        for atom, data in table.items():
            cel = td.format(atom, data['number'], data['small'], data['molar'])
            number = int(data['number'])
            if number in colspan:
                file.write(cel+space.format(col.pop()))
                """       elif number in lant:
                          str_lant += cel
                          if number == 57:
                              file.write(special.format('Lantanides', '*'))
                      elif number in act:
                          str_act += cel
                          if number == 89:
                              file.write(special.format('Actinides', '**'))
                """
            else:
                file.write(cel)
                if int(data['position']) == 17:
                    file.write(row)
        """
        file.write(space.format(3)+str_lant+row+space.format(3)+str_act+"</tr>\n</table></body>")
        """
        file.write("</tr>\n</table></body>")
        file.close()

def txt_to_dict():
    table = {}
    with open("periodic_table.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            temp = line.strip().split('=')
            data = dict(item.strip().split(':') for item in temp[1].split(','))
            table.update({temp[0] : data})
    file.close()
    populate(table)

def add_headers():
    with open("mendeleiv.html", "w") as file:
        file.write("<!DOCTYPE html>\n"
                   "<html lang='fr-FR'>\n"
                   "<head>"
                   "    <title>Mendeleiv</title>\n"
                   "    <meta charset='UTF-8'>\n"
                   "    <style>\n"
                   "        table { border-collapse:collapse;width:80%;}\n"
                   "        td {border:1px solid black;text-align:center;width:5vw;min-width:5.3vw;}"
                   "        li {font-size:0.7vw;}"
                   "        h4 {font-size:0.8vw;}"
                   "        .symbol {font-weight:bold;}"
                   "    </style>"
                   "</head>\n"
                   "<body>\n"
                   "    <table>"
                   "        <tr>")
        file.close()

if __name__ == "__main__":
    add_headers()
    txt_to_dict()
