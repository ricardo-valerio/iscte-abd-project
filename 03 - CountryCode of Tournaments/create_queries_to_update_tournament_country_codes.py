import pandas as pd
from termcolor import colored
from pprint import pprint

FILE_TO_READ = 'tournaments_country_codes.csv'

tournaments_data = pd.read_csv(FILE_TO_READ, sep='\t', encoding='utf8')

FILE_TO_GENERATE = "queries_to_update_tournament_country_codes.js"

import os
if os.path.exists(FILE_TO_GENERATE):
    os.remove(FILE_TO_GENERATE)


f = open(FILE_TO_GENERATE, "a", encoding="utf-8")


for tournament in tournaments_data.itertuples(index=True):

    tournament_name = tournament.Name
    tournament_location = tournament.Location
    tournament_country_code = tournament.CountryCode
    # print(
    #     f"{tournament.Index + 1}------------------------------------------------------------------------------------\n"
    #     f"Tournament: {tournament_name}, "
    #     f"Location: {tournament_location}, "
    #     f"Country code: {tournament_country_code}, \n"
    # )

    print(f"------- query para a linha: {tournament.Index + 1} -----------------------------------------------")
    mongodb_query = 'db.atpplayers.updateMany(\n'                                     \
                    '    // filter\n'                                                 \
                    '    {\n'                                                        \
                    f'       "Tournament": "{tournament_name}",\n'                    \
                    f'       "Location": "{tournament_location}"\n'                    \
                    '    },\n\n'                                                     \
                    '    // set command\n'                                            \
                    '    { "$set":\n'                                                 \
                    '      {\n'                                                       \
                    f'        "TournamentCountryCode": "{tournament_country_code}"\n' \
                    '      }\n'                                                       \
                    '    }\n'                                                         \
                    ')\n\n\n'                                                         \


    # print(mongodb_query)

    f.write(f"{mongodb_query}")

f.close()
