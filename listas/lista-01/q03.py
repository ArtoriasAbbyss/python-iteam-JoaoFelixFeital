# Lista 01 — Questão 03: Ficha de Cadastro
# Aluno: joao felix feital
# Data:  25/05/2026

# ── Enunciado ───────────────────────────────────────────────────────────────
# Solicite: nome completo, CPF (str), ano de nascimento (int), altura (float).
# O programa deve:
#   1. Calcular e exibir a idade em 2026.
#   2. Exibir todos os dados com f-string e tipos corretos.
#   3. Tratar com try/except o caso em que o ano não seja um número.
# Explique em comentário: por que float para altura e não int?

# ── Sua solução abaixo ──────────────────────────────────────────────────────
anoNascimento = int(input("Digite o ano em q nasceu: "));
anoAtual = int(2026);
try:
    print(f"Sua idade é {anoAtual - anoNascimento}");
except:
    print("O ano não é um número");
