print()
perguntas = {
    'Pergunta1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {'a':'4','b':'8','c':'10'},
        'resposta_certa': 'a'
    },
    'Pergunta2': {
        'pergunta': 'Quanto é 6+3?',
        'respostas': {'a':'5','b':'13','c':'9'},
        'resposta_certa': 'c'
    },
    'Pergunta3': {
        'pergunta': 'Quanto é 3*2?',
        'respostas': {'a':'5','b':'6','c':'9'},
        'resposta_certa': 'b'
    },
}

certas = 0

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    for rk, rv in pv['respostas'].items():
        print(f'{rk}: {rv}')
    resposta = input('Qual a resposta correta?')
    if resposta == pv['resposta_certa']:
        print('Parabéns! Você ACERTOU!')
        certas += 1
    else:
        print('Opaaa! Você ERROU!')
print(f'Você acertou {certas} respostas em um total de {len(perguntas)} perguntas')