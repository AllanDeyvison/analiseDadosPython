import pandas as pd
import plotly.express as px

table = pd.read_csv("telecom_users.csv")
table = table.drop("Unnamed: 0", axis=1)
table = table.drop("IDCliente", axis=1)
table["TotalGasto"] = pd.to_numeric(table["TotalGasto"], errors="coerce")
table = table.dropna(how="all", axis=1)
table = table.dropna(how="any", axis=0)

def opcoesDeGraficos(coluna):
    print("Opções de colunas:")
    for i, col in enumerate(coluna):
        print(f"{i+1}. {col}")

    while True:
        try:
            escolha = int(input("Digite o número da coluna para gerar o gráfico: "))
            if escolha < 1 or escolha > len(coluna):
                raise ValueError
            else:
                grafico = px.histogram(table, x=coluna[escolha - 1], color="Churn")
                grafico.show()
                break
        except ValueError:
            print("Opção inválida. Digite o número correspondente à coluna desejada.")

coluna = table.columns.tolist()

opcoesDeGraficos(coluna)
