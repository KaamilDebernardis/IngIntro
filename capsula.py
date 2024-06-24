
# def inicio():
    
#     if cp >= 1:
#         menor99()
#     else:
#         piezaspro()

# def piezaspro():
#     if cp==0:
#         print(f"cantidad de piezas procesadas: {cantpiezas}")

# def piezasinv():
#     if cp !=0:
#         print("codigo de pieza invalido")

# def menor99():
#     if cp<=99:
#         print("codigo de pieza: ", cp)
#         cantpiezas==cantpiezas+1
#         print(f"cantidad de piezas: {cantpiezas}")
        

# # if cp<= 99:
# #     mayor99(cp)

# cantpiezas=0
# cp=int(input("ingrese el codigo de la pieza para(0 para finalizar): "))

# inicio()

cant_piezas = 0

while True:
    cp = int(input('Ingresar el Código de Pieza (0 para finalizar): '))
    
    if cp >= 1 and cp <= 99:
        print('Código de Pieza:', cp)
        cant_piezas += 1
        prt = 0
        
        while True:
            cc = int(input('Ingrese el Código de Componente (0 para finalizar la pieza): '))
            
            if cc >= 101 and cc <= 9999:
                if cc % 100 == cp:
                    print('Código de Componente:', cc)
                    
                    while True:
                        prc = float(input('Ingrese el Precio del Componente: '))
                        
                        if prc < 10 or prc > 999.99:
                            print('Precio inválido')
                        else:
                            prt += prc
                            break
                else:
                    print('El Código de Componente no corresponde a la Pieza.')
            elif cc != 0:
                print('Código de Componente inválido.')
            else:
                break
        
        print('Precio Total de la Pieza:', prt)
    elif cp != 0:
        print('Código de Pieza inválido.')
    else:
        break

print('Cantidad de Piezas procesadas:', cant_piezas)

