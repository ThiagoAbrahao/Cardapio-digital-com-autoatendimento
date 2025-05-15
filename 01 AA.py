#sistema com "while True" para iniciar e reiniciar os atendimentos
while True:
    cadastro = input(
        "Olá, somos do Coffee Shops Tia Rosa,para visualizar o cardápio, precisaremos fazer um cadastro rapidinho, ok ? ").strip().lower()

    #Pega as informações dos clientes para a realização dos pedidos
    if cadastro == ("ok").strip().lower():
        nome_cliente = input("Certo,por favor, me diga seu nome ?")
        mesa_cliente = int(input("Qual o numero de sua mesa ?"))

        #mostrando as opções do cardápio
        print("beleza, aqui está nosso cardápio :")

        # Cardápio dividido por categorias de alimentos
        salgados = [
            {"nome": "Croissant Tradicional", "preco": 9.00, "ingredientes": "Massa folhada, manteiga"},
            {"nome": "Croissant Recheado (Presunto & Queijo)", "preco": 12.00,
             "ingredientes": "Massa folhada, presunto, queijo muçarela"},
            {"nome": "Torrada com Avocado e Ovo Pochê", "preco": 18.00,
             "ingredientes": "Pão artesanal, avocado, ovo, temperos"},
            {"nome": "Panquecas Americanas com Maple e Frutas", "preco": 20.00,
             "ingredientes": "Massa de panqueca, xarope de maple, frutas frescas"},
            {"nome": "Pão de Queijo Artesanal (3 unid.)", "preco": 10.00,
             "ingredientes": "Polvilho, queijo minas, ovos"},
            {"nome": "Tostex de Queijo, Tomate e Manjericão", "preco": 14.00,
             "ingredientes": "Pão de forma, queijo, tomate, manjericão"},
            {"nome": "Sanduiche Natural de Frango com Cenoura e Cream Cheese", "preco": 16.00,
             "ingredientes": "Pão integral, frango desfiado, cenoura ralada, cream cheese"},
            {"nome": "Ciabatta com Parma e Rúcula", "preco": 18.00,
             "ingredientes": "Pão ciabatta, presunto parma, rúcula, azeite"}
        ]

        bebidas_quentes = [
            {"nome": "Expresso", "preco": 6.00, "ingredientes": "Café 100% arábica"},
            {"nome": "Café Coado (filtrado)", "preco": 7.00, "ingredientes": "Café filtrado, água quente"},
            {"nome": "Capuccino Tradicional", "preco": 10.00,
             "ingredientes": "Café, leite vaporizado, chocolate em pó"},
            {"nome": "Mocha (com chocolate meio amargo)", "preco": 13.00,
             "ingredientes": "Café, leite, chocolate meio amargo"},
            {"nome": "Chá da Casa (ervas orgânicas)", "preco": 8.00, "ingredientes": "Blend de ervas naturais"}
        ]

        bebidas_geladas = [
            {"nome": "Cold Brew (café gelado filtrado a frio)", "preco": 12.00,
             "ingredientes": "Café especial, água fria, infusão lenta"},
            {"nome": "Frappé de Café com Baunilha", "preco": 14.00,
             "ingredientes": "Café, leite, gelo, essência de baunilha"},
            {"nome": "Chá Gelado de Hibisco com Limão Siciliano", "preco": 10.00,
             "ingredientes": "Hibisco, limão siciliano, gelo"},
            {"nome": "Smoothie de Morango com Banana e Iogurte", "preco": 16.00,
             "ingredientes": "Morango, banana, iogurte natural, mel"}
        ]

        doces_bolos = [
            {"nome": "Bolo de Cenoura com Calda de Chocolate (fatia)", "preco": 9.00,
             "ingredientes": "Cenoura, ovos, farinha, calda de chocolate"},
            {"nome": "Torta de Limão com Merengue", "preco": 12.00,
             "ingredientes": "Base crocante, creme de limão, merengue"},
            {"nome": "Brownie com Nozes", "preco": 10.00, "ingredientes": "Chocolate, ovos, farinha, nozes"},
            {"nome": "Cookie Gigante com Gotas de Chocolate", "preco": 8.00,
             "ingredientes": "Massa amanteigada, gotas de chocolate"},
            {"nome": "Cheesecake com Frutas Vermelhas", "preco": 14.00,
             "ingredientes": "Base de biscoito, creme de queijo, frutas vermelhas"}
        ]

        #Parte que exibi a lista de forma organizada e etseticamente bonita
        print("🥐 Salgados: ")
        for item in salgados:
            print(f"- {item['nome']}  - R$ {item['preco']:.2f} - {item['ingredientes']}")

        print("\n☕ Bebidas Quentes: ")
        for item in bebidas_quentes:
            print(f"- {item['nome']} - R$ {item['preco']:.2f} - {item['ingredientes']}")

        print("\n❄️ Bebidas Geladas: ")
        for item in bebidas_geladas:
            print(f"- {item['nome']} - R$ {item['preco']:.2f} - {item['ingredientes']}")

        print("\n🍰 Doces e Bolos: ")
        for item in doces_bolos:
            print(f"- {item['nome']} - R$ {item['preco']:.2f} - {item['ingredientes']}")

        # Adiciona funcionalidade para o cliente selecionar itens e calcular o total do pedido
        pedido = []  # Lista para armazenar os itens do pedido

        while True:
            print("\nDigite o número correspondente à categoria para selecionar itens:")
            print("1. Salgados")
            print("2. Bebidas Quentes")
            print("3. Bebidas Geladas")
            print("4. Doces e Bolos")
            print("5. Finalizar Pedido")

            escolha = input("Escolha uma categoria: ").strip()

            if escolha == "1":
                print("\n🥐 Salgados:")
                for i, item in enumerate(salgados, start=1):
                    print(f"{i}. {item['nome']} - R$ {item['preco']:.2f} - {item['ingredientes']}")
                item_escolhido = int(input("Escolha o número do item: ")) - 1
                quantidade = int(input("Digite a quantidade desejada: "))
                pedido.append({"nome": salgados[item_escolhido]["nome"],
                                "quantidade": quantidade,
                                "preco": salgados[item_escolhido]["preco"]})

            elif escolha == "2":
                print("\n☕ Bebidas Quentes:")
                for i, item in enumerate(bebidas_quentes, start=1):
                    print(f"{i}. {item['nome']} - R$ {item['preco']:.2f} - {item['ingredientes']}")
                item_escolhido = int(input("Escolha o número do item: ")) - 1
                quantidade = int(input("Digite a quantidade desejada: "))
                pedido.append({"nome": bebidas_quentes[item_escolhido]["nome"],
                                "quantidade": quantidade,
                                "preco": bebidas_quentes[item_escolhido]["preco"]})

            elif escolha == "3":
                print("\n❄️ Bebidas Geladas:")
                for i, item in enumerate(bebidas_geladas, start=1):
                    print(f"{i}. {item['nome']} - R$ {item['preco']:.2f} - {item['ingredientes']}")
                item_escolhido = int(input("Escolha o número do item: ")) - 1
                quantidade = int(input("Digite a quantidade desejada: "))
                pedido.append({"nome": bebidas_geladas[item_escolhido]["nome"],
                                "quantidade": quantidade,
                                "preco": bebidas_geladas[item_escolhido]["preco"]})

            elif escolha == "4":
                print("\n🍰 Doces e Bolos:")
                for i, item in enumerate(doces_bolos, start=1):
                    print(f"{i}. {item['nome']} - R$ {item['preco']:.2f} - {item['ingredientes']}")
                item_escolhido = int(input("Escolha o número do item: ")) - 1
                quantidade = int(input("Digite a quantidade desejada: "))
                pedido.append({"nome": doces_bolos[item_escolhido]["nome"],
                                "quantidade": quantidade,
                                "preco": doces_bolos[item_escolhido]["preco"]})

            #Comando final para emitir o resumo do pedido, a comanda
            elif escolha == "5":
                print("\n🧾 Resumo do Pedido:")
                total = 0
                for item in pedido:
                    subtotal = item["quantidade"] * item["preco"]
                    total += subtotal
                    print(f"{item['quantidade']}x {item['nome']} - R$ {subtotal:.2f}")
                print(f"\nTotal: R$ {total:.2f}")
                if total >= 35:
                    print("\nParabéns, a cada R$ 35,00 em compras você ganha 01 ponto, completando 10 pontos, você ganhará uma refeição de graça 😊!")
                    print("Você possui : 01/10")
                break
            else:
                print("Opção inválida. Tente novamente.")












