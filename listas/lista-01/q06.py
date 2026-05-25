# Lista 01 — Questão 06: Validador de Senha
# Aluno: (seu nome)
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Escreva um programa que solicite uma senha em loop até que atenda TODOS:
#   1. Mínimo 8 caracteres.
#   2. Pelo menos um dígito (use .isdigit() em cada caractere).
#   3. Pelo menos uma letra maiúscula.
# Para cada tentativa inválida, informe qual critério não foi atendido.
# Ao aceitar: 'Senha válida após X tentativa(s).'

# ── Sua solução abaixo ──────────────────────────────────────────────────────
tentativas = 0

while True:
    senha = input("Digite uma senha: ")
    tentativas += 1

    tem_numero = False
    tem_maiuscula = False

    # Verifica cada caractere
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True

        if caractere.isupper():
            tem_maiuscula = True

    # Lista de erros encontrados
    erros = []

    if len(senha) < 8:
        erros.append("A senha deve ter pelo menos 8 caracteres.")

    if not tem_numero:
        erros.append("A senha deve conter pelo menos um número.")

    if not tem_maiuscula:
        erros.append("A senha deve conter pelo menos uma letra maiúscula.")

    # Se houver erros, mostra todos
    if erros:
        print("\nSenha inválida:")
        for erro in erros:
            print("-", erro)
        print()

    else:
        print(f"Senha válida após {tentativas} tentativa(s).")
        break
