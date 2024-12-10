import pandas as pd
from termcolor import colored
from pprint import pprint

FILE_TO_MAKE_ANALYSIS = 'just_use_sublime.csv'

tournaments_data = pd.read_csv(FILE_TO_MAKE_ANALYSIS, sep='\t', encoding='utf8')

# coluna das localizações dos torneios
tournaments_line_numbers = tournaments_data.iloc[:, 0]

# print(tournaments_line_numbers)

numbers_to_check = [int(str(i).zfill(4)) for i in range(1, 8318)]
# print(numbers_to_check)  # This will print: ['0001', '0002', ..., '8317']


for number in numbers_to_check:
    if number in tournaments_data.values:

        count = (tournaments_line_numbers == number).sum()
        if count > 1:
            print(f"{number}: {count}")


for number in numbers_to_check:
    if number not in tournaments_data.values:
        print(f"{number} Não está no ficheiro")

