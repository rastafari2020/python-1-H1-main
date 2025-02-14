"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    i = 0
    while len(result) <=5:
        for i in range(6):
            result.append(i)
    result.reverse()
    print(result)
    return result
    

fn_hack_7()