from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from termcolor import colored
import pandas as pd


# FICHEIROS NECESSÁRIOS PARA O SCRIPT CORRER: ------------------------------------------------------------------
#
# ficheiro que tem os links dos jogadores presentes na BD de mongo (9960 no total)
FILE_DISTINCT_PLAYER_LINKS = "distinct_player_links_of_erros.txt"
#
# ficheiro onde vão ficar as queries que vão ser geradas por este script à medida que vai recolhendo os dados
FILE_MONGODB_QUERIES_GENERATED = "mongodb_queries_from_selenium_players_names_com_erros.js"
#
# ficheiro que o professor sugeriu no enunciado
FILE_COUNTRY_WITH_COUNTRY_CODES = "countries_net.csv"
# --------------------------------------------------------------------------------------------------------------
#
# carregar já o csv com esses country codes
df = pd.read_csv(FILE_COUNTRY_WITH_COUNTRY_CODES)


# FICHEIROS DE LOG QUE SERÃO GERADO PELO SCRIPT (servem para registar eventuais erros que captura de dados que possam ocorrer): ---------
#
# por exemplo um link inválido
FILE_LOG_ERROS_DE_LINKS = "log_de_erros_dos_player_links.txt"
#
# para registar países para os quais não foi possível associar um country code e será necessário verificar manualmente depois mais tarde
FILE_LOG_ERROS_COUNTRY_CODE_NAO_ENCONTRADO = "log_de_erros_paises_nao_encontrados.txt"
#---------------------------------------------------------------------------------------------------------------------------------------


START_LINE_NUMBER = int(input("Linha a começar no ficheiro de links? (1 por default (irá remover ficheiros existentes)): ") or 1)
IS_START_LINE_GREATER_THAN_ONE = True if START_LINE_NUMBER > 1 else False

# if START_LINE_NUMBER == 1:
# # queremos recomeçar tudo de novo portanto podemos apagar os ficheiros gerados
# # -----------------------------------------------------------------------------
#     import os

#     if os.path.exists("log_de_erros_paises_nao_encontrados.txt"):
#         os.remove("log_de_erros_paises_nao_encontrados.txt")

#     if os.path.exists("log_de_erros_dos_player_links.txt"):
#         os.remove("log_de_erros_dos_player_links.txt")

#     if os.path.exists("mongodb_queries_from_selenium.js"):
#         os.remove("mongodb_queries_from_selenium.js")
# # ------------------------------------------------------------------------------


def get_country_code(country_name, playerlink):

    result = df[df['Name'].str.lower() == country_name.lower()]

    if not result.empty:
        print(f"Código de {country_name}: {result['Code'].values[0]}")
        return result['Code'].values[0]
    else:
        f = open(file=FILE_LOG_ERROS_COUNTRY_CODE_NAO_ENCONTRADO, mode="a")
        if country_name != "NA":
            print(colored(f"{country_name} não encontrado.", "red"))
            f.write(f"{country_name}\n")
        else:
            print(colored(f"{country_name} significa - não existente no registo do jogador.", "red"))
            f.write("null\n")
        f.close()

        return None



with open(file=FILE_DISTINCT_PLAYER_LINKS, mode="r", encoding="utf-8") as file:

    # # Process each line one by one
    if START_LINE_NUMBER > 1 and IS_START_LINE_GREATER_THAN_ONE:
        for _ in range(START_LINE_NUMBER - 1):
            next(file)
        IS_START_LINE_GREATER_THAN_ONE = False

    count = START_LINE_NUMBER

    for line in file:
        # Strip newline or extra whitespace
        link_original = line.strip()
        # link = f"{link_original.split('/player-activity?')[0]}/overview"
        link = link_original

        if link:
            print(colored(f"\n[{count}]------- Processing link: {link} --------\n", "yellow"))
            count+=1

            driver = webdriver.Firefox() # or webdriver.Chrome()

            driver.get(link)

            try:
                elem = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "body > div.container > div > div.atp_layout > div > div.atp_layout-content > div.atp_player-personaldetails > div > div > ul.pd_right > li:nth-child(1) > span.flag")
                    )
                )
            except Exception as e:
                print(colored(f"erro no link: {link}", "red"))
                f = open(FILE_LOG_ERROS_DE_LINKS, "a")
                f.write(f"{link}\n")
                f.close()
            else:
                # Country --------------------------------------------------------------------------------------------------

                country = driver.find_element(By.CSS_SELECTOR, 'body > div.container > div > div.atp_layout > div > div.atp_layout-content > div.atp_player-personaldetails > div > div > ul.pd_right > li:nth-child(1) > span.flag').text

                if country.strip() == "":
                    country = "NA"

                # Birthplace -----------------------------------------------------------------------------------------------

                birthplace = driver.find_element(By.CSS_SELECTOR, 'body > div.container > div > div.atp_layout > div > div.atp_layout-content > div.atp_player-personaldetails > div > div > ul.pd_right > li:nth-child(2) > span:nth-child(2)').text.strip()

                if birthplace == "":
                    birthplace = "NA"



                # Plays ----------------------------------------------------------------------------------------------------

                plays = driver.find_element(By.CSS_SELECTOR, 'body > div.container > div > div.atp_layout > div > div.atp_layout-content > div.atp_player-personaldetails > div > div > ul.pd_right > li:nth-child(3) > span:nth-child(2)').text

                if plays.strip() == "":
                    plays = "NA"




                # Height --------------------------------------------------------------------------------------------------

                height = driver.find_element(By.CSS_SELECTOR, 'body > div.container > div > div.atp_layout > div > div.atp_layout-content > div.atp_player-personaldetails > div > div > ul.pd_left > li:nth-child(3) > span:nth-child(2)').text

                # extrair apenas os nºs da altura em cm
                match = re.search(r'\((\d+)cm\)', height)

                if match:
                    height = match.group(1)  # Extract the captured group
                    # print(f"Height in cm: {height}") # DEBUG
                else:
                    # print("No height found.") # DEBUG
                    height = "NA"


                # Country Code -------------------------------------------------------------------------------------------
                country_code = get_country_code(country_name=country, playerlink=link)


                print("country:", country)
                print("country_code:", country_code)
                print("birthplace:", birthplace)
                print("plays:", plays)
                print("height:", height)

                print("\n\n")

                # query para o mongodb -------------------------------------------------
                mongodb_query = 'db.atpplayers.updateMany(\n'                     \
                                '    // filter\n'                                 \
                                f'    {{"LinkPlayer": "{link_original}"}},\n\n'   \
                                '    // set command\n'                            \
                                '    { "$set":\n'                                 \
                                '      {\n'


                if height == "NA":
                    mongodb_query += f'        "Height": "{height}",\n'
                else:
                    mongodb_query += f'        "Height": {height},\n'


                if country.lower() in birthplace.lower():
                    mongodb_query += f'        "Born": "{birthplace}",\n'
                else:
                    if birthplace == "NA":
                        mongodb_query += f'        "Born": "{country}",\n'
                    else:
                        mongodb_query += f'        "Born": "{birthplace}, {country}",\n'


                if country_code is not None:
                    mongodb_query += f'        "BornCountryCode": "{country_code}",\n'
                else:
                    mongodb_query += f'        "BornCountryCode": null,\n'

                mongodb_query += f'        "Hand": "{plays}"\n'                    \
                                 '      }\n'                                       \
                                 '    }\n'                                         \
                                 ')\n\n\n'                                         \
                # ------------------------------------------------------------------------

                print(colored(mongodb_query, "green"), "\n\n")

                f = open(file=FILE_MONGODB_QUERIES_GENERATED, mode="a")
                f.write(f"{mongodb_query}")
                f.close()

            finally:
                # fechar a sessão do browser
                driver.close()




