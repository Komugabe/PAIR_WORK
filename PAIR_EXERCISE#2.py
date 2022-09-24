# MARIA ASSUMPTA
# IST 303
# Question 1

Men_round_of_16= {"Victor": ["Novak DJokovic", "Roger Federer",: "Rafael Nadal", : "Sam Querrey", : "Kei Nishikori", : "Guido Pella", : "David Goffin", : "Roberto Bautista Agut"]
"Losers" : ["Ugo Humbert", : "Matteo Berrettini", : "Joao Sousa", : "Tennys Sandgren", : "Mikhail Kukushkin", "Milos Raonic", : "Fernando Verdasco", : "Benoit Paire"]
}
women_round_of_16 = {"Victor": ["Shuai Zhang", "Elina Svitolina", "Alison Riske", "Barbora Strycova",
                                "Karolina Muchova", "Serena Williams", "Simona Halep", "Johanna Konta"],
                     "Loser": ["Dayana Yastremska", "Petra Martic", "Ashleigh Barty", "Elise Mertens",
                               "Karolina Pliskova", "Carla Suarez-Narvarro", "Cori Gauff", "Petra Kvitova"]}

 # Question 2
men_quarter_finals = {"Victor": ["Novak Djokovic", "Roger Federer", "Rafael Nadal", "Roberto Bautista Agut"],
                   "Loser": ["David Goffin", "Kei Nishikori", "Sam Querrey", "Guido Pella"]}
women_quarter_finals = {"Victor": ["Serena Williams", "Simona Halep", "Elina Svitolina", "Barbora Strycova"],
                     "Loser": ["Alison Riske", "Shuai Zhang", "Karolina Muchova", "Johanna Konta"]}
# Question 2
men_quarter_finals = {"Victor": ["Novak Djokovic", "Roger Federer", "Rafael Nadal", "Roberto Bautista Agut"],
                   "Loser": ["David Goffin", "Kei Nishikori", "Sam Querrey", "Guido Pella"]}
women_quarter_finals = {"Victor": ["Serena Williams", "Simona Halep", "Elina Svitolina", "Barbora Strycova"],
                     "Loser": ["Alison Riske", "Shuai Zhang", "Karolina Muchova", "Johanna Konta"
 # Question 4
men_final = {"Victor": "Novak Djokovic",
             "Loser": "Roger Federer"}
women_final = {"Victor": "Simona Halep ",
             "Loser": "Serena Williams"}

# Question 5
Wimbeldon = [(men_round_of_16, women_round_of_16), (men_quarter_finals, women_quarter_finals), (men_semi_finals,
             women_semi_finals), (men_final, women_final)]

# Question 6
# Create keylist
keylist = ["Victor", "Loser"]
# Create women list
women = []

for tup in Wimbeldon:
    for i in range(len(keylist)):
        for names in tup[1][keylist[i]]:
            if names not in women and len(names) > 1:
                women.append(names)

# Question 7
def tournament_round_games(tournament, category, round):
    """
    This function takes 3 parameters, a list with the tournament information (in our case, Wimbeldon), a string category (men or women)
    and a string round (round of 16, quarter finals, semi finals, or finals) and returns the players of that
    category and round in the tournament
    :param tournament: list
    :param category: string
    :param round: string
    :return: dictionary of winners and losers in the specified category and round of the tournament
    """

    # variable for category
    cat = None
    # variable for round
    rnd = None

    # Determine category
    if category == "Men" or category == "men":
        cat = 0
    elif category == "Women" or category == "women":
        cat = 1

    # Determine round
    if round == "round of 16":
        rnd = 0
    elif round == "quarter finals":
        rnd = 1
    elif round == "semi finals":
        rnd = 2
    elif round == "finals":
        rnd = 3
    else:
        print("Round not found please retry entry with 'round of 16', "
              "'quarter finals', 'semi finals', or 'finals'")

    if rnd is not None and cat is not None:
        return tournament[rnd][cat]
    else:
        print("Please retry search")
        return {}

# Test
print(tournament_round_games(Wimbeldon, "Men", "finals"))
print(tournament_round_games(Wimbeldon, "Women", "quarter finals"))