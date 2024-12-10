from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from termcolor import colored
import pandas as pd
import os

import time
from pprint import pprint
from bs4 import BeautifulSoup

# FICHEIROS NECESSÁRIOS PARA O SCRIPT CORRER: ------------------------------------------------------------------
#
FILE_OPPONENTS = "Nomes e Links__COMPLETO.csv"
# ----------------------------------------------------------------


opponents_data = pd.read_csv(FILE_OPPONENTS, sep='\t', encoding='utf8')



# FICHEIROS GERADOS --------------------------------------------------------------------------------------------
FILE_LOG_ERROS = "log_erros_a_abrir_o_link_no_browser.txt"
FILE_LOG_ERROS_NOMES = "players_com_nomes_que_nao_batem_certo.txt"
# ------------------------------------------------------------------------------------------



START_LINE_NUMBER = int(input("Linha a começar no ficheiro de links? (1 por default (irá remover ficheiros existentes)): ") or 1)
IS_START_LINE_GREATER_THAN_ONE = True if START_LINE_NUMBER > 1 else False

if START_LINE_NUMBER == 1:
# queremos recomeçar tudo de novo portanto podemos apagar os ficheiros gerados
# -----------------------------------------------------------------------------
    if os.path.exists(FILE_LOG_ERROS):
        os.remove(FILE_LOG_ERROS)

    if os.path.exists(FILE_LOG_ERROS_NOMES):
        os.remove(FILE_LOG_ERROS_NOMES)
# ------------------------------------------------------------------------------




for opponent in opponents_data.itertuples(index=True):

    # # Process each line one by one
    if START_LINE_NUMBER > 1 and IS_START_LINE_GREATER_THAN_ONE:
        if opponent.Index + 1 < START_LINE_NUMBER:
            continue
        else:
            IS_START_LINE_GREATER_THAN_ONE = False


    opponent_name = opponent.Name
    opponent_link = opponent.Link

    # print(
    #     f"Linha: {opponent.Index + 1} ---------------------------------------------------------------------------\n"
    #     f"Name: {opponent_name}, "
    #     f"Link: {opponent_link}, "
    # )






    driver = webdriver.Firefox() # or webdriver.Chrome()


    link_original = opponent_link

    link = f"{link_original.split('/player-activity?')[0]}/overview"


    if link:

        print(colored(f"\n[{opponent.Index + 1}]------- Processing link: {link} --------\n", "yellow"))

        driver.get(link)

        try:
            elem = WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, "body > div.atp_player-profile-header > div > div > div.player_profile > div.player_name > span")
                        )
                    )

        except Exception as e:
            print(colored(f"erro no link: {link}", "red"))
            f = open(FILE_LOG_ERROS, "a")
            f.write(f"[{opponent_name}] - {link}\n")
            f.close()
        else:

            player_name_in_web_page = driver.find_element(By.CSS_SELECTOR, 'body > div.atp_player-profile-header > div > div > div.player_profile > div.player_name > span').text


            # strip every space
            player_name_in_web_page = str.strip( re.sub( " +", " ", player_name_in_web_page ) )
            opponent_name = str.strip( re.sub( " +", " ", opponent_name ) )


            if opponent_name.lower() == player_name_in_web_page.lower():
                print(f"{opponent_name} == {player_name_in_web_page}")
            else:
                print(colored(f"{opponent_name} != {player_name_in_web_page}", "red"))
                f = open(FILE_LOG_ERROS_NOMES, "a")
                f.write(f"{opponent_name} vs {player_name_in_web_page}  ==>  {link}\n")
                f.close()



        finally:
            # fechar a sessão do browser
            driver.close()



