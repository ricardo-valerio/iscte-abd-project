import pandas as pd
from termcolor import colored

TOURNAMENTS_AND_LOCATIONS_CSV_FILE = 'tournaments_and_locations.csv'
tournaments_data = pd.read_csv(TOURNAMENTS_AND_LOCATIONS_CSV_FILE, sep='\t', encoding='utf8')

COUNTRIES_AND_CODES_CSV_FILE = 'countries_net.csv'
countries_data = pd.read_csv(COUNTRIES_AND_CODES_CSV_FILE, sep=',', encoding='utf8')

# colunas com os nomes dos países
countries_names = countries_data.iloc[:, 0]

# coluna das localizações dos torneios
tournaments_locations = tournaments_data.iloc[:, 1]


# for country in countries_names:
#     print(colored(f"country: {country}", "yellow"))
#     for line, location in enumerate(tournaments_locations):
#         print(colored(f"location: {location}", "blue"))

#         if country.lower() in location.lower():
#             print(colored(f"Yup I found that country: {country} is in location - {location} (linha {line})", "green"))



import os
if os.path.exists("just_use_sublime.csv"):
    os.remove("just_use_sublime.csv")



for country in countries_data.itertuples(index=False):
    # country_name = country.Name  # Access the country name
    # country_code = country.Code  # Access the country code
    # print(f"Country: {country_name}, Code: {country_code}")

    for tournament in tournaments_data.itertuples(index=True):


        # tournament_name = tournament.Tournament
        # tournament_location = tournament.Location
        # print(f"Tournament: {tournament_name}, Location: {tournament_location}")

        if country.Name.lower() in tournament.Location.lower():
            # print(colored(f"[FOUND] {tournament.Index + 1} - country: {country.Name} is in location - {tournament.Location} of the tournament {tournament.Tournament}", "green"))

            f = open(file="just_use_sublime.csv", mode="a", encoding="utf-8")
            f.write(f"{str(tournament.Index + 1).zfill(4)}\t{tournament.Tournament}\t{tournament.Location}\t{country.Code}\n")
            f.close()
