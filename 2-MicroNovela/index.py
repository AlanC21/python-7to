def micro_novela():
    print("Estás en un bosque misterioso. Hay dos caminos frente a ti.")
    decision1 = input("¿Quieres ir a la izquierda o a la derecha? (izquierda/derecha): ").lower()

    if decision1 == "izquierda":
        print("Te adentras en un sendero oscuro y peligroso. Encuentras una cueva.")
        decision2 = input("¿Quieres entrar a la cueva o seguir caminando? (entrar/seguir): ").lower()

        if decision2 == "entrar":
            print("Dentro de la cueva encuentras un tesoro oculto. ¡Felicidades!")
        elif decision2 == "seguir":
            print("Decides seguir caminando y te pierdes en el bosque para siempre.")
        else:
            print("Opción no válida.")
    
    elif decision1 == "derecha":
        print("Tomas el camino hacia un hermoso prado lleno de flores.")
        decision2 = input("¿Quieres descansar en el prado o seguir caminando? (descansar/seguir): ").lower()

        if decision2 == "descansar":
            print("Te quedas en el prado y disfrutas de la paz. ¡Has tenido un final feliz!")
        elif decision2 == "seguir":
            print("Decides seguir caminando y descubres una aldea cercana. ¡Te has salvado!")
        else:
            print("Opción no válida.")
    
    else:
        print("Opción no válida.")

micro_novela()