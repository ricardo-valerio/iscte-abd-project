import pandas as pd
from termcolor import colored
from pprint import pprint

FILE_TO_READ = 'opponents_links.csv'

opponents_data = pd.read_csv(FILE_TO_READ, sep='\t', encoding='utf8')

FILE_TO_GENERATE = "queries_to_update_LinkOpponent.js"

import os
if os.path.exists(FILE_TO_GENERATE):
    os.remove(FILE_TO_GENERATE)


f = open(FILE_TO_GENERATE, "a", encoding="utf-8")


for player in opponents_data.itertuples(index=True):

    player_name = player.Name
    player_link = player.Link

    # print(
    #     f"Linha: {player.Index + 1} ------------------------------------------------------------------------------------\n"
    #     f"Name: {player_name}, "
    #     f"Link: {player_link}\n"
    # )
    # exit()

    print(f"------- query para a linha: {player.Index + 1} -----------------------------------------------")
    mongodb_query = 'db.atpplayers.updateMany(\n'                                     \
                    '    // filter\n'                                                 \
                    '    {\n'                                                         \
                    f'       "Opponent": "{player_name}"\n'                           \
                    '    },\n\n'                                                      \
                    '    // set command\n'                                            \
                    '    { "$set":\n'                                                 \
                    '      {\n'                                                       \
                    f'        "LinkOpponent": "{player_link}"\n'                      \
                    '      }\n'                                                       \
                    '    }\n'                                                         \
                    ')\n\n\n'                                                         \


    # print(mongodb_query)

    f.write(f"{mongodb_query}")

f.close()
