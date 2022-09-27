# IST 303
# Question 1

Men_round_of_16= {{"Victor": ["Novak DJokovic", "Roger Federer", "Rafael Nadal", "Sam Querrey", "Kei Nishikori", "Guido Pella", "David Goffin", "Roberto Bautista Agut"]}
{"Losers" : ["Ugo Humbert", : "Matteo Berrettini", : "Joao Sousa", : "Tennys Sandgren", : "Mikhail Kukushkin", "Milos Raonic", : "Fernando Verdasco", : "Benoit Paire"]},

}
Men_round_of_16= [{"victor": "Novak DJokovic", "loser": ""}],




{"Victor": ["Novak DJokovic", "Roger Federer",: "Rafael Nadal", : "Sam Querrey", : "Kei Nishikori", : "Guido Pella", : "David Goffin", : "Roberto Bautista Agut"]
"Losers" : ["Ugo Humbert", : "Matteo Berrettini", : "Joao Sousa", : "Tennys Sandgren", : "Mikhail Kukushkin", "Milos Raonic", : "Fernando Verdasco", : "Benoit Paire"]
}

women_round_of_16 = {"Victor": ["Shuai Zhang", "Elina Svitolina", "Alison Riske", "Barbora Strycova",
                                "Karolina Muchova", "Serena Williams", "Simona Halep", "Johanna Konta"],
                     "Loser": ["Dayana Yastremska", "Petra Martic", "Ashleigh Barty", "Elise Mertens",
Wimbeldon = [(men_round_of_16, women_round_of_16), (men_quarter_finals, women_quarter_finals), (men_semi_finals,
             women_semi_finals), (men_final, women_final)]

# Question 6
# Create keylist
#keylist = ["Victor", "Loser"]
#keylist = ["Victor", "Loser"]
# Create women list
$women = []

myList = [(men_round_of_16, women_round_of_16), (men_quarter_finals, women_quarter_finals), (men_semi_finals,
             women_semi_finals), (men_final, women_final)]
myIter = iter (women)
print("The list is : ", myList)
print("The elements in the iterator are:")
for i in myIter:
    print (i)

#for tup in Wimbeldon:
    #for i in range(len(keylist)):
        #for names in tup[1][keylist[i]]:
            #if names not in women and len(names) > 1:
               # women.append(names)
#for tup in Wimbeldon:
   # for i in range(len(keylist)):
       # for names in tup[1][keylist[i]]:
           # if names not in women and len(names) > 1:
              #  women.append(names)

# Question 7
#def tournament_round_games(tournament, category, round):
