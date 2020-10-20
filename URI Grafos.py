# -*- coding: utf-8 -*-
"""
Arthur: Leandro Augusto Martins Gonçalves

Este é um arquivo de script temporário.
"""

matriz = {}
caminhos = []
T = int(input(2))

for i in range(T):
    var = 0
    while(var < 5):
        aux = input().split()
        if aux:
            matriz[var] = aux
            var += 1
            
            if (matriz[0][0] == '1'):
                print("ROBBERS")
                
            else: 
                resposta = "ROBBERS"
                caminhos.append([0,0])
                matriz[0][0] = 'x'
                
                for pos in caminhos:
                    cima = pos [0] - 1
                    baixo = pos [0] + 1
                    esq = pos [1] - 1
                    dir = pos [1] + 1
                    
                    if(cima > -1 and cima < 5):
                        if(matriz[cima][pos[1]] == '0'):
                            caminhos.append([cima, pos[1]])
                            matriz[cima][pos[1]] = 'x'
                            
                    if(baixo > -1 and baixo < 5):
                        if(matriz[baixo][pos[1]] == '0'):
                            caminhos.append([baixo, pos[1]])
                            matriz[baixo][pos[1]] = 'x'
                            
                    if(esq > -1 and esq < 5):
                        if(matriz[pos[0]][esq] == '0'):
                            caminhos.append([pos[0], esq])
                            matriz[pos[0]][esq] = 'x'
                            
                    if(dir > -1 and dir < 5):
                        if(matriz[pos[0]][dir] == '0'):
                            caminhos.append([pos[0], dir])
                            matriz[pos[0]][dir] = 'x'
                            
                    if([4, 4] in caminhos):
                        resposta = "COPS"
                        break
                    
                    print(resposta)
                    caminhos.clear()
                    matriz.clear()
                    

