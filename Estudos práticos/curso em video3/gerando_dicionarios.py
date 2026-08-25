# Exercício Python 105: Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar
# um dicionário com as seguintes informações:
    # – Quantidade de notas
    # – A maior nota
    # – A menor nota
    # – A média da turma 
    # – A situação (opcional)

def notas(*n, sit = False):
    ''' -> Função para analisarr notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar situação.
    :return: Dicionário com várias infromações sobre a situação da turma.
    '''
    alunos_notas = {}

    alunos_notas['total'] = len(n)
    alunos_notas['maior'] = max(n)
    alunos_notas['menor'] = min(n)
    alunos_notas['média'] = sum(n) / len(n)

    if sit:
        if alunos_notas['média'] >= 7:
            alunos_notas['situação'] = 'BOA'
        elif alunos_notas['média'] >= 5:
            alunos_notas['situação'] = 'RAZOÁVEL'
        else:
            alunos_notas['situação'] = 'RUIM'
            
    return alunos_notas


# Programa Principal
resp = notas(5.5,9.5,1,6.5,sit=True)
print(resp)
help(notas)