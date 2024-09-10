# 💰 Desafio: Sistema Bancário Simples em Python

Este projeto implementa um sistema bancário básico em Python, onde o usuário pode realizar operações de depósito, saque, visualizar extrato e sair da aplicação. O código contém validações de limite de saques diários e saldo disponível.

## 🚀 Funcionalidades

- **Depósito**: O usuário pode realizar depósitos em sua conta.
- **Saque**: Limite de 3 saques diários, com valor máximo de R$ 500 por operação.
- **Extrato**: Exibe o histórico de transações realizadas, incluindo depósitos e saques, além do saldo atual.
- **Limitações**: Não é possível sacar mais do que o saldo disponível na conta.

## 🛠️ Como o Sistema Funciona

Ao iniciar o programa, o usuário verá um menu com as seguintes opções:

```bash
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
```
1. **Depósito (d)**: Permite que o usuário deposite um valor positivo na conta. Se o valor inserido for inválido (menor ou igual a zero), a operação será cancelada.

2. **Saque (s)** :Limite de 3 saques por dia.
O valor máximo para saque é de R$ 500 por operação.
Se o saldo for insuficiente, o saque não será permitido.
3. **Extrato (e)**: Exibe o histórico de todas as transações realizadas (depósitos e saques) e o saldo atual da conta. Se não houverem transações, uma mensagem indicará que não houve movimentações.

4. **Sair (q)**: Encerra o programa.

## 💻 Exemplo de Uso
```
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Escolha uma opção: d
Informe o valor do depósito: 200
Depósito realizado com sucesso!

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Escolha uma opção: s
Informe o valor do saque: 100
Saque realizado com sucesso!
Saques restantes: 2

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Escolha uma opção: e
Extrato
----------------------
Depósito: + R$ 200.00
Saque: - R$ 100.00
----------------------
Saldo: R$ 100.00
----------------------
```

## 📜 Instruções de Execução
- Clone este repositório:
```
git clone https://github.com/seu-usuario/seu-repositorio.git
```
- Navegue até o diretório do projeto:
```
cd seu-repositorio
```
- Execute o script:
```
python3 sistema_bancario.py
```