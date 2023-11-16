from collections import deque

pilha = deque()
listaDesfazer = deque()
listaRefazer = []

options = [
    "Sair",
    "Adicionar texto",
    "Substituir palavra no texto",
    "Remover palavra do texto",
    "Remover texto todo",
    "Desfazer",
    "Refazer"
]

def displayMenu():
    print(f"{15 * '='} Menu {15 * '='}")
    for index, item in enumerate(options):
        print(f"{index} - {item}")
    print(f"{36 * '='}")

def inserir():
    print("Digite o texto a ser inserido:")
    texto = input(">>")

    file = open('./nomes.txt', 'r', encoding='utf-8')
    texto_antigo = file.read()
    listaDesfazer.append(texto_antigo)
    file.close()

    if len(texto_antigo) >= 1:
        file.close()
        arquivo = open('./nomes.txt', 'a', encoding="utf-8")
        arquivo.write(f"\n{texto}")
        arquivo.close()
    else:
        file.close()
        arquivo = open('./nomes.txt', 'a', encoding="utf-8")
        arquivo.write(f"{texto}")
        arquivo.close()

    print('Item adicionado com sucesso!')

def substituir():
    file = open('./nomes.txt', 'r', encoding='utf-8')
    texto_antigo = file.read()
    listaDesfazer.append(texto_antigo)
    file.close()

    print('Digite a palavra que deseja substituir')
    palavra = input(">>")
    print('Digite a nova palavra')
    sub = input(">>")
    arquivo = open('./nomes.txt', 'r', encoding="utf-8")
    texto = arquivo.read()
    arquivo.close()
    texto = texto.replace(palavra, sub)
    arquivo = open('./nomes.txt', 'w', encoding='utf-8')
    arquivo.write(texto)
    arquivo.close()
    print('Alterado')

def remover():
    file = open('./nomes.txt', 'r', encoding='utf-8')
    texto_antigo = file.read()
    listaDesfazer.append(texto_antigo)
    file.close()

    palavra = input("Digite a palavra que deseja remover:")
    arquivo = open('./nomes.txt', 'r', encoding="utf-8")
    texto = arquivo.read()
    arquivo.close()
    texto = texto.replace(palavra, "")
    arquivo = open('./nomes.txt', "w", encoding='utf-8')
    arquivo.write(texto)
    arquivo.close()

def removerTudo():
    file = open('./nomes.txt', 'r', encoding='utf-8')
    texto_antigo = file.read()
    listaDesfazer.append(texto_antigo)
    file.close()
    
    arquivo = open('./nomes.txt', 'w', encoding='utf-8')
    arquivo.close()

def desfazer():
    if len(listaDesfazer) != 0:
        arquivo = open('./nomes.txt', 'r', encoding='utf-8')
        listaRefazer.append(arquivo.read())
        arquivo.close()

        arquivo = open('./nomes.txt', 'w', encoding="utf-8")
        arquivo.write(listaDesfazer.pop())
        arquivo.close()
        print('Ação revertida')
    else:
        print('Não existem ações para serem revertidas')

def refazer():
    if len(listaRefazer) != 0:
        arquivo = open('./nomes.txt', 'r', encoding='utf-8')
        listaDesfazer.append(arquivo.read())
        arquivo.close()

        arquivo = open('./nomes.txt', 'w', encoding='utf-8')
        arquivo.write(listaRefazer.pop())
        arquivo.close()
        print('Ação refeita')

    else:
        print('Não existem ações para serem refeitas')

while True:    
    displayMenu()

    opcao = int(input(f'Escolha a opção de 0 a {len(options) - 1}: '))

    match opcao:
        case 0:
            print("Saindo da aplicação...")
            break
        case 1:
            print(f"{9 * '='} Adicionar texto {10 * '='}")
            inserir()
        case 2:
            print(f"{3 * '='} Substituir palavra no texto {4 * '='}")
            substituir()
        case 3:
            print(f"{5 * '='} Remover palavra do texto {5 * '='}")
            remover()
        case 4:
            print(f"{8 * '='} Remover texto todo {8 * '='}")
            removerTudo()
        case 5:
            print(f"{13 * '='} Desfazer {13 * '='}")
            desfazer()
        case 6:
            print(f"{14 * '='} Refazer {13 * '='}")
            refazer()