class Ocorrencia:

    # Construtor da classe
    def __init__(self):

        self._codigo_docente = 0
        self._evento = ""
        self._data_inicio = ""
        self._data_fim = ""

    # --- Setters ---

    def set_codigo_docente (self, novo_codigo):
        self._codigo_docente = novo_codigo

    def set_evento (self, novo_evento):
        self._evento = novo_evento

    def set_data_inicio (self, nova_data_inicio):
        self._data_inicio = nova_data_inicio

    def set_data_fim (self, nova_data_fim):
        self._data_fim = nova_data_fim

    # --- Getters ---

    def get_codigo_docente (self):
        return self._codigo_docente

    def get_evento (self):
        return self._evento

    def get_data_inicio (self):
        return self._data_inicio

    def get_data_fim (self):
        return self._data_fim