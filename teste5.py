def inverter_string(texto):


  texto_invertido = ""
  for i in range(len(texto) - 1, -1, -1):
    texto_invertido += texto[i]
  return texto_invertido

# Obtém a string do usuário
texto = input("Digite uma string: ")

# Inverte a string e imprime o resultado
resultado = inverter_string(texto)
print("A string invertida é:", resultado)