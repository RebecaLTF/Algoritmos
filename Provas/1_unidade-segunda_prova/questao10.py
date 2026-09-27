sistemas = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
votos = [0] * 6
voto = -1
while voto != 0:
  opcao = int(input("Digite o voto (1-6) ou 0 para encerrar: "))
  if opcao.isdigit():
    voto = int(opcao)
    if 1 <= voto <= 6:
            votos[voto - 1] += 1
    elif voto != 0:
      print("Voto inválido! Digite um número entre 1 e 6 ou 0 para encerrar.")
  else:
    print("Entrada inválida! Digite um número inteiro entre 0 e 6.")

total_votos = sum(votos)
print("\nSistema Operacional     Votos   %")
print("-------------------     -----   ---")
for i in range(6):
    percentual = (votos[i] / total_votos * 100) if total_votos > 0 else 0
    print(f"{sistemas[i]:<23}{votos[i]:<8}{int(percentual)}%")
print("-------------------     -----")
print(f"Total                    {total_votos}")
if total_votos > 0:
    max_votos = max(votos)
    indice_vencedor = votos.index(max_votos)
    percentual_vencedor = (max_votos / total_votos * 100)
    print(f"\nO Sistema Operacional mais votado foi o {sistemas[indice_vencedor]}, "
          f"com {max_votos} votos, correspondendo a {int(percentual_vencedor)}% dos votos.")
else:
    print("\nNenhum voto foi registrado.")