import time
import sys

# Função de animação de carregamento
def loading_animation(text):
    print(text, end="")
    for _ in range(3):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.5)
    print(" Concluído!\n")
