#EXEMPLO DE COMO DEVE SER:
#Bem-vindo ao detector automático de COH-PIAH.
#Informe a assinatura típica de um aluno infectado:
#Entre o tamanho médio de palavra: 4.51
#Entre a relação Type-Token: 0.693
#Entre a Razão Hapax Legomana: 0.55
#Entre o tamanho médio de sentença: 70.82
#Entre a complexidade média da sentença: 1.82
#Entre o tamanho médio de frase: 38.5
#Digite o texto 1 (aperte enter para sair): Num fabulário ainda por encontrar será um dia lida esta fábula: A uma bordadora dum país longínquo foi encomendado pela sua rainha que bordasse, sobre seda ou cetim, entre folhas, uma rosa branca. A bordadora, como era muito jovem, foi procurar por toda a parte aquela rosa branca perfeitíssima, em cuja semelhança bordasse a sua. Mas sucedia que umas rosas eram menos belas do que lhe convinha, e que outras não eram brancas como deviam ser. Gastou dias sobre dias, chorosas horas, buscando a rosa que imitasse com seda, e, como nos países longínquos nunca deixa de haver pena de morte, ela sabia bem que, pelas leis dos contos como este, não podiam deixar de a matar se ela não bordasse a rosa branca. Por fim, não tendo melhor remédio, bordou de memória a rosa que lhe haviam exigido. Depois de a bordar foi compará-la com as rosas brancas que existem realmente nas roseiras. Sucedeu que todas as rosas brancas se pareciam exactamente com a rosa que ela bordara, que cada uma delas era exactamente aquela. Ela levou o trabalho ao palácio e é de supor que casasse com o príncipe. No fabulário, onde vem, esta fábula não traz moralidade. Mesmo porque, na idade de ouro, as fábulas não tinham moralidade nenhuma.
#Digite o texto 2 (aperte enter para sair): Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres. 
#Digite o texto 3 (aperte enter para sair): Senão quando, estando eu ocupado em preparar e apurar a minha invenção, recebi em cheio um golpe de ar; adoeci logo, e não me tratei. Tinha o emplasto no cérebro; trazia comigo a idéia fixa dos doidos e dos fortes. Via-me, ao longe, ascender do chão das turbas, e remontar ao Céu, como uma águia imortal, e não é diante de tão excelso espetáculo que um homem pode sentir a dor que o punge. No outro dia estava pior; tratei-me enfim, mas incompletamente, sem método, nem cuidado, nem persistência; tal foi a origem do mal que me trouxe à eternidade. Sabem já que morri numa sexta-feira, dia aziago, e creio haver provado que foi a minha invenção que me matou. Há demonstrações menos lúcidas e não menos triunfantes. Não era impossível, entretanto, que eu chegasse a galgar o cimo de um século, e a figurar nas folhas públicas, entre macróbios. Tinha saúde e robustez. Suponha-se que, em vez de estar lançando os alicerces de uma invenção farmacêutica, tratava de coligir os elementos de uma instituição política, ou de uma reforma religiosa. Vinha a corrente de ar, que vence em eficácia o cálculo humano, e lá se ia tudo. Assim corre a sorte dos homens.
#Digite o texto 4 (aperte enter para sair):
#O autor do texto 2 está infectado com COH-PIAH

#COMO MONTAR(ORGANIZAÇÃO DO DESENVOLVIMENTO):
#Montar uma função main chamada coh-piah. Adicionar as funções na ordem sugerida pelo cursera, com exceção das tres ultima que tenho que criar,
#onde primeiro calcula assinatura, as compara e depois avalia. 


import re

def le_assinatura():
    #A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:")) 

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    #A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    #A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    #A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    #A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    #Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    #Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    #IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    #Usar a formula do cursera:
    sab = 0 
    for i in range(6):
       aux = abs(as_a[i] - as_b[i]) 
       sab = sab + aux
    sab = sab / 6
    return sab



def calcula_assinatura(texto):
    #IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    #wal-Tamanho médio de palavra: Média simples do número de caracteres por palavra.
    #ttr-Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
    #hlr-Razão Hapax Legomana: Número de palavras utilizadas uma única vez dividido pelo número total de palavras.
    #sal-Tamanho médio de sentença: Média simples do número de caracteres por sentença.
    #sac-Complexidade de sentença: Média simples do número de frases por sentença.
    #pal-Tamanho médio de frase: Média simples do número de caracteres por frase.
    
    sentencas = separa_sentencas(texto)
    aux_s = 0
    for sentenca in sentencas:
        aux_s = aux_s + len(sentenca) 
        #aux_s.append(len(sentenca))  
    sal = aux_s / len(sentencas)

    frases = []
    for sentenca in sentencas:
        frases_da_sentenca = separa_frases(sentenca)
        for frase in frases_da_sentenca:
            frases.append(frase)
    aux_f = 0
    for frase in frases:
        aux_f = aux_f + len(frase)
    pal = aux_f / len(frases)

    sac = len(frases) / len(sentencas)

    palavras = []
    for frase in frases:
        palavras_da_frase = separa_palavras(frase)
        for palavra in palavras_da_frase:
            palavras.append(palavra)
    aux_p = 0
    for palavra in palavras:
        aux_p = aux_p + len(palavra)
    wal = aux_p / len(palavras) 

    palavra_unica = n_palavras_unicas(palavras)
    hlr = palavra_unica / len(palavras)

    palavra_diferente = n_palavras_diferentes(palavras)
    ttr = palavra_diferente / len(palavras)

    ass_cp = [wal, ttr, hlr, sal, sac, pal]
   
    return ass_cp



def avalia_textos(textos, ass_cp):
    #IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    
    grau_similaridade = []

    for texto in textos:
        assinatura = calcula_assinatura(texto)
        comparacao = compara_assinatura(assinatura, ass_cp)
        grau_similaridade.append(comparacao)
    
    resultado = min(grau_similaridade)
    resultado = grau_similaridade.index(resultado)

    return resultado + 1



#main função 

def coh_piah():
    ass_cp = le_assinatura()
    textos = le_textos()
    resultado = avalia_textos(textos, ass_cp)
    print("O autor do texto", resultado, "está infectado com COH-PIAH")


coh_piah()