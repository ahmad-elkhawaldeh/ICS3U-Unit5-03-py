# !/usr/bin/env python3

# Created by: Ahmad El-khawaldeh
# Created on: Dec 2020
# This program gives you a percentage of your mark


# function to convert level to percentage
def percentage(level): # function definition
    if(level == '4+'): # if level is 4+
        result = (100+95)/2 
    elif(level == '4'): # if level is 4
        result = (94+87)/2
    elif(level == '4-'): # if level is 4-
        result = (80+86)/2
    elif(level == '3+'): # if level is 3+
        result = (77+79)/2
    elif(level == '3'): # if level is 3
        result = (73+76)/2
    elif(level == '3-'): # if level is 3-
        result = (70+72)/2
    elif(level == '2+'): # if level is 2+
        result = (67+69)/2
    elif(level == '2'): # if level is 2
        result = (63+66)/2
    elif(level == '2-'): # if level is 2-
        result = (60+62)/2
    elif(level == '1+'): # if level is 1+
        result = (57+59)/2
    elif(level == '1'): # if level is 1
        result = (53+56)/2
        
    elif(level == '1-'): # if level is 1-
        result = (50+52)/2
        
    elif(level == 'R'): # if level is R
        result = 49/2
        
    else: # if level is not valid
        result = -1 # store -1 to result
    print(" no valid level")
  
def main():
    level = input("Enter the level: ")
    print("The Percentage is: ", percentage(level))

if __name__ == "__main__":
   main()

    
