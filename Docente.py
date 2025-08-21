class Docente:

    # Construtor da classe
    def __init__(self):

        self._codigo = 0  
        self._nome = ""
        self._data_nascimento = ""  # Armazenada como string para manter o formato dd/mm/aaaa
        self._data_ingresso = ""    # Armazenada como string para manter o formato dd/mm/aaaa
        self._ocorrencia = None # Em vez de um ponteiro, usamos None (é o equivalente a nullptr)
        self._publicacoes = []

        # Atributos para a fase de recredenciamento
        self._pontuacao = 0.0
        self._status_recredenciamento = ""

    # --- Setters ---

    def set_codigo  (self, novo_codigo):
        self._codigo = novo_codigo

    def set_nome (self, novo_nome):
        self._nome = novo_nome

    def set_data_nascimento (self, nova_data_nasc):
        self._data_nascimento = nova_data_nasc

    def set_data_ingresso (self, nova_data_ingr):
        self._data_ingresso = nova_data_ingr

    def set_ocorrencia (self, nova_ocorrencia):
        self._ocorrencia = nova_ocorrencia

    def set_publicacoes (self, novas_publicacoes):
        self._publicacoes = novas_publicacoes

    def set_pontuacao (self, nova_pontuacao):
        self._pontuacao = nova_pontuacao

    def set_status_recredenciamento (self, novo_status):
        self._status_recredenciamento = novo_status

    # --- Getters ---

    def get_codigo (self):
        return self._codigo

    def get_nome (self):
        return self._nome

    def get_data_nascimento (self):
        return self._data_nascimento

    def get_data_ingresso (self):
        return self._data_ingresso

    def get_ocorrencia (self):
        # Retorna o objeto Ocorrencia associado, ou None se não houver.
        return self._ocorrencia

    def get_publicacoes (self):
        # Retorna a lista de publicações do docente.
        return self._publicacoes

    def get_num_publicacoes (self):
        # Retorna o número de publicações associadas ao docente.
        return len(self._publicacoes)

    def get_pontuacao (self):
        return self._pontuacao

    def get_status_recredenciamento (self):
        return self._status_recredenciamento