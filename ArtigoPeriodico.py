# Importa a classe "mãe" 
from Publicacoes import Publicacoes

# A classe ArtigoPeriodico é definida entre parênteses para indicar
# que ela herda da classe Publicacoes.
class ArtigoPeriodico (Publicacoes):

    # Construtor da classe 
    def __init__(self):

        # Chama o construtor da classe mãe (Publicacoes) para garantir que todos os atributos herdados sejam inicializados.
        super().__init__()

        # Inicializa o atributo que é específico desta classe.
        self._volume_periodico = 0

    # --- Setter específico ---

    def set_volume_periodico (self, novo_volume):
        self._volume_periodico = novo_volume

    # --- Getter específico ---

    def get_volume_periodico (self):
        return self._volume_periodico

    # Sobrescrita do método get_pontos para calcular os pontos de acordo com a lógica específica de ArtigoPeriodico.
    def get_pontos (self):

        return self.get_fator_de_impacto() * 1.0    # Chama o método get_fator_de_impacto da classe mãe, multiplica por 1.0 e retorna o resultado