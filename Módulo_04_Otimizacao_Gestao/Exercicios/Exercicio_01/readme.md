# Exercício 01 - Modelagem de Processos em Tecnologia

## Módulo 4 - Otimização da Gestão de Tempo e Recursos

---

## Objetivo do Exercício

Desenvolver uma modelagem completa de processos de um departamento de tecnologia utilizando plataformas visuais (Miro/Whimsical), aplicando os conceitos de **Business Process Management (BPM)** e preparando o terreno para futuras integrações e automatizações.

---

## Contexto Escolhido

**Empresa:** Departamento de Tecnologia (Fictício)  
**Departamento:** Suporte Técnico e Operações de TI  
**Processo Selecionado:** **Gestão de Incidentes**

### Por que Gestão de Incidentes?

O processo de Gestão de Incidentes é crítico para:
- Manutenção da disponibilidade e performance de sistemas
- Garantia da continuidade dos negócios
- Satisfação dos usuários finais
- Identificação de melhorias e oportunidades de automação

---

## Estrutura da Modelagem

### Elementos Obrigatórios Documentados

Para cada atividade do processo, foram obrigatoriamente documentados:

| Elemento | Descrição |
|----------|-----------|
| ⏰ **Prazo de Execução** | Tempo estimado ou máximo para conclusão da atividade |
| 📄 **Descrição Clara** | Explicação objetiva do que a atividade envolve e seus objetivos |
| 👤 **Responsável** | Papel ou pessoa encarregada de executar a atividade |
| 🏢 **Local de Execução** | Sistema, ferramenta, e-mail ou ambiente onde a atividade é realizada |

### Metodologia 5W2H Aplicada

Cada atividade foi detalhada considerando:

- **What?** (O quê?) - Atividade específica a ser realizada
- **Why?** (Por quê?) - Propósito e objetivo da atividade
- **Who?** (Quem?) - Responsável pela execução
- **Where?** (Onde?) - Local/sistema onde ocorre
- **When?** (Quando?) - Prazo de execução
- **How?** (Como?) - Método de execução
- **How much?** (Quanto?) - Recursos envolvidos

---

## 🔄 Fluxo do Processo de Gestão de Incidentes

### Visão Macro do Processo

```
Incidente Reportado → Registro → Classificação → Atribuição → 
Investigação → Solução → Validação → Comunicação → Fechamento
```

### Papéis Envolvidos

- 👤 **Analista de Suporte N1** - Registro, classificação inicial e comunicação
- 👤 **Analista de Suporte N2 / Gerente** - Classificação avançada e atribuição
- 👥 **Equipe Técnica** - Investigação, diagnóstico e implementação de soluções
- 🧪 **QA / Usuário Final** - Teste e validação da solução

---

## Arquivos do Projeto

### Diagramas Mermaid

#### 1. Guia de Modelagem de Processos
**Arquivo:** [`Guia_de_Modelagem_de_Processos.mmd`](/Guia_de_Modelagem_de_Processos.mmd)

Este diagrama apresenta a estrutura conceitual do guia de modelagem, incluindo:
- Escolha de empresa e departamento
- Entendimento de BPM e dados
- Elementos obrigatórios por atividade
- Notação e simbologia (BPMN)
- Estrutura hierárquica de processos
- Metodologia 5W2H completa

**Visualização:**
```mermaid
%%{init: {'theme':'dark', 'themeVariables': {
  'darkMode': true,
  'primaryColor': '#BD93F9',
  'primaryTextColor': '#F8F8F2',
  'primaryBorderColor': '#6272A4',
  'lineColor': '#F8F8F2',
  'secondaryColor': '#44475A',
  'tertiaryColor': '#282A36',
  'clusterBkg': '#44475A',
  'clusterBorder': '#6272A4',
  'nodeBorder': '#BD93F9',
  'fontFamily': 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif'
}}}%%
flowchart TD
    classDef startEnd fill:#FF79C6,stroke:#FF79C6,stroke-width:2px,color:#000000
    classDef process fill:#44475A,stroke:#BD93F9,stroke-width:2px,color:#F8F8F2
    classDef decision fill:#6272A4,stroke:#8BE9FD,stroke-width:2px,color:#F8F8F2
    classDef subgraphBkg fill:#282A36,stroke:#6272A4,stroke-width:2px,color:#F8F8F2
    classDef integration fill:#50FA7B,stroke:#50FA7B,stroke-width:2px,color:#000000
    classDef automation fill:#FFB86C,stroke:#FFB86C,stroke-width:2px,color:#000000
    
    subgraph subGraph0["📋 Guia de Modelagem de Processos em Tecnologia"]
        direction TB
        A("🎯 Início: Objetivo do Guia"):::startEnd
        B("Capacitar usuário em modelagem de processos de TI<br>para automação/integração"):::process
        D("🏢 Escolha Empresa/Departamento de TI"):::process
        D1["💼 Ex: Desenvolvimento, Infraestrutura, Suporte"]:::process
        E("📚 Entendimento de BPM e Dados"):::process
        E1["🔄 BPM: Sequência de atividades que agregam valor"]:::process
        E2["📊 Dados: Essenciais para eficiência e decisão estratégica"]:::process
        E3["📈 Ciclo de Vida: Modelagem → Execução → Monitoramento → Otimização"]:::process
        F("📝 Elementos Obrigatórios por Atividade"):::process
        F1["⏰ Prazo de Execução"]:::process
        F2["📄 Descrição Clara da Atividade"]:::process
        F3["👤 Identificação do Responsável"]:::process
        F4["🏢 Local Onde a Atividade Ocorre"]:::process
        G("🎨 Notação e Simbologia"):::process
        G1["📐 Inspirar-se em BPMN: Eventos, Atividades, Decisões, Fluxos, Piscinas/Raias"]:::process
        H("🏗️ Estrutura Hierárquica"):::process
        H1["📂 Macro Processos → Processos → Subprocessos → Atividades"]:::process
        I("🔍 Metodologia 5W2H para Detalhamento"):::process
        I1["❓ What: O quê?"]:::process
        I2["❓ Why: Por quê?"]:::process
        I3["❓ Who: Quem?"]:::process
        I4["❓ Where: Onde?"]:::process
        I5["❓ When: Quando?"]:::process
        I6["❓ How: Como?"]:::process
        I7["❓ How much: Quanto?"]:::process
    end

    %% Conexões principais do guia
    A --> B
    B --> D
    D --> D1
    D1 --> E
    E --> E1
    E1 --> E2
    E2 --> E3
    E3 --> F
    F --> F1 & F2 & F3 & F4
    F4 --> G
    G --> G1
    G1 --> H
    H --> H1
    H1 --> I
    I --> I1 & I2 & I3 & I4 & I5 & I6 & I7

    %% Aplicar classes de estilo aos subgraphs
    class subGraph0, subgraphBkg
```

#### 2. Processo de Gestão de Incidentes (Exemplo Prático)
**Arquivo:** [`Modulo_4_Aula_9_Exercicio_1.mmd`](/Modulo_4_Aula_9_Exercicio_1.mmd)

Este diagrama apresenta o fluxo completo e detalhado do processo de Gestão de Incidentes, incluindo:
- Todas as etapas do processo com swimlanes (raias por papel)
- Elementos obrigatórios de cada atividade
- Pontos de decisão e fluxos alternativos
- **Pontos de Integração identificados**
- **Oportunidades de Automação mapeadas**

**Visualização:**
```mermaid
%%{init: {'theme':'dark', 'themeVariables': {
  'darkMode': true,
  'primaryColor': '#BD93F9',
  'primaryTextColor': '#F8F8F2',
  'primaryBorderColor': '#6272A4',
  'lineColor': '#F8F8F2',
  'secondaryColor': '#44475A',
  'tertiaryColor': '#282A36',
  'clusterBkg': '#44475A',
  'clusterBorder': '#6272A4',
  'nodeBorder': '#BD93F9',
  'fontFamily': 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif'
}}}%%
flowchart TD
    classDef startEnd fill:#FF79C6,stroke:#FF79C6,stroke-width:2px,color:#000000
    classDef process fill:#44475A,stroke:#BD93F9,stroke-width:2px,color:#F8F8F2
    classDef decision fill:#6272A4,stroke:#8BE9FD,stroke-width:2px,color:#F8F8F2
    classDef subgraphBkg fill:#282A36,stroke:#6272A4,stroke-width:2px,color:#F8F8F2
    classDef integration fill:#50FA7B,stroke:#50FA7B,stroke-width:2px,color:#000000
    classDef automation fill:#FFB86C,stroke:#FFB86C,stroke-width:2px,color:#000000

    subgraph subGraph7["🔄 Processo de Gestão de Incidentes<br> (Exemplo<br> Prático)"]
        direction TB
        
        subgraph subGraph1["👤 Papel: Usuário/Sistema"]
            INC_A("📥 Início: Incidente Reportado"):::startEnd
        end
        
        subgraph subGraph2["👤 Papel: Analista de Suporte N1"]
            INC_B["📝 Registrar Incidente<br>⏰ Prazo: 15min<br>📄 Coletar informações iniciais<br>👤 Analista Suporte N1<br>🏢 Sistema ITSM"]:::process
            INC_C{"🔍 Classificar Incidente?"}:::decision
            INC_D["🏷️ Classificar e Priorizar<br>⏰ Prazo: 30min<br>📄 Avaliar natureza, impacto e urgência<br>👤 Analista N1/N2<br>🏢 Sistema ITSM"]:::process
        end
        
        subgraph subGraph3["👤 Papel: Analista N2 / Gerente"]
            INC_E["👥 Atribuir à Equipe<br>⏰ Prazo: 15min<br>📄 Encaminhar para equipe técnica<br>👤 Analista N2/Gerente<br>🏢 Sistema ITSM"]:::process
        end
        
        subgraph subGraph4["👤 Papel: Equipe Técnica"]
            INC_F["🔬 Investigar e Diagnosticar<br>⏰ Prazo: 1h-24h<br>📄 Analisar, reproduzir erro<br>👤 Equipe Técnica<br>🏢 Ferramentas monitoramento"]:::process
            INC_G{"✅ Solução Encontrada?"}:::decision
            INC_H["⚡ Implementar Solução<br>⏰ Prazo: 30min-48h<br>📄 Aplicar correção<br>👤 Equipe Técnica<br>🏢 Ambiente desenvolvimento"]:::process
            INC_I["📤 Escalar Incidente<br>⏰ Prazo: Imediato<br>📄 Encaminhar nível superior<br>👤 Equipe Técnica/Gerente<br>🏢 Sistema ITSM"]:::process
        end
        
        subgraph subGraph5["👤 Papel: QA / Suporte / Usuário"]
            INC_J["🧪 Testar e Validar<br>⏰ Prazo: 1h<br>📄 Garantir resolução completa<br>👤 QA/Suporte/Usuário<br>🏢 Ambiente testes"]:::process
        end
        
        subgraph subGraph6["👤 Papel: Analista N1/N2"]
            INC_K["📢 Comunicar Resolução<br>⏰ Prazo: 30min<br>📄 Informar usuário<br>👤 Analista N1/N2<br>🏢 Sistema ITSM/E-mail"]:::process
            INC_L["🔒 Fechar Incidente<br>⏰ Prazo: 1h<br>📄 Atualizar base conhecimento<br>👤 Analista N1/N2<br>🏢 Sistema ITSM"]:::process
            INC_M("✅ Fim: Incidente Resolvido"):::startEnd
        end
    end

    subgraph subGraph10["⚡ Pontos de Integração e Automatização"]
        direction TB
        
        subgraph subGraph8["🔗 Integração (Exemplos)"]
            INT1["🖥️ Monitoramento ↔ ITSM"]:::integration
            INT1_DESC["📊 Cria incidentes automaticamente<br>com alertas críticos"]:::process
            
            INT2["📧 E-mail/Chatbot ↔ ITSM"]:::integration
            INT2_DESC["🤖 Converte reportes em tickets<br>automaticamente"]:::process
            
            INT3["📚 Base Conhecimento ↔ ITSM"]:::integration
            INT3_DESC["💡 Sugere artigos durante<br>registro/investigação"]:::process
            
            INT4["💬 Comunicação ↔ ITSM"]:::integration
            INT4_DESC["🔔 Notificações automáticas de status<br>para Slack/Teams"]:::process
        end
        
        subgraph subGraph9["🤖 Automação (Exemplos)"]
            AUTO1["🎯 Registro e Classificação"]:::automation
            AUTO1_DESC["🧠 Chatbots/formulários inteligentes<br>pré-classificam incidentes"]:::process
            
            AUTO2["📋 Atribuição Automática"]:::automation
            AUTO2_DESC["⚙️ Regras no ITSM atribuem incidentes<br>por palavras-chave/tipo"]:::process
            
            AUTO3["📨 Respostas Padrão"]:::automation
            AUTO3_DESC["📤 Envio automático de soluções<br>pré-definidas"]:::process
            
            AUTO4["⬆️ Escalonamento Automático"]:::automation
            AUTO4_DESC["⏰ Escala incidentes não resolvidos<br>dentro do SLA"]:::process
            
            AUTO5["🔒 Fechamento Automático"]:::automation
            AUTO5_DESC["🕒 Fecha incidentes 'resolvidos'<br>após período sem reabertura"]:::process
            
            AUTO6["🔄 Atualização Base"]:::automation
            AUTO6_DESC["📝 Sugere inclusão de novas soluções<br>na base após fechamento"]:::process
        end
    end


    %% Conexões do processo de incidentes
    INC_A --> INC_B
    INC_B --> INC_C
    INC_C -- Sim --> INC_D
    INC_C -- Não --> INC_B
    INC_D --> INC_E
    INC_E --> INC_F
    INC_F --> INC_G
    INC_G -- Sim --> INC_H
    INC_G -- Não --> INC_I
    INC_I --> INC_F
    INC_H --> INC_J
    INC_J --> INC_K
    INC_K --> INC_L
    INC_L --> INC_M

    %% Conexões de integração e automação
    INT1 --> INT1_DESC
    INT2 --> INT2_DESC
    INT3 --> INT3_DESC
    INT4 --> INT4_DESC
    AUTO1 --> AUTO1_DESC
    AUTO2 --> AUTO2_DESC
    AUTO3 --> AUTO3_DESC
    AUTO4 --> AUTO4_DESC
    AUTO5 --> AUTO5_DESC
    AUTO6 --> AUTO6_DESC

    %% Conexões entre seções principais
    INC_M --> INT1 & AUTO1

    %% Aplicar classes de estilo aos subgraphs
    class subGraph1,subGraph2,subGraph3,subGraph4,subGraph5,subGraph6,subGraph7,subGraph8,subGraph9,subGraph10 subgraphBkg
```

---

## Ferramentas e Tecnologias Mencionadas

### Sistemas ITSM
- Jira Service Management
- ServiceNow

### Monitoramento
- Grafana
- Prometheus
- Zabbix
- Datadog
- ELK Stack (Elasticsearch, Logstash, Kibana)

### Desenvolvimento e CI/CD
- GitHub / GitLab
- Jenkins
- GitLab CI

### Comunicação
- Slack
- Microsoft Teams
- E-mail

---

## KPIs e Métricas do Processo

### Indicadores de Performance

| KPI | Objetivo | Medição |
|-----|----------|---------|
| ⏱️ **Tempo Médio de Resolução (MTTR)** | < 4 horas para incidentes críticos | Tempo entre abertura e fechamento |
| 📈 **Taxa de Resolução no Primeiro Contato** | > 60% | Incidentes resolvidos sem escalonamento |
| ⭐ **CSAT (Satisfação do Cliente)** | > 4.5/5.0 | Pesquisa pós-resolução |
| 🎯 **Cumprimento de SLA** | > 95% | Incidentes resolvidos dentro do prazo |
| 🔄 **Taxa de Reincidência** | < 10% | Incidentes reabertos após fechamento |
| 📊 **Volume de Incidentes por Categoria** | Análise mensal | Identificação de problemas sistêmicos |

---

## Modelagem Visual no Miro

### Link de Acesso
**[Acessar Modelagem Completa no Miro](https://miro.com/welcomeonboard/VVIxTmwvclU4UVQ1NC8zMmFnRWdQdEpWdkRiYk5jd2pxanBlOWJ1SzZyYUtDVXlwREs5RDlablpYOGFCZDN4Zi9wdmZ4cFljdlFvb3hncmw4aytVOUxpaDZPZlJSc1pMdS9maGNQRzd2VDZpOERiUWpPSmJEWDQvaUV1aG9ZZ0R0R2lncW1vRmFBVnlLcVJzTmdFdlNRPT0hdjE=?share_link_id=528125263395)**

### Recursos Visuais Incluídos

- ✅ Fluxograma completo com notação BPMN
- ✅ Swimlanes (raias) organizando responsabilidades
- ✅ Cartões detalhados para cada atividade
- ✅ Códigos de cores para diferentes tipos de ação
- ✅ Anotações sobre pontos de integração
- ✅ Identificação visual de oportunidades de automação

---

## Aprendizados e Conclusões

### Principais Insights

1. **Importância da Padronização:** Processos bem documentados facilitam a identificação de melhorias
2. **Dados como Base:** Métricas claras permitem gestão baseada em evidências
3. **Automação Estratégica:** Identificar pontos de automação pode reduzir tempo de resolução em até 60%
4. **Integração de Sistemas:** Ferramentas conectadas eliminam trabalho manual e erros

---

## Referências

- Guia Completo para Modelagem de Processos em Tecnologia (Material do Curso)
- BPMN 2.0 Specification
- ITIL v4 Framework (Incident Management)
- Metodologia 5W2H aplicada a processos
