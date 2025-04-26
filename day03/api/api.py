# essa é uma API de operações básicas de CRUD
# ela foi criada seguidas as instruções em: https://medium.com/@habbema/python-apis-862ff2fd324e

from flask import flask, jsonify, request

app = flask(__name__)
tarefas = []

@app.route('/') # a rota mapeia a URL a uma função específica. nesse caso, ela irá até a função que exibe um texto da página home
def home():
    return 'bem vindo à API de tarefas!'

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas) # o métood jsonify converte uma estrutura pyhton (dicionário ou lista) em resposts JSON

@app.route('/tarefas', method=['POST'])
def criar_tarefa():
    descricao = request.json.get('descricao')
    nova_tarefa = {'id': len(tarefas) + 1, 'descricao': descricao}
    tarefas.append(nova_tarefa), 201
    return jsonify(nova_tarefa), 201

if __name__ == '__main__':
    app.run(debug=True)



