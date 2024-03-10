import csv

def count_by_state(rests, upper):   
    if upper == 'US':
       num1 = 0
       for values in rests.values():
           num1 += 1
    else:   
        num1 = 0
        for values in rests.values():
            if upper == values[0]:
                num1 += 1       
    return num1

def count_by_style(rests, lower):
    if lower == 'any':
       num2 = 0
       for values in rests.values():
           num2 += 1
    else:   
        num2 = 0
        for values in rests.values():
            if lower == values[1]:
                num2 += 1   
    return num2

def avg_by_state(rests, upper):
    sum1 = 0
    num4 = 0
    for values in rests.values():    
        if upper == values[0] or upper == 'US':
            sum1 += float(values[2])
            num4 += 1
            num3 = sum1 / num4
                   
    return num3

def avg_by_style(rests, lower):
    sum2 = 0
    num5 = 0
    for values in rests.values():
        if lower == values[1] or lower == 'any':
            sum2 += float(values[2])
            num5 += 1
            num6 = sum2 / num5            
        
    return num6

def print_lowest_revenue(rests):
    num7 = 999999.0
    for ID in rests.keys():
        if float(rests[ID][-1]) < float(num7):
            lowID = ID  
            lowRev2 = float(rests[ID][-1])
            lowStyle = rests[ID][-2]
            lowState = rests[ID][-3]
            num7 = lowRev2
    print(f'Lowest Revenue: Restaurant {lowID} in {lowState}, {lowStyle} style, had ${lowRev2:.2f}')
                

###########################################################################################################
# This is where your main program will start.  Do not change these two lines, and remember that you need 
# to indent all of your code one level to fall under the if.
# 
if __name__ == '__main__':
    
    # below is a list containing all of the valid state abbreviations in the United States
    States = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
              "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
              "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
              "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
              "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
              
    
    # all of your code for your main program goes here, indented to this level.  Code in this 
    # section will call the functions defined above.
    Styles = ['dine in', 'express', 'truck']
    
    States.append('US')
    Styles.append('any')
    
    file_name = input('Enter the filename of the file containing restaurants data:\n')
    
    f = open(file_name, 'r')
    csvfile = csv.reader(f, delimiter=',')
    
    first_row = True
    rests = {}
    for i in csvfile:
        if first_row:
            first_row = False
            continue
        
        rests.update({i[0] : [i[1], i[2], i[3]]})
       
    user_input = 0
    
    while user_input != 6:
        
        print('(1) Get the number of restaurants by state')
        print('(2) Get the number of restaurants by style')
        print('(3) Get the average revenue of restaurants by state')
        print('(4) Get the average revenue of restaurants by restaurant style')
        print('(5) Print restaurant with lowest revenue')
        print('(6) Exit')
        user_input = int(input('Enter a selection 1-6:\n'))
        
        if user_input == 1:
            state = input('Enter a 2 letter state abbreviation, or \'US\' for all restaurants in the U.S.:\n')
            upper = state.upper()
            while upper not in States:
                print(f'{state} is not a valid state abbreviation')
                state = input('Enter a 2 letter state abbreviation, or \'US\' for all restaurants in the U.S.:\n')
                upper = state.upper()
                
            if upper in States:            
                count = count_by_state(rests, upper)
                print(f'There are {count} Sparty Burger Restaurants in {upper}') 
            
        elif user_input == 2:
            style = input('Enter the restaurant style, or \'any\' for all styles:\n')
            lower = style.lower()
            while lower not in Styles:
                print(f'{style} is not a valid restaurant style')
                style = input('Enter the restaurant style, or \'any\' for all styles:\n')
                lower = style.lower()
                
            if lower in Styles:
                count = count_by_style(rests, lower)
                print(f'There are {count} Sparty Burger {lower} style restaurants')
        
        elif user_input == 3:
            state = input('Enter a 2 letter state abbreviation, or \'US\' for all restaurants in the U.S.:\n')
            upper = state.upper()
            while upper not in States:
                print(f'{state} is not a valid state abbreviation')
                state = input('Enter a 2 letter state abbreviation, or \'US\' for all restaurants in the U.S.:\n')
                upper = state.upper()
                
            if upper in States:            
                avg = avg_by_state(rests, upper)
                print(f'The average revenue in {upper} is ${avg:.2f}')
            
        elif user_input == 4:
            style = input('Enter the restaurant style, or \'any\' for all styles:\n')
            lower = style.lower()
            while lower not in Styles:
                print(f'{style} is not a valid restaurant style')
                style = input('Enter the restaurant style, or \'any\' for all styles:\n')
                lower = style.lower()
                
            if lower in Styles:
                avg = avg_by_style(rests, lower)
                print(f'The average revenue of {lower} style restaurants is ${avg:.2f}')
            
        elif user_input == 5:
            lowRev = print_lowest_revenue(rests)
            # print(f'Lowest Revenue: Restaurant IDK in {lowRev[0]}, {lowRev[1]} style, had ${float(lowRev[2]):.2f}')
            
        elif user_input == 6:
            Exit = 'yes'
            
        else:
            print('Invalid selection - must be a number from 1 to 6')
            
    f.close()
