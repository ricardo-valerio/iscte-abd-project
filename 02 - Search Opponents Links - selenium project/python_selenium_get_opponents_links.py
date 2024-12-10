from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from termcolor import colored
import pandas as pd

import time
from pprint import pprint
from bs4 import BeautifulSoup

# FICHEIROS NECESSÁRIOS PARA O SCRIPT CORRER: ------------------------------------------------------------------
#
FILE_OPPONENTS_GOOGLE_SEARCH_QUERIES = "opponents_google_search_queries.txt"
# --------------------------------------------------------------------------------------------------------------


# FICHEIROS GERADOS --------------------------------------------------------------------------------------------
# ficheiro onde vão ficar as queries que vão ser geradas por este script à medida que vai recolhendo os dados
FILE_OPPONENTS_LINKS_FOUND = "opponents_links.txt"
#
FILE_LOG_ERROS = "log_erros.txt"
# --------------------------------------------------------------------------------------------------------------



START_LINE_NUMBER = int(input("Linha a começar no ficheiro de links? (1 por default (irá remover ficheiros existentes)): ") or 1)
IS_START_LINE_GREATER_THAN_ONE = True if START_LINE_NUMBER > 1 else False

if START_LINE_NUMBER == 1:
# queremos recomeçar tudo de novo portanto podemos apagar os ficheiros gerados
# -----------------------------------------------------------------------------
    import os

    if os.path.exists(FILE_OPPONENTS_LINKS_FOUND):
        os.remove(FILE_OPPONENTS_LINKS_FOUND)

    if os.path.exists(FILE_LOG_ERROS):
        os.remove(FILE_LOG_ERROS)
# ------------------------------------------------------------------------------


# driver = webdriver.Firefox() # or webdriver.Chrome()

with open(file=FILE_OPPONENTS_GOOGLE_SEARCH_QUERIES, mode="r", encoding="utf-8") as file:

    # # Process each line one by one
    if START_LINE_NUMBER > 1 and IS_START_LINE_GREATER_THAN_ONE:
        for _ in range(START_LINE_NUMBER - 1):
            next(file)
        IS_START_LINE_GREATER_THAN_ONE = False

    count = START_LINE_NUMBER



    for line in file:
        driver = webdriver.Firefox() # or webdriver.Chrome()

        # Strip newline or extra whitespace
        google_search_query = line.strip()

        if google_search_query:

            print(colored(f"\n[{count}]------- Processing link: {google_search_query} --------\n", "yellow"))

            driver.get(google_search_query)

            try:
                elem = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "#web_content_wrapper")
                    )
                )

                # time.sleep(120)

            except Exception as e:
                print(colored(f"erro na google search: {google_search_query}", "red"))
                f = open(FILE_LOG_ERROS, "a")
                f.write(f"{google_search_query}\n")
                f.close()
            else:

                link = driver.find_element(By.CSS_SELECTOR, '#web_content_wrapper')

                # print(link.get_attribute('innerHTML'))

                soup = soup = BeautifulSoup(link.get_attribute('innerHTML'), 'html.parser')

                # DEBUG -----------------------
                # print(soup.prettify())
                # ----------------------------


                list_with_possible_links = soup.find_all('a', {'href': re.compile(r'atptour.com/en/players/.*/overview$')})


                first_and_most_probable_link = None

                if len(list_with_possible_links) > 0:
                    first_and_most_probable_link = list_with_possible_links[0].get('href')

                # DEBUG ------------------------
                # pprint(list_with_possible_links)
                # ------------------------------


                if first_and_most_probable_link:
                    f = open(FILE_OPPONENTS_LINKS_FOUND, "a", encoding="utf-8")

                    with open(file="Opponents_sem_info_na_DB.txt", mode="r", encoding="utf-8") as opponents_names_file:
                        for _ in range(count - 1):
                            next(opponents_names_file)

                        current_name_at_this_line = opponents_names_file.readline().strip()
                        print(colored(f"[{current_name_at_this_line}] - {first_and_most_probable_link}", "green" ) )
                        f.write(f"{count} [{current_name_at_this_line}] - {first_and_most_probable_link}\n")
                    f.close()
                else:
                    f = open(FILE_LOG_ERROS, "a")

                    with open(file="Opponents_sem_info_na_DB.txt", mode="r", encoding="utf-8") as opponents_names_file:
                        for _ in range(count - 1):
                            next(opponents_names_file)

                        current_name_at_this_line = opponents_names_file.readline().strip()
                        print(colored(f"{count} [{current_name_at_this_line}] | query: {google_search_query}", "red"))
                        f.write(f"{count} [{current_name_at_this_line}]  | query: {google_search_query}\n")

                    f.close()

            finally:

                # # fechar a sessão do browser
                driver.close()

                count += 1



