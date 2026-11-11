from hashlib import *



class tabelahash:
    def _init_ (self,capacidade:int):
        self.capacidade = capacidade
        self.tabela = [[]for _ in range(capacidade)]

    def funcao_hash(self, chave:str):
        soma = sum(ord(c) for c in chave)
        return soma%self.capacidade
    
    def __repr__(self):
        texto = f"Tabela"
        for i in range(self.capacidade):
            texto = texto + f"\n{i} -> {self.tabela[i].__repr__()}"
        return texto

    def hash_usuario(self, usuario: str, senha:str):
        user_hash = self.funcao_hash(usuario)
        senha_hash = sha512(f"{usuario}{senha}".encode('utf-8')).hexdigest()
        for registro in self.tabela[user_hash]:
            if registro["usuario"] == usuario:
                registro["hash_senha"] = senha_hash
                return
        self.tabela[user_hash].append({'usuario': usuario, 'hash_senha': senha_hash})

    def delecao(self, usuario: str):
        indice = self.funcao_hash(usuario)
        self.tabela[indice]= None
