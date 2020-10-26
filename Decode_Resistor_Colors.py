def decode_resistor_colors(bands):
    res = {'black':'0', 'brown':'1', 'red':'2', 'orange':'3', 'yellow':'4',
           'green':'5', 'blue':'6', 'violet':'7', 'grey':'8', 'white':'9'}

    code = bands.split("")

    print(code)
    print(int(res[code[0]] + res[code[1]]) *(10 ** int(res[code[2]]))

    power = int(res[code[0]] + res[code[1]]) *(10 ** int(res[code[2]]))

    if power < 1000:
        output = str(power) + ' ohms, '
    elif power < 1000000:
        if (int(power/1000) == float(power/1000)):
            output = str(int(power/1000)) + 'k ohms, '
        else:
            output = str(float(power/1000000)) + 'M ohms, '
    else:
        if int(power/10000000) == float(power/1000000):
            output = str(int(power/1000000)) + 'M ohms, '
        else:
            output = str(float(power/1000000)) + 'M ohms, '

    if len(code) == 3:
        output += ('20%')
    else:
        output += (res[code[3]] + '%')
    return output

