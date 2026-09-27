# QUESTÃO 19 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet(em MBps), calcule e informe o tempo aproximado de download do arquivo usando este link(em minutos).

arquivo = float(input('Tamanho de um arquivo para download em MB: '))
velocidade = float(input('Velocidade de um link de Internet em MBps: '))
tempo = ((arquivo*8)/velocidade)/60
print('O tempo aproximado de download do arquivo usando este link em minutos é de', tempo,)