import pandas as pd
import sqlite3
from bll import create_dataframe, save_dataframe_sqlite, analyze_data, filter_by_name, filter_by_cpf
from tabulate import tabulate


if __name__ == "__main__":
    # Caminho banco de dados e nome da tabela
    database = "project/database/dados_bancarios.db"
    table = "costumers"

    # Criar DataFrame inicial
    df_costumers = create_dataframe()

    # Salvar no banco de dados SQLite
    save_dataframe_sqlite(df_costumers, database, table)


    # Coletar os dados novamente do banco de dados simulando a coleta real
    with sqlite3.connect(database) as conn:
        df_customers_collected = pd.read_sql_query(f"SELECT * FROM {table}", conn)

    # Analisar os dados coletados
    analyze_data(df_customers_collected)

    # Filtrar clientes por nome
    searched_name = "Sidney"
    df_filtered_name = filter_by_name(df_customers_collected, searched_name)
    print(f"\nClientes encontrados com o nome '{searched_name}':")
    print(df_filtered_name)
    
    # Filtrar clientes por cpf
    searched_cpf = "98765432100"
    df_filtered_cpf = filter_by_cpf(df_customers_collected, searched_cpf)
    print(f"\nClientes encontrados com CPF {searched_cpf}: ")
    print(df_filtered_cpf)

    # Exibindo os dados filtrados por CPF com Tabulate
    print("\nExibindo os dados filtrados por CPF com Tabulate:")
    print(tabulate(df_filtered_cpf, headers="keys", tablefmt="grid"))
