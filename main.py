import json

def adicionar_tarefas(tarefas):
    titulo = input('Digite o nome da tarefa: ').strip()
    if not titulo:
        print('Digite uma Tarefa!')
        return
    tarefa = {
        "titulo": titulo,
        "status": False
    }

    tarefas.append(tarefa)
    salvar_tarefas(tarefas)

    print('Tarefa adicionada com sucesso!')


def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)


def carregar_tarefas():
        try: 
            with open('tarefas.json', 'r') as arquivo:
                tarefas = json.load(arquivo)
                return tarefas
        except FileNotFoundError:
                return []



def listar_tarefas(tarefas):
    if not tarefas:
        print('Nenhuma tarefa cadastrada.')
        return
    else:
        for indice, tarefa in enumerate(tarefas,    start=1):
            if tarefa['status']:
                simbolo = '✔'
            else:
                simbolo = '❌'
            
            print(f'{indice} - {tarefa["titulo"]} [{simbolo}]')
          


def concluir_tarefas(tarefas):
    if not tarefas:
        print('Nenhuma tarefa pra concluir')
        return
    else:
        listar_tarefas(tarefas)
        try:    
            num_tarefa= int(input('Digite o numero da tarefa! '))
        except ValueError:
         print('Digite um número válido!')
         return
        indice_real = num_tarefa -1
        if indice_real >= 0 and indice_real < len(tarefas):
            if tarefas[indice_real]['status']:
                print('Essa tarefa já está concluída!')
                return
            tarefas[indice_real]['status'] = True
            salvar_tarefas(tarefas)
            print('Tarefa concluida com sucesso!')
        else: 
            print('Número de tarefa inválido!')
        


def remover_tarefas(tarefas):
    if not tarefas:
        print('Nenhuma tarefa pra remover!')
        return
    else:
        listar_tarefas(tarefas)
        try:
            num_tarefa = int(input('Digite o número da tarefa que quer remover: '))
        except ValueError:
            print('Digite um número válido!')
            return
        indice_real = num_tarefa - 1
        if indice_real >= 0 and indice_real < len(tarefas):
            tarefas.pop(indice_real)
            salvar_tarefas(tarefas)
            print('Tarefa removida com sucesso!')
        else:
            print('Número de tarefa inválido!')

    
    
tarefas = carregar_tarefas()

while True:
    print('\n ===== TO-DO LIST ======')
    print('1 - Adicionar Tarefa')
    print('2 - Listar tarefas')
    print('3 - Concluir Tarefa')
    print('4 - Remover Tarefa')
    print('5 - Sair')

    opcao =  input('Escolha uma opção: ').strip()

    if opcao == '1': 
        adicionar_tarefas(tarefas)

    elif opcao == '2':
        listar_tarefas(tarefas)

    elif opcao == '3':
        concluir_tarefas(tarefas)

    elif opcao == '4':
        remover_tarefas(tarefas)

    elif opcao == '5':
        print('Programa encerrado.')
        break

    else:
        print('Opção inválida!')