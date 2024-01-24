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
location = input('Enter lcoation of shipping package, Domestic/International:')
weight = input('Enter weight of the package:')
def calculate_cost(location, weight):
    if weight <= 2.0:
        if location.lower() == 'domestic':
            return weight * 1.50 
        elif location.lower() == 'international':
            return weight * 5.00 
    elif weight <= 6.00:
        if location.lower() == 'domestic':
            return 3.00 * weight 
        elif location.lower() == 'international':
            return weight * 10 
    elif weight <= 10.00:
        if location.lower() == 'domestic':
             return weight * 1.50 
        elif location.lower() == 'international':
            return weight * 15.00
    else: 
        if location.lower() == 'domestic':
            return 4.75 * weight
        elif location.lower() == 'international':
            return 25 * weight 
     

## Q3 
def withdrawlAmount(balance, withdrawl_amount):
   balance = withdrawl_amount
   return balance

def depositAmount(balance, deposit_amount):
     balance += deposit_amount
     return balance

def main():
    message = "start"
    current_balance = float(input("current balance:"))

    while message != "quit ":
        message = input("please enter type of transaction 'quit', 'withdrawl','deposit'")
        if message.lower() == 'withdrawl':
            withdraw = float(input("what is the amount:"))
            if withdraw <= current_balance:
                withdrawlAmount(current_balance, withdraw)
            else:
                print("please reenter withdrawl lower than your $.")

        elif message.lower == 'deposit':
            update_amount = float(input('How much do you want to deposit'))
            current_balance= depositAmount(current_balance,update_amount)
        print(current_balance)
    


