def juego_preguntas():
    print("Bienvenido al juego de preguntas y respuestas")
    respuestas = {}

    respuestas["nombre"] = input("¿Cual es tu nombre completo? ")
    respuestas["color"] = input("¿Cuál es tu color favorito? ")
    respuestas["comida"] = input("¿Cuál es tu comida favorita? ")
    respuestas["animal"] = input("¿Cuál es tu animal favorito? ")
    
    print("\n¡Gracias por responder! Aquí están tus respuestas:")
    for pregunta, respuesta in respuestas.items():
        print(f"Tu {pregunta} favorito es: {respuesta}")

juego_preguntas()