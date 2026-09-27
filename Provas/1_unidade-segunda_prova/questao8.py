meses = ["Janeiro", "Fevereiro", "Março", "Abril","Maio", "Junho", "Julho", "Agosto","Setembro", "Outubro", "Novembro", "Dezembro"]
temperaturas = []
for i in range(12):
    temperatura = float(input(f"Digite a temperatura média de {meses[i]}: "))
    temperaturas.append(temperatura)
media_anual = sum(temperaturas) / 12
print(f"Média anual das temperaturas: {media_anual:.2f}°C")
print("Meses com temperatura acima da média anual:")
for i in range(12):
    if temperaturas[i] > media_anual:
        print(f"{i+1} – {meses[i]}: {temperaturas[i]:.2f}°C")