#Conjunto de Funções desenvolvidas por Leonardo Gimenes
#Objetivo: Estabelecer comunicação serial e diagnosticar funcionamento.
#Ler e escrever pela mesma





def mySerial():


#Importando o framework de serial e fazendo os ajustes para abertura da porta COM
    import serial
    import time
    
    porta="COM8"                #input(print("Digite a porta serial a ser usada (ex: COM10): "))
    velocidade= 115200           #input(print("Digite VELOCIDADE: "))
    bytesize= 8
    
   

    mySerial1=serial.Serial(porta,velocidade,bytesize)

#Testando se a portal serial está aberta para comunicação
    if mySerial1.isOpen()==True:
        print("Confirmando abertura de comunicação serial")
    else:
        print("Falha na abertura de comunicação serial")
        print("Favor checar disponibilidade de porta COM seleciona")
        print("Programa será abortado")

   
#Função principal para leitura e escrita da serial    
    while True:
        opcao=int(input(print("Digite 1 para Ler da Serial\n Digite 2 para Escrever na Serial\n Digite 3 para Sair")))
        if opcao==1:
            lerSerial()
        if opcao==2:
            escreverSerial(mySerial1)
        if opcao!=1 and opcao!=2:
            return False
    mySerial.close()


# Função escreve na serial e confirma integridade de escrita
def escreverSerial(mySerial1):
    escSer=input(print("Digite o comando a ser enviado pela Serial:"))
    # CSE     <LF><CR>
    data2=mySerial1.write(bytes(escSer,'UTF-8'))
    data=mySerial1.inWaiting()
    tdata=mySerial1.read()
    print(str(data2))
    
    
    

    
    

    

    
    
