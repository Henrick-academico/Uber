def quicksort(lista:list, i:int, f:int):
    if len(lista)>1:
        x = lista[i]
        lado = 'E'
        inicio = i
        fim = f
        while f!=i:
            if lado == 'E':
                if lista[f]< x:
                    lista[i] = lista[f]
                    lado = 'D'
                    i+=1
                else:
                    f-=1
            else:
                if lista[i]>x:
                    lista[f] = lista[i]
                    lado = 'E'
                    f-=1 
                else:
                    i+=1        
        lista[f] = x
        if i != inicio:
            quicksort(lista,inicio,i-1)

        if f != fim:
            quicksort(lista,f+1,fim)
