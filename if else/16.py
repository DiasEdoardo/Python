def main():
    print("Responda às seguintes perguntas com 'sim' ou 'nao'.")
    
    respostas_positivas = 0
    
    resposta_a = input("Telefonou para a vítima? ").lower()
    resposta_b = input("Esteve no local do crime? ").lower()
    resposta_c = input("Mora perto da vítima? ").lower()
    resposta_d = input("Devia para a vítima? ").lower()
    resposta_e = input("Já trabalhou com a vítima? ").lower()
    
    if resposta_a == "sim":
        respostas_positivas += 1
    if resposta_b == "sim":
        respostas_positivas += 1
    if resposta_c == "sim":
        respostas_positivas += 1
    if resposta_d == "sim":
        respostas_positivas += 1
    if resposta_e == "sim":
        respostas_positivas += 1
    
    if respostas_positivas == 2:
        print("Suspeita")
    elif 3 <= respostas_positivas <= 4:
        print("Cúmplice")
    elif respostas_positivas == 5:
        print("Assassino")
    else:
        print("Inocente")

if __name__ == "__main__":
    main()
