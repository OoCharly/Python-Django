from django.shortcuts import render


def ex03(request):
    black = 0x000000
    blue = 0x0000FF
    red = 0xFF0000
    green = 0x00FF00
    colors = []
    i = 1
    while i < 51:
        color = {
            'black': "{0:0>6}".format(hex(black + 0x020202 * i).replace('0x', '')),
            'blue': "{0:0>6}".format(hex(blue + 0x020200 * i).replace('0x', '')),
            'green': "{0:0>6}".format(hex(green + 0x020002 * i).replace('0x', '')),
            'red': "{0:0>6}".format(hex(red + 0x000202 * i).replace('0x', '')),
        }
        colors.append(color)
        i += 1

    return render(request, 'ex03/table.html', {'colors': colors, 'black': 'Noir', 'blue': 'Bleu', 'red': 'Rouge', 'green': 'Vert'})

# Create your views here.
