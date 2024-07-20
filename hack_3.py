"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    result = s
    reemplazos = {
        'a': '@',
        'e': '3',
        'i': '¡',
        'o': '0',
        'u': 'v'
    }
    
    for clave, valor in reemplazos.items():
        result = result.replace(clave, valor)
    
    if len(result) > 1:
        if len(result) == 2 and result[1] in reemplazos.values():
            result = result[0].upper() + result[1]
        else:
            result = result[0].upper() + result[1:-1] + result[-1].upper()
    elif len(result) == 1:
        result = result.upper()
    
    return result
