if __name__ == '__main__':
    nasted={}
    for _ in range(0,int(input())):
        name = input()
        score = float(input())
        nasted[name]=score
    notas=nasted.values()
    aux=sorted(list(set(notas)))
    alvo=aux[1]
    saida=[]
    for key, value in nasted.items():
        if value==alvo:
            saida.append(key)
    saida.sort()
    for lanca in saida:
        print (lanca)