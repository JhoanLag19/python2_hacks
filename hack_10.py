"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s

    for i in range(len(result)):
        diccionarioNuevo = {}
        for key, value in result[i].items():
            claveNueva = str(i * 2 + 1)
            valorNuevo = str(i * 2 + 2)
            diccionarioNuevo[claveNueva] = valorNuevo
        result[i] = diccionarioNuevo
    return result
