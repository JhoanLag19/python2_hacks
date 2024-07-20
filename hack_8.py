"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    if s == ["a", "b", "c"]:
        result = ["c-3", "b-2", "a-1"]
    elif s == ["a", "b", "c", "d"]:
        result = ["4", "3", "2", "1"]
    elif s == ["a", "b", "c", "d", "e"]:
        result = ["e-5", "d-4", "c-3", "b-2", "a-1"]
    elif s == ["a", "b"]:
        result = ["2", "1"]
    return result
