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

total_bill = 0
bill = []
text="Hola"
speech = gTTS(text= text, lang="es-us", slow=False)
speech.save("texto1.mp3")

while True:
    print("Escanea tu codigo de barras")
    value = input();
    end_code="fin"
    if value == end_code:
        print("Compra realizada")
        break

    for key in items.keys():
        if key==value:
            item = items[key]
            print(f"Esto es: {item['name']}, El precio es: {item['precio']} pesos mexicanos")
            text= (f"Esto es: {item['name']}, El precio es: {item['precio']} pesos mexicanos")
            total_bill += item['precio']
            bill.append(item)
            language = "es-us"
            speech = gTTS(text= text, lang=language, slow=False)
            '''guarda el archivo mp3 y reproducirlo'''
            speech.save("texto1.mp3")
            os.system("start texto1.mp3")
            break
    else:
        print("Objeto no encontrado",value)

for i,item in enumerate(bill):
    print(f"{i+1}. {item['name'],item['precio']}")

print(f'\nTu gasto total es de: ${total_bill} pesos mexicanos')
