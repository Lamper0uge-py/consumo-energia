system_styles = {"divider_bar" : "==" * 25} #Dicionário contendo estilos para melhorar a legibilidade no terminal;

print("Bem-vindo a calculadora de consumo de energia!")
print(system_styles["divider_bar"])

while True:
    print("Menu\n1 - Iniciar programa\n2 - Menu de ajuda\n0 - Encerrar programa")
    option_select = float(input("\nInforme a opção desejada: ")) #Armazena a opção selecionada;
    print(system_styles["divider_bar"])

    #Bloco: Programa;
    if option_select == 1:
        print("Programa iniciado!")

        try:
            device_name = input("Informe o nome do aparelho: ") #Armazena o nome do aparelho;
            power = float(input("Informe a potência do aparelho em watts: ")) #Armazena a potência do aparelho;
            medium_use = float(input("Informe o uso médio por dia em horas: ")) #Armazena o uso médio do aparelho;
            cost_value = 0.725 #Valor médio do kWh da Enel SP no ano de 2025;

            monthly_consumption = (power * medium_use * 30) / 1000 #Cálculo do consumo médio ao longo do mês;
            estimated_monthly_cost = monthly_consumption * cost_value #Estimativa do valor a ser pago no mês;
            estimated_anual_cost = estimated_monthly_cost * 12 #Estimativa do valor a ser pago no ano;

            print(system_styles["divider_bar"])
            print("Aparelho: {}\nConsumo estimado: {:.2f} kWh/mês".format(device_name, monthly_consumption))
            print("Com base no valor médio do kWh da Enel SP no ano de 2025, o preço estimado deste aparelho é R$ {:.2f} ao mês e R$ {:.2f} ao ano." .format(estimated_monthly_cost, estimated_anual_cost))
            print(system_styles["divider_bar"])

        except ValueError: #Tratamento de erro;
            print("\nValor digitado inválido, tente novamente por favor!")
            print(system_styles["divider_bar"])

    #Bloco: Menu de ajuda;
    elif option_select == 2:
        print("Bem-vindo ao menu de ajuda!\nAbaixo algumas dicas sobre como usar a calculadora!\n")
        print("- Informe apenas números válidos, sem letras ou símbolos, com exceção do campo nome do aparelho.")
        print("- Para valores decimais utilize ponto ao invés de vírgula (ex.: 2,20 = 2.20).")
        print("- Preencha o tempo de uso em horas por dia; para minutos, use valor decimal (ex.: 30 min = 0.5 h).")
        print("- Verifique a potência do aparelho em watts(W) na etiqueta do equipamento.")
        print(system_styles["divider_bar"])

    #Bloco: Encerrar programa;
    elif option_select == 0:
        print("Encerrando programa...\nPrograma encerrado, volte sempre!")
        print(system_styles["divider_bar"])
        break

    #Tratamento de erro da variável option_select;
    else:
        print("Valor digitado inválido, tente novamente por favor.")
        print("Caso precise de ajuda, acesse o menu de ajuda digitando 2 e apertando enter.")
        print(system_styles["divider_bar"])