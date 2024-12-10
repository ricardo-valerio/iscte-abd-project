import pandas as pd
from termcolor import colored
from pprint import pprint

FILE_TO_READ = 'nomes a faltar por ter link no atributo LinkOpponent.csv'
FILE_TO_READ_2 = 'Nomes e Links__COMPLETO.csv'

opponents_data = pd.read_csv(FILE_TO_READ, sep='\t', encoding='utf8')
players_data = pd.read_csv(FILE_TO_READ_2, sep='\t', encoding='utf8')

# FILE_TO_GENERATE = "queries_to_update_LinkOpponent_2.js"

# import os
# if os.path.exists(FILE_TO_GENERATE):
#     os.remove(FILE_TO_GENERATE)


#  f = open(FILE_TO_GENERATE, "a", encoding="utf-8")

e = open("nomes_a_faltar_que_deram_erro.txt", "a", encoding="utf-8")

# s = open("nomes_correspondidos.txt", "a", encoding="utf-8")



opponents_not_found_counter = 0


counter = 1
for opponent in opponents_data.itertuples(index=True):

    print(colored(f"======================================= [{counter}] ========================================", "green"))
    counter += 1

    opponent_found = False

    opponent_name = opponent.Name

    # print(
    #     f"Linha: {opponent.Index + 1} ------------------------------------------------------------------------------------\n"
    #     f"Name: {opponent_name}"
    # )


    for player in players_data.itertuples(index=True):

        player_name = player.Name
        player_link = player.Link

        # print(
        #     f"Linha: {player.Index + 1} ---------------------------------------------------------------------------\n"
        #     f"Name: {player_name}, "
        #     f"Link: {player_link}, "
        # )

        if opponent.Name == player.Name:
            opponent_found = True
            print(f"[{opponent.Index}]{opponent.Name}  ==  {player.Name}[{player.Index}]")
            # s.write(f"{player.Name}\t{player.Link}\n")
            continue

    if not opponent_found:
        print(colored(f"Não conseguimos encontrar [{opponent.Index}]{opponent.Name}", "red"))
        opponents_not_found_counter += 1

        # inserir num ficheiro os nomes para dps ir procurar os links
        e.write(f"[{opponent.Index}] - {opponent.Name}\n")




e.close()
# s.close()

print("\n\n --------------------------------------")
print(f"opponents not found: {opponents_not_found_counter}")





    # print(f"------- query para a linha: {player.Index + 1} -----------------------------------------------")
    # mongodb_query = 'db.atpplayers.updateMany(\n'                                     \
    #                 '    // filter\n'                                                 \
    #                 '    {\n'                                                         \
    #                 f'       "Opponent": "{player_name}"\n'                           \
    #                 '    },\n\n'                                                      \
    #                 '    // set command\n'                                            \
    #                 '    { "$set":\n'                                                 \
    #                 '      {\n'                                                       \
    #                 f'        "LinkOpponent": "{player_link}"\n'                      \
    #                 '      }\n'                                                       \
    #                 '    }\n'                                                         \
    #                 ')\n\n\n'                                                         \


    # print(mongodb_query)

#     f.write(f"{mongodb_query}")

# f.close()
