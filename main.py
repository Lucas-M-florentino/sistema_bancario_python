menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

  print(menu)
  opcao = input("Escolha uma opção: ")
  if opcao == "d":

    valor  = float(input("Informe o valor do depósito: "))
    if valor > 0:
      saldo += valor
      extrato += f"Depósito: + R$ {valor:.2f}\n"
    else:
      print("Operação falhou! Valor informado é inválido.")
      
  elif opcao == "s":
    if numero_saques < LIMITE_SAQUES:
    
      valor = float(input("Informe o valor do saque: "))
      if valor > 0:
        extrato += f"Saque: - R$ {valor:.2f}"

        if (saldo - valor) >= 0:
          if valor <= limite:
            saldo -= valor
            numero_saques += 1
            extrato += "\n"
            print(f"Saques restantes: {LIMITE_SAQUES - numero_saques}")
          else:
            extrato += f" - Negado. Valor de saque superior ao limite de {limite}.\n"
            print(f"Valor excede o limite de saque de {limite} por operação.")
        else:
          extrato += " - Negado. Saldo insuficiente!\n"
          print("Operação falhou! Você não tem saldo suficiente.")
      else:
        print("Operação falhou! Valor informado é inválido.")
    else:
      print("Você excedeu o limite de saques.")
      
  elif opcao == "e":
    print("Extrato")
    print("----------------------")
    print(extrato if extrato else "Não realizou movimentções." )
    print("----------------------")
    print(f"Saldo: R$ {saldo:.2f}")
    print("----------------------")
    
  elif opcao == "q":
    print("Saindo...")
    break
    
  else:
    print(f"Opção {opcao} inválida, tente novamente uma opçao válida")