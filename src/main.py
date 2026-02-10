import os
from control.cauculo import ProcessoCauculo
import model.conexaoBancoSqlite

os.system('cls')

#Criando a conexão com o banco de dados SQLite
conexaoSqlite = model.conexaoBancoSqlite

#Entrada de dados--------------------------------------------------------
faturamento=float(input("INFORME O VALOR DO FATURAMENTO: "))
custo=float(input("INFORME O VALOR DE CUSTO: "))

# Instanciando o objeto ProcessoCauculo e calculando o lucro
processoCauculo=ProcessoCauculo(faturamento,custo)

# Realizar o Cauculo do Lucro.
lucroCauculado=processoCauculo.caucularLucro()

# Realizar o Registro de Cauculo em Banco de Dados.
conexaoSqlite.registrarRelatorio(faturamento,custo,lucroCauculado)

#Saída de Dados------------------------------------------------------------
print('''\nLUCRO: ''',lucroCauculado)
