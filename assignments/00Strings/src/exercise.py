def main():
    #escribe tu código abajo de esta línea
    escuela="TecNM-Campus Culiacán"

    primeros=escuela[0:10]
    ultimos=escuela[-8:]
    enmedio=escuela[2:7]
    pares=escuela[::2]
    impares=escuela[1::2]

    print("primeros="+primeros)
    print("ultimos="+ultimos)
    print("en medio="+enmedio)
    print("pares="+pares)
    print("impares="+impares)

if __name__=='__main__':
    main()
