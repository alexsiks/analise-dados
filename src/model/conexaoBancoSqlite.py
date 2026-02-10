import sqlite3
from datetime import datetime

class ConexaoBancoSqlite:
    def __init__(self, caminho_banco="src/model/Banco.db"):
        self.caminho_banco = caminho_banco
        self.conn = None
    
    def conectar(self):
        """Cria conexão e inicializa a tabela de relatório"""
        self.conn = sqlite3.connect(self.caminho_banco)
        self._criar_tabela()
        return self.conn
    
    def _criar_tabela(self):
        """Cria a tabela de relatório se não existir"""
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS relatorio(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dataVenda DATETIME,
                faturamento REAL,
                custo REAL,
                lucro REAL
            )
        ''')
        self.conn.commit()
    
    def registrar_relatorio(self, faturamento, custo, lucro):
        """Insere um novo relatório no banco"""
        if not self.conn:
            self.conectar()
        
        self.conn.execute('''
            INSERT INTO relatorio (dataVenda, faturamento, custo, lucro)
            VALUES (datetime('now'), ?, ?, ?)
        ''', (faturamento, custo, lucro))
        self.conn.commit()
    
    def fechar(self):
        """Fecha a conexão com o banco"""
        if self.conn:
            self.conn.close()
    
    def __enter__(self):
        self.conectar()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fechar()
