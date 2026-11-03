'''
the horse want to wear 4 different cloured hoursehuoue

he wants to spend minimum for party 

we have to find number of horsehoue we need to buy to make all colour different 
'''

'''
Example Input :
    1 7 3 3
Example Output:(number of more colours we need to but)
    1
'''


# Simple Approach just count the unique number of colours the horse has 

def horseColour(colours):
    s=set()
    for col in colours:
        s.add(col)
    return 4-len(s)

print(horseColour([1,7,3,3]))