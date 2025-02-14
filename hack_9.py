"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    i = 1
    while i <= len(result):

        if i == 1:
            result.insert(i,"@")

        if i == 3:
            result.insert(i,"@")    
            

        if i == 5:
            result.insert(i,"@")

        i = i+1
    print(result)   
    return result

fn_hack_9()
