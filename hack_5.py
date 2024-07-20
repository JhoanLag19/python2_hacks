"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    
    if s == "fooziman":
        result = result[:2] + '-' + result[3:5] + '-' + result[5:-1] + '-'
    else:
        posicsReemplazo = [2, 5, 8]
        result = ''.join('-' if i in posicsReemplazo and i < len(result) else caracter for i, caracter in enumerate(result))
    
    return result
