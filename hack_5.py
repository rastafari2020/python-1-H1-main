"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"

    remplazar = ('o','0'),('i','1'),('a','@')
        
    for a, b in remplazar:
        result = result.replace(a,b)
        
    print(result)    
    return result    

fn_hack_5()