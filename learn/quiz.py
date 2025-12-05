
quess = ("whats capital frensh ?",
         "what the beggest contry by land ?",
         "what the beggest contry by people ?",
         "whats capital morocco ?",
         "whats the smartest in this fucking world ?")

options = ( ('A. AGADIR', 'B. MONACO', 'C. PARIS', 'D. MADRID'),
            ('A. Algerie', 'B. Russia', 'C. Morocco', 'D. china'),
            ('A. Algerie', 'B. Russia', 'C. Morocco', 'D. china'),
            ('A. RABAT', 'B. AGADIR', 'C. TANGER', 'D. MADRID'),
            ('A. Chadi', 'B. Hwawi', 'C. Oudra', 'D. Bomzwi'))

answers = ('C', 'B', 'D', 'A', 'A')
geusses = [ ]
score = 0 
num_que = 0

for question in quess:
    print('-------------------------------------------')
    print(question)
    for option in options[num_que]:
        print(option)

    geuss = input('Enter (A,B,C,D) :').upper()
    geusses.append(geuss)
    if geuss == answers[num_que]:
        score +=1
        print('CORRECT')
    else:
        print('INCORRECT')     
    print(score,'/ 5')
    num_que += 1    
