import requests

BASE_URL = 'http://localhost:5000'
def obter_tarefas():
    response = requests.get(f'{BASE_URL}/tarefas')
    
def criar_tarefas(descricao):
    response = requests.post(f'{BASE_URL}/tarefas', json={'descricao': descricao})
    return response.json()

def executar_exemplos():
    print('listando tarefas: ')
    print(obter_tarefas())
    print('criando uma novaa tarefa: ')
    print(criar_tarefas('estudar python'))
    
    if __name__ == '__main__':
        executar_exemplos