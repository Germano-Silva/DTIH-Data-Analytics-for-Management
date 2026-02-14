import requests
import time

# --- Configurações do Trello ---
API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
API_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# --- Dados do Quadro ---
BOARD_NAME = "Projeto – Organização do Evento Interno"
LISTS = ["A Fazer", "Em Execução", "Aguardando Terceiros", "Concluído"]
LABELS = {
    "Alta Prioridade": "red",
    "Média Prioridade": "yellow",
    "Baixa Prioridade": "blue"
}

# --- Dados dos Cartões com Responsáveis ---
# Nota: Use o nome de usuário (username) ou nome completo para buscar o ID automaticamente.
CARDS_DATA = [
    {
        "name": "Reservar espaço físico para o evento", 
        "due": "2026-03-15", 
        "labels": ["Alta Prioridade"], 
        "members": ["me"],
        "checklist": ["Pesquisar opções de locais adequados.", "Verificar disponibilidade e custos.", "Confirmar reserva e enviar contrato."]
    },
    {
        "name": "Enviar convite aos colaboradores", 
        "due": "2026-03-20", 
        "labels": ["Média Prioridade"], 
        "members": ["me"],
        "checklist": ["Elaborar texto do convite.", "Definir ferramenta de envio (e-mail marketing, intranet).", "Disparar convites e monitorar aberturas."]
    },
    {
        "name": "Definir lista de convidados externos", 
        "due": "2026-03-10", 
        "labels": ["Alta Prioridade"], 
        "members": ["me"],
        "checklist": ["Reunir sugestões de convidados com a diretoria.", "Consolidar lista final.", "Obter contatos para envio de convites."]
    },
    {
        "name": "Contratar buffet", 
        "due": "2026-03-25", 
        "labels": ["Alta Prioridade"], 
        "members": ["me"],
        "checklist": ["Pesquisar fornecedores de buffet.", "Solicitar orçamentos e cardápios.", "Degustação e fechamento de contrato."]
    },
    {
        "name": "Criar apresentação institucional", 
        "due": "2026-04-05", 
        "labels": ["Média Prioridade"], 
        "members": ["me"],
        "checklist": ["Coletar informações e dados relevantes.", "Desenvolver slides e design.", "Revisar e aprovar com a equipe."]
    },
    {
        "name": "Comprar materiais de apoio", 
        "due": "2026-04-10", 
        "labels": ["Baixa Prioridade"], 
        "members": ["me"],
        "checklist": ["Listar materiais necessários (canetas, blocos, etc.).", "Pesquisar fornecedores e preços.", "Realizar compra e organizar entrega."]
    },
    {
        "name": "Fazer checklist de equipamentos", 
        "due": "2026-04-12", 
        "labels": ["Média Prioridade"], 
        "members": ["me"],
        "checklist": ["Identificar equipamentos necessários (projetor, som, microfones).", "Verificar disponibilidade interna.", "Solicitar aluguel, se necessário."]
    },
    {
        "name": "Solicitar orçamento para brindes", 
        "due": "2026-03-18", 
        "labels": ["Baixa Prioridade"], 
        "members": ["me"],
        "checklist": ["Pesquisar opções de brindes.", "Entrar em contato com fornecedores.", "Comparar orçamentos e apresentar propostas."]
    }
]

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

if __name__ == "__main__":
    create_trello_board()
