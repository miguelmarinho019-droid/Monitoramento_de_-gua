from colorama import Fore, Style
import random

niveis = ["Muito baixo (crítico) ","Baixo ", "Médio ", "Alto ", "Muito alto " ]

capacidade = random.randint(100,1000)

# Função de cálculo de nível
def calculo_de_nivel(): 
    if capacidade <= 200:
     return niveis [0] 
    elif capacidade <= 400 and capacidade > 200:
      return niveis [1]
    elif capacidade <= 600 and capacidade > 400:
      return niveis [2]
    elif capacidade <= 800 and capacidade > 600:
      return niveis [3]
    elif capacidade <= 1000 and capacidade > 800:
      return niveis [4]


# Função para demonstrar o nível com a cor correspondente e cálculo
def funçao_de_visualizaçao():
  nivel = calculo_de_nivel()
  if nivel == niveis [0]:
    print("NÍVEL DE ÁGUA:")
    print(Fore.RED + nivel + Style.RESET_ALL)
  elif nivel == niveis [1]:
    print("NÍVEL DE ÁGUA:")
    print(Fore.YELLOW + nivel + Style.RESET_ALL)
  elif nivel == niveis [2]:
    print("NÍVEL DE ÁGUA:")
    print(Fore.GREEN + nivel + Style.RESET_ALL)
  elif nivel == niveis [3]:
    print("NÍVEL DE ÁGUA:")
    print(Fore.CYAN + nivel + Style.RESET_ALL)
  elif nivel == niveis [4]:
    print("NÍVEL DE ÁGUA:")
    print(Fore.BLUE + nivel + Style.RESET_ALL)

funçao_de_visualizaçao()