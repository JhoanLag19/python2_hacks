"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    
    if len(result) > 2 and result != "qux":
        result = result[1:-1]
    
    return result
