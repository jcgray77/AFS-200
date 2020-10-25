def countingCases (string): 
   
    uppercases = 0
    lowercases = 0
    for x in list(string):
        if x.isupper():
            uppercases += 1
        elif x.islower():
            lowercases += 1
    print("UpperCase Count: ", uppercases)
    print("LowerCase Count: ", lowercases)
    

countingCases("Tiggers are wonderful things!!!!")