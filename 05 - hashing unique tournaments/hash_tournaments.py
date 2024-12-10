import pandas as pd
from termcolor import colored
from pprint import pprint
import hashlib


FILE_TO_READ = 'atpplayers_tournaments_to_hash.csv'

tournaments_data = pd.read_csv(FILE_TO_READ, sep='\t', encoding='utf8')

FILE_TO_GENERATE = "tournaments_hashes.js"

# import os
# if os.path.exists(FILE_TO_GENERATE):
#     os.remove(FILE_TO_GENERATE)


f = open(FILE_TO_GENERATE, "a", encoding="utf-8")

for tournament in tournaments_data.itertuples(index=True):


    tournament_name = tournament.Name
    tournament_location = tournament.Location
    tournament_date = tournament.Date
    string_to_hash = f"{tournament.Name}{tournament_location}{tournament.Date}"

    print(
        f"Linha: {tournament.Index + 1} ----------------------------------\n"
        f"Name: {tournament_name}\t"
        f"Name: {tournament_location}\t"
        f"Date: {tournament_date}\t"
        f"Hash_MD5 of '{tournament.Name}{tournament_location}{tournament.Date}': {hashlib.md5(string_to_hash.encode()).hexdigest()}",
    )


    f.write(f"{hashlib.md5(string_to_hash.encode()).hexdigest()}\n")


    # for player in players_data.itertuples(index=True):

    #     # player_name = player.Name
    #     # player_link = player.Link

    #     # print(
    #     #     f"Linha: {player.Index + 1} ------------------------------------------------------------------------------------\n"
    #     #     f"Name: {player_name}, "
    #     #     f"Link: {player_link}, "
    #     # )

    #     if tournament.Name.lower() in player.Name.replace("-", " ").lower():
    #         opponent_found = True
    #         print(f"[{tournament.Index}]{tournament.Name}  ==  {player.Name}[{player.Index}]")
    #         s.write(f"{player.Name}\t{player.Link}\n")

    # if not opponent_found:
    #     print(colored(f"Não conseguimos encontrar [{tournament.Index}]{tournament.Name}", "red"))
    #     opponents_not_found_counter += 1

    #     # inserir num ficheiro os nomes para dps ir procurar os links
    #     f.write(f"[{tournament.Index}] - {tournament.Name}\n")






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



#     f.write(f"{mongodb_query}")

f.close()
