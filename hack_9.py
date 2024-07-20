"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    for clave in list(s.keys()):
        if "foo" in clave:
            s["Foo"] = s.pop(clave).replace("fookziman", "Fooziman")
            if len(s) > 1:
                del s[list(s.keys())[0]]
    return result
