from googlesearch import search

buscas = [
    "Lula educacao",
    "Lula democracia",
    "Lula SUS",
    "Crescimento Brasil Lula",
    "Brasil Lula Desmatamento",
    "Lula vacina H1N1",
    "Lula geração empregos",
    "Lula defesa pobres"
]

for k in range(50):
    contador_buscas = 0
    for i in buscas:
        contador_buscas = contador_buscas + 1
        contador_resultado = 0

        file_object = open('results_bolsonaro.txt', 'a')
        print (str(contador_buscas) + " " + i)
        file_object.write(str(contador_buscas) + " " + i)
        file_object.write("\n")
        for resultado in search(i, stop=10):
            contador_resultado = contador_resultado + 1
            print (str(contador_resultado) + " " + resultado)
            file_object.write(str(contador_resultado) + " " + resultado)

        file_object.close()