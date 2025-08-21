# Classe base para publicações
# A intenção é que esta classe seja só herdada, e não usada para criar objetos diretamente
class Publicacoes:

    # Construtor da classe
    def __init__(self):
        
        self._ano = 0
        self._nome_conferencia_periodico = ""
        self._titulo = ""
        self._autores = ""
        self._edicao = 0
        self._pagina_inicial = 0
        self._pagina_final = 0
        self._fator_de_impacto = 0.0

    # --- Setters ---

    def set_ano (self, novo_ano):
        self._ano = novo_ano

    def set_nome_conferencia_periodico (self, novo_nome):
        self._nome_conferencia_periodico = novo_nome

    def set_titulo (self, novo_titulo):
        self._titulo = novo_titulo

    def set_autores (self, novos_autores):
        self._autores = novos_autores

    def set_edicao (self, nova_edicao):
        self._edicao = nova_edicao

    def set_pagina_inicial (self, nova_pag):
        self._pagina_inicial = nova_pag

    def set_pagina_final (self, nova_pag):
        self._pagina_final = nova_pag

    def set_fator_de_impacto (self, novo_fi):
        self._fator_de_impacto = novo_fi

    # --- Getters ---

    def get_ano (self):
        return self._ano

    def get_nome_conferencia_periodico (self):
        return self._nome_conferencia_periodico

    def get_titulo (self):
        return self._titulo

    def get_autores (self):
        return self._autores

    def get_edicao (self):
        return self._edicao

    def get_pagina_inicial (self):
        return self._pagina_inicial

    def get_pagina_final (self):
        return self._pagina_final

    def get_fator_de_impacto (self):
        return self._fator_de_impacto

    # Este método vai ser sobrescrito pelas classes "filhas" então ele não vai fazer nada aqui.
    def get_pontos (self):
    
        pass
