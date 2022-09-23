#henrique kenzo higa - 32256957
final_arquivo = False
string_vazia = ''
final_palavra=False
palavras=[0]*1000
lista2=[1,1]
n=0
meu_arquivo = open('input.txt', 'r')
arquivo_comp=open('compactado.txt','w')

def comparacao(pala,lista):
    for i in range(len(lista)):
        if lista[i]==0:
            return True
        elif lista[i]==pala:
            return False  
def posicao(pala,lista,x):
    count=1
    for k in range(x):
        if lista[k]==pala:
            for i in range(len(lista)):
                if lista[i]==pala:
                    palavras2=[0]*(i+1)
                    for j in range (i):
                        palavra=lista[j]
                        palavras2[j+1]=palavra
                    palavras2[0]=pala
                    for l in range(i+1):
                        lista[l]=palavras2[l]
            return count
        
        else:
            count+=1
    return True

def primeira(pala,lista,x):
    if x==0:
        lista[0]=pala
        print(lista[0])
        return
    else:
        palavras2=[0]*(x+1)
        for j in range (x):
            palavra=lista[j]
            palavras2[j+1]=palavra
        palavras2[0]=pala
        for l in range(x+1):
            lista[l]=palavras2[l]
        

while not final_arquivo:
    linha = meu_arquivo.readline().rstrip()
    if linha == string_vazia:
        final_arquivo = True        
    else:
        teste=len(linha.split())
        compactador = linha.split(' ')
        for i in range(teste):
            if comparacao(compactador[i],palavras):
                primeira(compactador[i],palavras,n)
                writeFile = arquivo_comp.write(compactador[i]+" ")
                n+=1
            else:
               teste=posicao(compactador[i],palavras,n)
               writeFile = arquivo_comp.write(f"{teste} ")

        writeFile = arquivo_comp.write("\n")

                
            
                
        

meu_arquivo.close()
arquivo_comp.close()


    
                    
            
            
            


            

