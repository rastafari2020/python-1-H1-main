"""
loop: for [] output => [0,1,2,3,4,5]
"""

def fn_hack_6():
    result = []
    i = 0
    for i in range(6):
        result.append(i)
    print(result)
    return result

fn_hack_6()

