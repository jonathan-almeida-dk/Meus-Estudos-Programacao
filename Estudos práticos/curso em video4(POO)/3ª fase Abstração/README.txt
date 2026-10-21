ABSTRAÇÃO

A prática de ignorar o irrelevante e se focar estritamente no essencial!

PRINCIPAIS VANTAGENS:
- Maior legibilidade
- Padronização
- Simplificação
- Segurança

ABSTRAÇÃO DE DADOS:
    Existe abstração de dados, que acontece quando
    ignoramos informações desnecessárias para o escopo do projeto.

ABSTRAÇÃO DE PROCESSOS:
    Existe a abstração de processos, quando não precisamos saber como um
    método faz seu trabalho, apenas sabe que ele existe pela interface.

Uma classe abstrata nunca será instanciada, já que ela
será usada apenas como base para as subclasses.

Ao defenir um conjunto de métodos abstratos,
dizemos que estamos criando a interface pública da classe.

Uma classe abstrata pode ter métodos abstratos que deverão
ser obrigatoriamente implemnetados nas subclasses.

Mas uma classe abstrata pode ter métodos concretos se eles
funcionaram da mesma maneira para todas a subclasses(DRY).

==========================================================================

CONTROLE GENÉRICO <--- Classe Abstrata (mãe)
    + ligar()
    + desligar()
    + aumentar_volume()       <------ MÉTODOS ABSTRATOS (abstract) # são exclusivos da Classe Abstrata
    + diminuir_volume()
    + avancar_canal()
    + retroceder_canal()

CONTROLE GENÉRICO <--- Classe Abstrata (mãe)
    CONTROLE 1   |
    CONTROLE 2   |
    CONTROLE 3   | <----- Classes Filhas ou  Classe Especializada
    CONTROLE 4   |
    CONTROLE 5   |