import pandas as pd
from termcolor import colored
from pprint import pprint

FILE_TO_READ = 'atpplayers_tournaments_to_hash.csv'

tournaments_data = pd.read_csv(FILE_TO_READ, sep='\t', encoding='utf8')

FILE_TO_GENERATE = "queries_to_update_tournament_ids.js"

# import os
# if os.path.exists(FILE_TO_GENERATE):
#     os.remove(FILE_TO_GENERATE)


f = open(FILE_TO_GENERATE, "a", encoding="utf-8")



for tournament in tournaments_data.itertuples(index=True):

    tournament_name = tournament.Name
    tournament_location = tournament.Location
    tournament_date = tournament.Date
    tournament_hash_id = tournament.Hash


    # print(colored(f"======= [{tournament.Index + 1}] =============", "green"))
    # print(
    #     f"Name: {tournament_name} |"
    #     f"Date: {tournament_date} |"
    #     f"Hash: {tournament_hash_id} \n\n"
    # )


    print(f"------- query para a linha: {tournament.Index + 1} -----------------------------------------------")

    mongodb_query = 'db.atpplayers.updateMany(\n'                                     \
                    '    // filter\n'                                                 \
                    '    {\n'                                                         \
                    f'       "Tournament": "{tournament_name}",\n'                    \
                    f'       "Location": "{tournament_location}",\n'                  \
                    f'       "Date": "{tournament_date}"\n'                           \
                    '    },\n\n'                                                      \
                    '    // set command\n'                                            \
                    '    { "$set":\n'                                                 \
                    '      {\n'                                                       \
                    f'        "TournamentId": "{tournament_hash_id}"\n'               \
                    '      }\n'                                                       \
                    '    }\n'                                                         \
                    ')\n\n\n'

    f.write(f"{mongodb_query}")


f.close()
