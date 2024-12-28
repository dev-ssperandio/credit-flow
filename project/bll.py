import pandas as pd
import sqlite3


# Cria DataFrame inicial
def create_dataframe():
    data = {
        "id": [1, 2, 3],
        "name": ["Edelvita", "Ivanessa", "Sidney"],
        "cpf": ["123245678900", "98765432100", "45612378900"]
    }

    df = pd.DataFrame(data)

    print("DataFrame criado com sucesso.")

    return df

def save_dataframe_sqlite(df, database, table):
    try:
        with sqlite3.connect(database) as conn:
            df.to_sql(table, conn, if_exists="replace", index=False)
            print(f"Dados salvos na tabela '{table}' do banco de dados '{database}' com sucesso.")
        pass
    except Exception as e:
        print("Erro ao salvar no banco de dados: ", e)


# Função para realizar a análise dos dados
def analyze_data(df):
    print(f"\nAnálise dos dados: \nColunas: {df.columns}")
    print("Valores unicos por coluna: ")
    for column in df.columns:
        print(f"  {column}: {df[column].nunique()} únicos")

    print("\nInformações gerais: ")
    print(df.info())

    print("\nEstatística descritivas: ")
    print(df.describe())

def filter_by_name(df, name):
    df_filtered = df[df['name'].str.contains(name, case=False, na=False)]
    return df_filtered

def filter_by_cpf(df, cpf):
    df_filtered = df[df['cpf'].str.contains(cpf, case=False, na=False)]
    return df_filtered


class Costumer:
    def __init__(self, id, name, cpf):
        self.__id = id
        self.__name = name
        self.__cpf = cpf
        self.__cards = [] # Lista para armazenar os cartões do clieinte


    # Getter e Setters
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name == new_name

    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def cards(self):
        return self.__cards
    

    # Métodos
    def add_card(self, card):
        self.__cards.append(card)

    def reomove_card(self, card_number):
        self.__cards = [c for c in self.__cards if c.number != card_number]
        
    def __str__(self):
        return f"Cliente: {self.__name} \nCPF: {self.__cpf} \nCartões: {[c.number for c in self.__cards]}"


class CreditCard:
    def __init__(self, number, limit, costumer):
        self.__number = number
        self.__limit = limit
        self.__balance = limit # Saldo inicial igual ao limite
        self.__costumer = costumer


    # Getters e Setters
    @property
    def number(self):
        return self.__number
    
    @property
    def limit(self):
        return self.__limit
    
    @limit.setter
    def limit(self, new_limit):
        if new_limit >= self.__balance:
            self.__limit == new_limit
        else:
            raise ValueError("O novo limite deve ser superior ao saldo atual.")
        
    @property
    def balance(self):
        return self.__balance

    @property
    def costumer(self):
        return self.__costumer
    

    # Métodos
    def make_purchase(self, value):
        if value > self.__balance:
            raise ValueError("Saldo insuficiente para compra")
        self.__balance -= value

    def make_payment(self, value):
        if self.__balance + value > self.limit:
            raise ValueError("Pagamento superior ao limite do cartão.")
        self.__balance += value

    def __str__(self):
        return f"Cartão: {self.__number} \nLimite: {self.__limit} \nSaldo: {self.__balance} \nCliente: {self.__costumer.name}"
        