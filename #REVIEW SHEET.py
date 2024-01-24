#REVIEW SHEET 
#Question 1 = English to piglatin 

def getPigLatin(pigStr):
    pigList = pigStr.split() # convert string variable pigStr to a list pigList
    pigLatin = []
    for x in pigList:
        if len(x) > 1:
            word = x[1:] + x[0] + 'ay'
        else: 
            word = x + 'ay'
        pigLatin.append(word)
    return ' '.join(pigLatin)
    
def main_PigLatin():
    message = input('Please enter a sentence:')
    print(getPigLatin(message))

main_PigLatin()


#Question 2 
location = input('Enter lcoation of shipping package:')
weight = input('Enter weight of the package:')
def calculate_cost(location, weight):
    if weight <= 2.0
        charge = 1.50 * weight
        print(charge)
    elif weight <= 6 
        charge = 3.00 * weight 
        print(charge)

