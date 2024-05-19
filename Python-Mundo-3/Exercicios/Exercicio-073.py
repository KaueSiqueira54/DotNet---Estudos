times = ("Athletico-PR", "Bahia", "Flamengo", "Botafogo", "São Paulo", "Cruzeiro", "Atlético-MG", "Bragantino", "Palmeiras", "Internacional", "Fortaleza", "Grêmio", "Vasco da Gama", "Criciúma", "Juventude", "Corinthians", "Fluminense", "EC Vitória", "Atlético-GO", "Cuiabá")

print(f"Os 5 primeiros times são: \n{times[:5]}")
print(f"Os 4 últimos times são: \n{times[-4:]}")
print(f"Os times em ordem alfabética são: \n{sorted(times)}")
print(f"O palmeiras esta na {times.index("Palmeiras")} posição")