def cenario(msg):
    print('-' * 54)
    print(msg)
    print('-' * 54)
 
 #adicionar função inicial e termino
 
 
    while True:
        try:
            escolha = int(input('Digite qual em parte da aventura você está:\n1-SOMA DAS PEÇAS DO MAPA \n2-VERIFICAR SE VOCÊ TEM RECURSOS O SUFICIENTE ATÉ A CAVERNA \n3-CONTAR QUANTOS PASSOS FALTAM ATÉ A CAVERNA \n4-DIVIDIR O TESOURO COM OS SEUS COMPANHEIROS\n5-FINALIZAR A AVENTURA:'))

            if escolha == 1:
                print('Nessa Aventura, precisamos achar 10 pedaços do mapa para a caverna. Se acharmos mais de 10 peças, podemos vender ela para conseguir alguns trocados, cada peça vale 32 dobrões.')
                pecas1 = int(input('Digite quantas peças do mapa você achou:')) #pecas = peças(por algum motivo, o python não identifica o Ç)
                pecas2 = int(input('Digite quantas peças seus companheiros acharam:'))
                soma = pecas1 + pecas2 
 
                if soma == 10:
                    print(f'Você achou {pecas1} peças do mapa, e os seus companheiros acharam {pecas2} peças, no total deu {soma} peças, conseguimos todas as peças do mapa.\n')
                elif soma >= 11:
                	total_de_pecas_do_mapa = pecas1 - 10
                	dobroes_ganho = total_de_pecas_do_mapa * 32
                	print(f'Você conseguiu pegar {total_de_pecas_do_mapa} peça(s) à mais, como recompensa você conseguiu {dobros_ganho} no total. Meus parabéns.')
                else:
                    print('Caracter inválido, digite apenas números.\n')
                    
            elif escolha == 3: 
                passos1 = 500
                passos2 = int(input('Digite quantos passos você já deu, no mapa diz que devemos dar 500 passos para chegar lá: '))
                subt = passos1 - passos2
 
                if subt < passos1:
                    print(f'Você deu {passos2} passos, no mapa dizia {passos1} passos, ou seja, faltam {subt} passos para chegar até a caverna.\n')
                elif subt >= passos1:
                    print(f'Bem, depois de {subt} passos, conseguimos chegar á Caverna, dizem que existe um tesouro com até 100.000 Dobrões.\n')
                   
            elif escolha == 2:
                comida_nece = int(input('Digite qual é a quantidade de comida que você tem:')) 
                comida_consumida = int(input('Quantas refeições você faz por dia: '))
                dias  = 500
                calc = comida_nece * comida_consumida #calc = calcular.
                if calc < dias:
                    print(f'Você tem {comida_nece} porções de comida e come {comida_consumida} vezes por dia({calc} no total), mas pela quantidade de dias({dias}), isso vai ser pouco.\n')
                elif calc >= dias:
                    print(f'Você tem {comida_nece} porções de comida e come {comida_consumida} vezes por dia,ou seja, juntando a quantidade de comida e quantas vezes você come, no total vai ser {calc}, pela quantidade de dias(que é {dias} dias) você conseguirá chegar sem fome.\n')
                else:
                    print('ERRO: caracter inválido\n')
            
            elif escolha == 4:
                try:
                    tesouro = float(input('Digite qual é a quantidade de Dobrões que tem nesse tesouro(100 até 100.000):'))
                    calc = tesouro / 5 #calc = calcular/cálculo 
 
                    print(f'O tesouro tem {tesouro} Dobrões, dividindo para seus companheiros, fica {calc:,.2f} Dobrões para cada.\n')
                   
                except:
                    print('ERRO: caracter Inválido\n')
 
            elif escolha == 5:
                print('CHEGAMOS NO FINAL DESSA AVENTURA, ATÉ A PRÓXIMA AVENTURA MARUJO ;)')
                break
 
        except:
            print('Erro: caracter inválido\n')
 
cenario(' BEM-VINDO MARUJO, VOCÊ ESTÁ NO MUNDO Nº 1.9.0')