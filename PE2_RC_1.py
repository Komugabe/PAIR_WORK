# from collections import Counter
#
# # Question 1
men_round_of_16 = [
    {"victor": "Novak DJokovic", "loser": "Ugo Humbert"},
    {"victor": "Roger Federer", "loser": "Matteo Berrettini"},
    {"victor": "Rafael Nadal", "loser": "Joao Sousa"},
    {"victor": "Sam Querrey", "loser": "Tennys Sandgren"},
    {"victor": "Kei Nishikori", "loser": "Mikhail Kukushkin"},
    {"victor": "Guido Pella", "loser": "Milos Raonic"},
    {"victor": "David Goffin", "loser": "Fernando Verdasco"},
    {"victor": "Roberto Bautista Agut", "loser": "Benoit Paire"}
]
women_round_of_16 = [
    {"victor": "Shuai Zhang", "loser": "Dayana Yastremska"},
    {"victor": "Elina Svitolina", "loser": "Petra Martic"},
    {"victor": "Alison Riske", "loser": "Ashleigh Barty"},
    {"victor": "Barbora Strycova", "loser": "Elise Mertens"},
    {"victor": "Karolina Muchova", "loser": "Karolina Pliskova"},
    {"victor": "Serena Williams", "loser": "Carla Suarez-Narvarro"},
    {"victor": "Simona Halep", "loser": "Cori Gauff"},
    {"victor": "Johanna Konta", "loser": "Petra Kvitova"}
]

# # Question 2
men_quarter_finals = [
    {"victor": "Novak DJokovic", "loser": "David Goffin"},
    {"victor": "Roger Federer", "loser": "Kei Nishikori"},
    {"victor": "Rafael Nadal", "loser": "Sam Querrey"},
    {"victor": "Roberto Bautista Agut", "loser": "Guido Pella"}
]
women_quarter_finals = [
    {"victor": "Serena Williams", "loser": "Alison Riske"},
    {"victor": "Simona Halep", "loser": "Shuai Zhang"},
    {"victor": "Elina Svitolina", "loser": "Karolina Muchova"},
    {"victor": "Barbora Strycova", "loser": "Johanna Konta"}
]

# # Question 3
men_semi_finals = [
    {"victor": "Novak DJokovic", "loser": "Rafael Nadal"},
    {"victor": "Roger Federer", "loser": "Roberto Bautista Agut"}
]
women_semi_finals = [
    {"victor": "Serena Williams", "loser": "Elina Svitolina"},
    {"victor": "Simona Halep", "loser": "Barbora Strycova"}
]

#  # Question 4
men_final = [
    {"victor": "Novak DJokovic", "loser": "Roger Federer"}
]
women_final = [
    {"victor": "Simona Halep", "loser": "Serena Williams"}
]

# # Question 5
#
wimbledon = {
    "M": men_round_of_16,
    "M": men_quarter_finals,
    "M": men_semi_finals,
    "M": men_final,
    "F": women_round_of_16,
    "F": women_quarter_finals,
    "F": women_semi_finals,
    "F": women_final
}
# #print(wimbledon)
# # Question 6
# # Using a for iterator, create a list of all the women that played in the Wimbledon
# # tournament. Ensure that a player is shown once and only once. Assign this list to
# # the variable women.
# # tournament = wimbledon, category = men or women, and round = round of 16, quarter finals, finals
women = {}

for key, values in wimbledon.items():
    if key == 'F':
        print(values)

    # if key == "F":
    #     for value2 in values.items():
        # for key3, value3 in value2.items():
        #     for item in value3:
        #         women.add(item)
            #print(value2)
#
#
#     for key2, value in values.items():
#         if key2 == 'F':
#             for item in value:
#                 f_animal.add(item)
# print(women)
#
#
#

women = set()
for match in women_round_of_16:
  for key, value in match.items():
    women.add(value)
print(women)