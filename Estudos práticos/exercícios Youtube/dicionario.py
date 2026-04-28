# informacoes do jogador
player = {
    "nome": "Jonathan",
    "level": 1,
    "hp": 100,
    "exp": 0,
    "dano": 5,
}
print (player['nome'])
print (player['level'])
print (player['hp'])
print (player['exp'])
print (player['dano'])

# lista de inimigos
npcs = [
    { "Name": "Monstrinho", "Dano": 2, "HP": 50, "EXP": 5 },
    { "Name": "Monstro", "Dano": 5, "HP": 100, "EXP": 10 },
    { "Name": "Monstrão", "Dano": 10, "HP": 150, "EXP": 15 },
    { "Name": "CHEFÃO", "Dano": 25, "HP": 200, "EXP": 20 },
    ]
for inimigo in npcs:
    print(inimigo['Name'])
    print(inimigo['Dano'])
    print(inimigo['HP'])
    print(inimigo['EXP'])

