"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = s
    if result == [0]:
        return result
    i = 0
    while i < len(result):
        if i % 2 == 0:
            result[i] = str(i + 1)
        else:
            result[i] = i + 1
        i += 1
    return result
