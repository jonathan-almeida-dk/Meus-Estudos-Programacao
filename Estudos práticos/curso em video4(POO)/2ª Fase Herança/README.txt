HERANÇA

É um relacionamento entre 'itens gerais' (ancestrais) e 
'tipos mais específicos' (descendentes) desses itens, 
que herdam 'atributos' e 'métodos' de níveis superiores.

PRINCIPAIS VANTAGENS:
- Reutilização de código
- Organização hierárquica
- Facilita manutenção
- Extensibilidade (Altera um ancestral, todos os que herdam serão alterados)
- Suporte a polimorfismo
=======================================
SuperClasse
    Classe Base
    Ancestral
    Classe Mãe

Herança
    Generalização
    Relação tipo "é um "

SubClasse
    Classe Derivada
    Descendente
    Classe Filha

========================================

Classe Pessoa 🧍‍♂️(Genérica) <----- Classe Abstrata
    + nome
    + idade 
    + fazer_aniversário() 
    + estudar() {abstract}  <----- método concreto

    Classe Aluno 🧑‍🎓 <------ Classe Especializada
        + curso
        + turma
        + fazer_matricula()
        + estudar()

    Classe Professor 🧑‍🏫  <------ Classe Especializada
        + especialidade
        + nivel
        + dar_aula()
        + estudar()

    Classe Funcionário 👩‍💼  <------ Classe Especializada
        + cargo
        + setor
        + bater_ponto()
        + estudar()
