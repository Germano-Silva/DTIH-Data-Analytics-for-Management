# Exercício Prático - Organização e Automação de Tarefas no Trello

Este projeto contém um script Python que automatiza a criação de um quadro no Trello para organizar as tarefas de um evento interno, conforme descrito no exercício prático.

## Estrutura do Projeto

- `Modulo-05-Aula-08-Exercicio-01.md`: Descrição detalhada do exercício prático
- `trello.py`: Script Python que automatiza a criação do quadro no Trello
- `README.md`: Este arquivo, com explicação do código

## Descrição do Exercício

O exercício consiste em criar um quadro no Trello chamado "Projeto – Organização do Evento Interno" com as seguintes listas:
- A Fazer
- Em Execução
- Aguardando Terceiros
- Concluído

Devem ser incluídos pelo menos 8 cartões com tarefas reais, cada um com:
- Etiqueta de prioridade (Alta, Média, Baixa)
- Data de entrega
- Checklist com pelo menos 3 subtarefas
- Responsável

## Explicação do Código

### 1. Importação de Bibliotecas

```python
import requests
import time
```

- `requests`: Biblioteca usada para fazer requisições HTTP à API do Trello
- `time`: Biblioteca usada para manipulação de tempo (não utilizada no código atual, mas mantida para possíveis funcionalidades futuras)

### 2. Configurações da API do Trello

```python
API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
API_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```

- `API_KEY`: Chave de API da conta Trello utilizada para autenticar as requisições
- `API_TOKEN`: Token de autenticação que permite o script acessar a conta Trello

### 3. Dados do Quadro

```python
BOARD_NAME = "Projeto – Organização do Evento Interno"
LISTS = ["A Fazer", "Em Execução", "Aguardando Terceiros", "Concluído"]
LABELS = {
    "Alta Prioridade": "red",
    "Média Prioridade": "yellow",
    "Baixa Prioridade": "blue"
}
```

- `BOARD_NAME`: Nome do quadro que será criado no Trello, conforme especificado no exercício
- `LISTS`: Lista dos nomes das colunas (listas) que serão criadas no quadro
- `LABELS`: Dicionário mapeando nomes de etiquetas de prioridade para suas cores correspondentes no Trello

### 4. Dados dos Cartões

```python
CARDS_DATA = [
    {
        "name": "Reservar espaço físico para o evento", 
        "due": "2026-03-15", 
        "labels": ["Alta Prioridade"], 
        "members": ["me"],
        "checklist": ["Pesquisar opções de locais adequados.", "Verificar disponibilidade e custos.", "Confirmar reserva e enviar contrato."]
    },
    # ... outros cartões ...
]
```

- `CARDS_DATA`: Lista de dicionários contendo informações para cada cartão:
  - `name`: Nome da tarefa
  - `due`: Data de entrega
  - `labels`: Lista de etiquetas de prioridade
  - `members`: Lista de responsáveis (usuários do Trello)
  - `checklist`: Lista de subtarefas para o checklist do cartão

A função suporta:
  - `"me"`: Atribui automaticamente o usuário atual da API
  - Username de outros usuários: Busca automaticamente o ID do membro
  - Se um username não for encontrado, o script exibe um aviso e continua
### 5. Função de Requisição ao Trello

```python
def trello_request(method, endpoint, params=None):
    url = f"https://api.trello.com/1/{endpoint}"
    base_params = {'key': API_KEY, 'token': API_TOKEN}
    if params:
        base_params.update(params)
    
    response = requests.request(method, url, params=base_params)
    if response.status_code != 200:
        print(f"Erro na requisição {endpoint}: {response.status_code} - {response.text}")
        response.raise_for_status()
    return response.json()
```

- `trello_request`: Função auxiliar que faz requisições à API do Trello
- Parâmetros:
  - `method`: Método HTTP (GET, POST, PUT, DELETE)
  - `endpoint`: Endpoint da API do Trello
  - `params`: Parâmetros adicionais da requisição
- Retorna a resposta em formato JSON
- Trata erros, imprimindo mensagens detalhadas em caso de falha
### 5. Função para Buscar ID de Membros

```python
def get_member_id(identifier):
    """Busca o ID de um membro pelo username ou retorna o ID do próprio usuário se for 'me'."""
    if identifier.lower() == "me":
        member = trello_request('GET', 'members/me')
        return member['id']
    
    # Busca por username
    try:
        member = trello_request('GET', f'members/{identifier}')
        return member['id']
    except:
        print(f"Aviso: Não foi possível encontrar o membro '{identifier}'.")
        return None
```

- `get_member_id`: Função auxiliar que busca o ID de um membro do Trello
- Parâmetros:
  - `identifier`: Pode ser:
    - `"me"`: Retorna o ID do usuário atual da API
    - Username: Busca o ID do membro pelo username
- Retorna:
  - ID do membro se encontrado
  - `None` se não encontrar e exibe um aviso
### 6. Função de Requisição ao Trello

```python
def trello_request(method, endpoint, params=None):
    url = f"https://api.trello.com/1/{endpoint}"
    base_params = {'key': API_KEY, 'token': API_TOKEN}
    if params:
        base_params.update(params)
    
    response = requests.request(method, url, params=base_params)
    if response.status_code != 200:
        print(f"Erro na requisição {endpoint}: {response.status_code} - {response.text}")
        response.raise_for_status()
    return response.json()
```

- `trello_request`: Função auxiliar que faz requisições à API do Trello
- Parâmetros:
  - `method`: Método HTTP (GET, POST, PUT, DELETE)
  - `endpoint`: Endpoint da API do Trello
  - `params`: Parâmetros adicionais da requisição
- Retorna a resposta em formato JSON
- Trata erros, imprimindo mensagens detalhadas em caso de falha
### 7. Função de Criação do Quadro

```python
def create_trello_board():
    try:
        print(f"1. Criando o quadro '{BOARD_NAME}'...")
        board = trello_request('POST', 'boards', {'name': BOARD_NAME, 'defaultLists': 'false', 'defaultLabels': 'false'})
        board_id = board['id']
        print(f"   Quadro criado! ID: {board_id}")

        # Criar Listas
        trello_lists = {}
        for list_name in LISTS:
            print(f"2. Criando lista '{list_name}'...")
            lst = trello_request('POST', f'boards/{board_id}/lists', {'name': list_name})
            trello_lists[list_name] = lst['id']

        # Criar Etiquetas
        trello_labels = {}
        for label_name, color in LABELS.items():
            print(f"3. Criando etiqueta '{label_name}' ({color})...")
            lbl = trello_request('POST', f'boards/{board_id}/labels', {'name': label_name, 'color': color})
            trello_labels[label_name] = lbl['id']

        # Criar Cartões
        for card in CARDS_DATA:
            print(f"4. Criando cartão: {card['name']}...")
            label_ids = [trello_labels[n] for n in card['labels']]
            
            new_card = trello_request('POST', 'cards', {
                'name': card['name'],
                'idList': trello_lists["A Fazer"],
                'due': card['due'],
                'idLabels': ",".join(label_ids)
            })
            
            # Adicionar Checklist
            if card.get('checklist'):
                ck = trello_request('POST', f'cards/{new_card["id"]}/checklists', {'name': 'Tarefas'})
                for item in card['checklist']:
                    trello_request('POST', f'checklists/{ck["id"]}/checkItems', {'name': item})

        print(f"\nSucesso! Acesse seu quadro em: {board['url']}")

    except Exception as e:
        print(f"\nFalha no processo: {e}")
```

- `create_trello_board`: Função principal que realiza todo o processo de criação do quadro
- Passos:
  1. **Criação do quadro**: Cria um novo quadro no Trello com o nome especificado
  2. **Criação das listas**: Para cada lista definida em `LISTS`, cria uma coluna no quadro
  3. **Criação das etiquetas**: Para cada etiqueta de prioridade, cria uma etiqueta colorida no quadro
  4. **Criação dos cartões**: Para cada cartão em `CARDS_DATA`:
     - Cria o cartão na lista "A Fazer"
     - Adiciona as etiquetas de prioridade
     - Adiciona a data de entrega
     - Cria um checklist com as subtarefas especificadas
### 8. Função de Criação do Quadro

```python
def create_trello_board():
    try:
        print(f"1. Criando o quadro '{BOARD_NAME}'...")
        board = trello_request('POST', 'boards', {'name': BOARD_NAME, 'defaultLists': 'false', 'defaultLabels': 'false'})
        board_id = board['id']
        print(f"   Quadro criado! ID: {board_id}")

        # Criar Listas
        trello_lists = {}
        for list_name in LISTS:
            print(f"2. Criando lista '{list_name}'...")
            lst = trello_request('POST', f'boards/{board_id}/lists', {'name': list_name})
            trello_lists[list_name] = lst['id']

        # Criar Etiquetas
        trello_labels = {}
        for label_name, color in LABELS.items():
            print(f"3. Criando etiqueta '{label_name}' ({color})...")
            lbl = trello_request('POST', f'boards/{board_id}/labels', {'name': label_name, 'color': color})
            trello_labels[label_name] = lbl['id']

        # Cache de IDs de membros para evitar requisições repetidas
        member_cache = {}

        # Criar Cartões
        for card in CARDS_DATA:
            print(f"4. Criando cartão: {card['name']}...")
            label_ids = [trello_labels[n] for n in card['labels']]
            
            # Resolver IDs dos membros
            card_member_ids = []
            for m in card.get('members', []):
                if m not in member_cache:
                    m_id = get_member_id(m)
                    if m_id:
                        member_cache[m] = m_id
                if m in member_cache:
                    card_member_ids.append(member_cache[m])

            # Criar o cartão com membros atribuídos
            new_card = trello_request('POST', 'cards', {
                'name': card['name'],
                'idList': trello_lists["A Fazer"],
                'due': card['due'],
                'idLabels': ",".join(label_ids),
                'idMembers': ",".join(card_member_ids) # Atribui os responsáveis aqui
            })
            
            # Adicionar Checklist
            if card.get('checklist'):
                ck = trello_request('POST', f'cards/{new_card["id"]}/checklists', {'name': 'Tarefas'})
                for item in card['checklist']:
                    trello_request('POST', f'checklists/{ck["id"]}/checkItems', {'name': item})

        print(f"\nSucesso! Acesse seu quadro em: {board['url']}")

    except Exception as e:
        print(f"\nFalha no processo: {e}")
```

- `create_trello_board`: Função principal que realiza todo o processo de criação do quadro
- Passos:
  1. **Criação do quadro**: Cria um novo quadro no Trello com o nome especificado
  2. **Criação das listas**: Para cada lista definida em `LISTS`, cria uma coluna no quadro
  3. **Criação das etiquetas**: Para cada etiqueta de prioridade, cria uma etiqueta colorida no quadro
  4. **Criação dos cartões**: Para cada cartão em `CARDS_DATA`:
     - Cria o cartão na lista "A Fazer"
     - Adiciona as etiquetas de prioridade
     - Adiciona a data de entrega
     - Atribui membros responsáveis (buscando seus IDs automaticamente)
     - Cria um checklist com as subtarefas especificadas

#### Novas funcionalidades:
- **Cache de membros**: Armazena IDs de membros já buscados para evitar requisições repetidas
- **Atribuição automática de responsáveis**: Busca o ID de cada membro pelo username ou usa "me" para o usuário atual
- **Tratamento de erros**: Se um username não for encontrado, exibe um aviso e continua o processo
### 8. Execução do Script

```python
if __name__ == "__main__":
    create_trello_board()
```

- Verifica se o script está sendo executado diretamente (não importado como módulo)
- Chama a função `create_trello_board()` para iniciar o processo de criação do quadro
### 9. Execução do Script

```python
if __name__ == "__main__":
    create_trello_board()
```

- Verifica se o script está sendo executado diretamente (não importado como módulo)
- Chama a função `create_trello_board()` para iniciar o processo de criação do quadro

### 5. Função de Requisição ao Trello

```python
def trello_request(method, endpoint, params=None):
    url = f"https://api.trello.com/1/{endpoint}"
    base_params = {'key': API_KEY, 'token': API_TOKEN}
    if params:
        base_params.update(params)
    
    response = requests.request(method, url, params=base_params)
    if response.status_code != 200:
        print(f"Erro na requisição {endpoint}: {response.status_code} - {response.text}")
        response.raise_for_status()
    return response.json()
```

- `trello_request`: Função auxiliar que faz requisições à API do Trello
- Parâmetros:
  - `method`: Método HTTP (GET, POST, PUT, DELETE)
  - `endpoint`: Endpoint da API do Trello
  - `params`: Parâmetros adicionais da requisição
- Retorna a resposta em formato JSON
- Trata erros, imprimindo mensagens detalhadas em caso de falha

### 6. Função de Criação do Quadro

```python
def create_trello_board():
    try:
        print(f"1. Criando o quadro '{BOARD_NAME}'...")
        # Criamos o quadro sem listas/etiquetas padrão para controle total
        board = trello_request('POST', 'boards', {'name': BOARD_NAME, 'defaultLists': 'false', 'defaultLabels': 'false'})
        board_id = board['id']
        print(f"   Quadro criado! ID: {board_id}")

        # Criar Listas
        trello_lists = {}
        for list_name in LISTS:
            print(f"2. Criando lista '{list_name}'...")
            lst = trello_request('POST', f'boards/{board_id}/lists', {'name': list_name})
            trello_lists[list_name] = lst['id']

        # Criar Etiquetas
        trello_labels = {}
        for label_name, color in LABELS.items():
            print(f"3. Criando etiqueta '{label_name}' ({color})...")
            lbl = trello_request('POST', f'boards/{board_id}/labels', {'name': label_name, 'color': color})
            trello_labels[label_name] = lbl['id']

        # Criar Cartões
        for card in CARDS_DATA:
            print(f"4. Criando cartão: {card['name']}...")
            label_ids = [trello_labels[n] for n in card['labels']]
            
            new_card = trello_request('POST', 'cards', {
                'name': card['name'],
                'idList': trello_lists["A Fazer"],
                'due': card['due'],
                'idLabels': ",".join(label_ids)
            })
            
            # Adicionar Checklist
            if card.get('checklist'):
                ck = trello_request('POST', f'cards/{new_card["id"]}/checklists', {'name': 'Tarefas'})
                for item in card['checklist']:
                    trello_request('POST', f'checklists/{ck["id"]}/checkItems', {'name': item})

        print(f"\nSucesso! Acesse seu quadro em: {board['url']}")

    except Exception as e:
        print(f"\nFalha no processo: {e}")
```

- `create_trello_board`: Função principal que realiza todo o processo de criação do quadro
- Passos:
  1. **Criação do quadro**: Cria um novo quadro no Trello com o nome especificado
  2. **Criação das listas**: Para cada lista definida em `LISTS`, cria uma coluna no quadro
  3. **Criação das etiquetas**: Para cada etiqueta de prioridade, cria uma etiqueta colorida no quadro
  4. **Criação dos cartões**: Para cada cartão em `CARDS_DATA`:
     - Cria o cartão na lista "A Fazer"
     - Adiciona as etiquetas de prioridade
     - Adiciona a data de entrega
     - Cria um checklist com as subtarefas especificadas

### 7. Execução do Script

```python
if __name__ == "__main__":
    create_trello_board()
```

- Verifica se o script está sendo executado diretamente (não importado como módulo)
- Chama a função `create_trello_board()` para iniciar o processo de criação do quadro

## Execução do Script

Para executar o script e criar o quadro no Trello:

```bash
python trello.py
```

O script irá:
1. Criar o quadro "Projeto – Organização do Evento Interno"
2. Criar as quatro listas (A Fazer, Em Execução, Aguardando Terceiros, Concluído)
3. Criar as etiquetas de prioridade (Alta, Média, Baixa) com cores correspondentes
4. Criar os 8 cartões com suas respectivas etiquetas, datas e checklists
5. Exibir a URL do quadro criado para acesso

## Considerações

- As credenciais da API (API_KEY e API_TOKEN) estão sensurados no script. Em ambientes de produção, estas informações devem ser armazenadas de forma segura (variáveis de ambiente, arquivos de configuração, etc.)
- O script assume que a conta Trello associada às credenciais tem permissão para criar quadros e adicionar conteúdo
- As datas de entrega estão definidas como exemplos e podem ser ajustadas conforme necessário
- O script pode ser modificado para ler dados de um arquivo de configuração ou de um banco de dados para maior flexibilidade