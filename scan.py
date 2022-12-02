from gtts import gTTS
import os

'''Aquí van todas las posibles alternativas para el lector.'''
items = {"4005900618993":{"name":"Nivea Men Fresh",
                            "precio":99},
        "YQDB04354":{"name":"Eyoyo Wearable Ring Escaner de Codigo de Barras",
                            "precio":1150},
        "IBGO26535":{"name":"Fun Kit Electronic Components",
                            "precio":279},
        "LHJC61255":{"name":"Lentes Flex Focus Optic",
                            "precio":99},
        "758888882024":{"name":"Lentes Flex Focus Optic",
                            "precio":99},
        "7501630200080":{"name":"Cuaderno escolar Baseball",
                            "precio":20},                    
        "7501055317660":{"name":"Gatorade 1 litro",
                            "precio":25},    
        "7506129430801":{"name":"Scribe escolar plus",
                            "precio":24},   
        "7500533001091":{"name":"Agua purificada",
                            "precio":6},   
        }

def Procedimiento():
    total_bill = 0
    bill = []
    contador = 0
    continuar = True

    while continuar == True:
        print("Escanea tu codigo de barras")
        value = input();
        modo_manual="S_CMD_MT00"
        modo_auto="S_CMD_020F"
        end_code="0"
        if value == end_code:
            break
        if value == modo_manual:
            print("Ahora estás en modo manual")
        if value == modo_auto:
            print("Ahora estás en modo automatico")

        for key in items.keys():
            if key==value:
                item = items[key]
                print(f"Esto es: {item['name']}, El precio es: {item['precio']} pesos mexicanos")
                text= (f"Esto es: {item['name']}, El precio es: {item['precio']} pesos mexicanos")
                total_bill += item['precio']
                bill.append(item)
                contador + 1
                language = "es-us"
                speech = gTTS(text= text, lang=language, slow=False)
                '''guarda el archivo mp3 y reproducirlo'''
                speech.save("texto1.mp3")
                os.system("start texto1.mp3")
                break
        else:
            print("Objeto no encontrado",value)
            '''add = int(input("Cantidad de articulos a ingresar: "))
            if(add!=0):
                from database import articulo
            else:
                Procedimiento()'''

    for i,item in enumerate(bill):
         print(f"{i+1}. {item['name'],item['precio']}")

    '''en caso de existir menos de un articulo, no hará falta decir el precio final'''
    if contador>0:
        print(f'\nTu gasto total es de: ${total_bill} pesos mexicanos')
        textTotal= (f'\nTu gasto total es de: {total_bill} pesos mexicanos')
        language = "es-us"
        speech2 = gTTS(text= textTotal, lang=language, slow=False)
        speech2.save("textTotal.mp3")
        os.system("start textTotal.mp3")

    '''lanzamiento de menu de inicio luego de finalizar un registro de articulos'''
    print("Ingresa cualquier texto para continuar \no escanea el codigo para apagar el escaner")
    finish = "^&041&^"
    goback = input();
    if goback == finish:
        continuar = False
    else:
        continuar = True
        contador = 0
        Procedimiento()
Procedimiento()


