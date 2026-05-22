# Desafio 02 — Calculadora de IMC
# Aluno: (seu nome aqui)
# Data:  (data de entrega)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
nome = str(input("Digite seu nome:"))
altura = float(input("Digite sua altura:"))
massa = float(input("Digite sua massa corporal: "))
print(f"{nome}, seu imc é {massa / (altura * altura)}")
