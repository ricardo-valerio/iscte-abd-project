import pandas as pd
from termcolor import colored
from pprint import pprint

FILE_TO_READ = 'Nomes em Opponent (excepto bye e os casos especiais de 7 nomes).csv'
FILE_TO_READ_2 = 'Nomes e Links__COMPLETO__FINAL.csv'

nomes_no_atributo_opponent = pd.read_csv(FILE_TO_READ, sep='\t', encoding='utf8')
nome_e_links_data = pd.read_csv(FILE_TO_READ_2, sep='\t', encoding='utf8')



FILE_TO_GENERATE = "queries_to_update_LinkOpponents_que_restam.js"
# FILE_TO_GENERATE = "links_dos_oponents_para_pesquisar_info.csv"

import os
if os.path.exists(FILE_TO_GENERATE):
    os.remove(FILE_TO_GENERATE)


f = open(FILE_TO_GENERATE, "a", encoding="utf-8")


nomes_de_oponents_nao_encontrados = list()

opponents_not_found_counter = 0

for nome_em_opponent in nomes_no_atributo_opponent.itertuples(index=True):

    opponent_found = False

    # print(f"[{nome_em_opponent.Index + 1}] {nome_em_opponent.Name}")

    for nome_e_link in nome_e_links_data.itertuples(index=True):

        if nome_em_opponent.Name == nome_e_link.Name:
            opponent_found = True
            # print(f"[{nome_em_opponent.Index + 1}]  {nome_em_opponent.Name}  ==  {nome_e_link.Name}  [{nome_e_link.Index + 1}]")

            print(f"------- mongo query para {nome_em_opponent.Index + 1} {nome_em_opponent.Name}")

            mongodb_query = 'db.atpplayers.updateMany(\n'                                     \
                            '    // filter\n'                                                 \
                            '    {\n'                                                         \
                            f'       "Opponent": "{nome_e_link.Name}"\n'                      \
                            '    },\n\n'                                                      \
                            '    // set command\n'                                            \
                            '    { "$set":\n'                                                 \
                            '      {\n'                                                       \
                            f'        "LinkOpponent": "{nome_e_link.Link}"\n'                 \
                            '      }\n'                                                       \
                            '    }\n'                                                         \
                            ')\n\n\n'                                                         \

            print(mongodb_query)

            f.write(f"{mongodb_query}\n")

            f.write(f"{nome_e_link.Name}\t{nome_e_link.Link}\n")

            continue

    if not opponent_found:
        print(colored(f"Não conseguimos encontrar [{nome_em_opponent.Index}]{nome_em_opponent.Name}", "red"))
        opponents_not_found_counter += 1
        nomes_de_oponents_nao_encontrados.append(nome_em_opponent.Name)


f.close()

print("\n\n --------------------------------------")
print(f"opponents not found: {opponents_not_found_counter}")
print(f"Nomes dos oponentes não encontrados: {nomes_de_oponents_nao_encontrados}")

print("Para ver os comandos mongodb gerados ver o ficheiro:", FILE_TO_GENERATE)

