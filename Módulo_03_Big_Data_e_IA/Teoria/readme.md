# Big Data e Inteligência Artificial na Gestão Empresarial

**Resumo**

Os documentos fornecem uma visão abrangente sobre o universo de Big Data e Inteligência Artificial (IA), abordando desde os conceitos fundamentais até suas aplicações práticas na gestão empresarial. O tema central é como as organizações podem extrair valor estratégico de grandes volumes de dados. Os materiais detalham as características do Big Data, conhecidas como os **5 Vs (Volume, Velocidade, Variedade, Veracidade e Valor)**, e apresentam a arquitetura de dados, desde a coleta até o consumo final.

Um foco significativo é dado à Inteligência Artificial, explorando seus subcampos como **Machine Learning e Deep Learning**, e como eles dependem de dados para "aprender" e gerar previsões. São discutidas aplicações práticas, como a otimização da cadeia de suprimentos, personalização da experiência do cliente e análise preditiva de demanda. As fontes também apresentam ferramentas essenciais de visualização e análise de dados, como Power BI e Tableau, e o impacto das IAs Generativas, como ChatGPT e DALL-E, na automação de tarefas e produção de conteúdo.

Finalmente, é levantada uma discussão crítica sobre os desafios éticos e sociais da IA, destacando os **vieses algorítmicos** e a importância da transparência e regulamentação, conforme ilustrado no documentário "Coded Bias".

---

## Índice

* [1. Big Data: Fundamentos, Desafios e Oportunidades](#1-big-data-fundamentos-desafios-e-oportunidades)
  * [1.1. As 5 Características (5 Vs) do Big Data](#11-as-5-características-5-vs-do-big-data)
  * [1.2. Arquitetura e Fluxo de Dados](#12-arquitetura-e-fluxo-de-dados)
  * [1.3. Desafios do Big Data](#13-desafios-do-big-data)
  * [1.4. Oportunidades Geradas pelo Big Data](#14-oportunidades-geradas-pelo-big-data)
* [2. Inteligência Artificial (IA): Conceitos, Técnicas e Aplicações](#2-inteligência-artificial-ia-conceitos-técnicas-e-aplicações)
  * [2.1. Conceitos Fundamentais e Evolução da IA](#21-conceitos-fundamentais-e-evolução-da-ia)
  * [2.2. Técnicas de IA para Gestão](#22-técnicas-de-ia-para-gestão)
  * [2.3. IAs Generativas e seu Impacto](#23-ias-generativas-e-seu-impacto)
* [3. Aplicações Práticas de Dados e IA na Gestão Empresarial](#3-aplicações-práticas-de-dados-e-ia-na-gestão-empresarial)
  * [3.1. Tomada de Decisão com Algoritmos Preditivos](#31-tomada-de-decisão-com-algoritmos-preditivos)
  * [3.2. Estudo de Caso: Cortex Intelligence](#32-estudo-de-caso-cortex-intelligence)
* [4. Ferramentas e Tecnologias para Análise de Dados](#4-ferramentas-e-tecnologias-para-análise-de-dados)
  * [4.1. Ferramentas de Visualização e Análise com IA](#41-ferramentas-de-visualização-e-análise-com-ia)
  * [4.2. Ferramentas de Engenharia de Dados](#42-ferramentas-de-engenharia-de-dados)
* [5. Desafios Éticos e Sociais da Inteligência Artificial](#5-desafios-éticos-e-sociais-da-inteligência-artificial)
  * [5.1. Vieses Algorítmicos e o Caso "Coded Bias"](#51-vieses-algorítmicos-e-o-caso-coded-bias)
  * [5.2. Privacidade, Transparência e Responsabilidade](#52-privacidade-transparência-e-responsabilidade)
* [Conclusão](#conclusão)
* [Referências](#referências)

---

## 1. Big Data: Fundamentos, Desafios e Oportunidades

O termo Big Data se refere a um enorme volume de dados gerados continuamente a partir de diversas fontes, como redes sociais, sensores de IoT e transações online (Módulo 03 - Aula 01). O conceito vai além do volume, englobando características específicas que definem sua complexidade e potencial.

### 1.1. As 5 Características (5 Vs) do Big Data

O conceito é geralmente explicado por meio de cinco características principais (Módulo 03 - Aula 01):

* **Volume:** Refere-se à quantidade massiva de dados gerados diariamente. Trilhões de bytes de dados são criados a cada segundo, incluindo registros de transações bancárias, interações em redes sociais e dados de servidores.

* **Velocidade:** A rapidez com que os dados são gerados e precisam ser processados, muitas vezes em tempo real. Empresas de e-commerce monitoram transações instantaneamente para detectar fraudes ou ajustar estoques.

* **Variedade:** Os dados podem ser estruturados (bancos de dados relacionais), semiestruturados (XML, JSON, logs) ou não estruturados (vídeos, e-mails, áudios, postagens em redes sociais), aumentando a complexidade da análise.

* **Veracidade:** Trata da confiabilidade e qualidade dos dados, exigindo a filtragem de informações imprecisas ou irrelevantes. Nas redes sociais, por exemplo, pode haver muita desinformação que compromete a análise.

* **Valor:** A característica final, que representa a capacidade de transformar dados brutos em insights acionáveis que geram impacto positivo para o negócio.

### 1.2. Arquitetura e Fluxo de Dados

O ciclo de vida dos dados em um ambiente de Big Data segue uma estrutura lógica (Módulo 03 - Aula 01 e Aula 08):

1. **Fontes de Dados (Data Sources):** O ponto de origem dos dados, que podem ser sistemas internos (CRM, ERP, OLTP), redes sociais, Meta Ads, Google Analytics, planilhas Excel, entre outros.

2. **Ingestão/Coleta (Data Ingestion/Collection):** Processo de extrair os dados das fontes e movê-los para um ambiente centralizado. Pode ser feito:
   - **Batch/Scheduled:** Dados coletados em blocos, em horários definidos
   - **Speed/Real-Time:** Coleta contínua em tempo real (streaming)
   - Ferramentas: Airbyte, Fivetran, Zapier, Scripts Python

3. **Armazenamento (Data Storage):** Os dados coletados são armazenados em diferentes soluções:
   - **Cloud Storage:** HD online para arquivos como CSVs, imagens, PDFs (Google Cloud Storage, Amazon S3, Azure Blob)
   - **Data Lakes:** Repositório de dados brutos sem estrutura rígida (AWS Lake Formation, Google BigLake, Azure Data Lake, Databricks Delta Lake)
   - **Data Warehouses:** Ambientes otimizados para dados estruturados (BigQuery, Snowflake, Redshift, Azure Synapse)
   - **Bancos RDBMS e NoSQL:** Para diferentes tipos de estruturação

4. **Processamento (Data Processing):** Os dados são limpos, organizados e transformados usando ferramentas como Apache Spark, BigQuery e Dataflow. Remove duplicatas, trata erros e aplica regras de negócio.

5. **Análise (Data Analyses):** Aplicação de modelos estatísticos, Machine Learning, sistemas de recomendação e análises preditivas sobre os dados processados.

6. **Consumo (Data Consumption):** Os insights gerados são apresentados através de dashboards (Power BI, Tableau, Looker Studio), relatórios, visualizações de dados e alertas em tempo real.

**Governança de Dados:** Todo esse processo é supervisionado pela governança, que garante segurança, privacidade, qualidade, catalogação e rastreabilidade dos dados (Módulo 03 - Aula 01).

**SQL no Data Warehouse:** O SQL (Structured Query Language) é a linguagem principal para consultar, organizar e preparar dados no Data Warehouse, funcionando como a "chave de leitura" dessas estruturas (Módulo 03 - Aula 08).

### 1.3. Desafios do Big Data

As empresas enfrentam diversos obstáculos ao implementar iniciativas de Big Data (Módulo 03 - Aula 01):

* **Armazenamento e Processamento:** Necessidade de infraestrutura robusta, geralmente baseada em nuvem (AWS, Google Cloud, Azure), para lidar com o volume exponencial de dados.

* **Integração de Dados Heterogêneos:** Dificuldade de unificar dados de diferentes formatos e fontes. Ferramentas de ETL (Extração, Transformação e Carga), como Apache Nifi ou Talend, ajudam nesse processo.

* **Qualidade e Limpeza dos Dados:** Garantir que os dados sejam precisos, completos e livres de erros é essencial. O processo de data cleaning inclui remoção de duplicatas, correção de erros e preenchimento de informações ausentes.

* **Segurança e Privacidade:** Proteção de dados sensíveis e cumprimento de regulamentações como LGPD (Brasil) e GDPR (Europa).

* **Escassez de Profissionais Qualificados:** A demanda por especialistas em ciência de dados, estatística e IA supera a oferta no mercado.

### 1.4. Oportunidades Geradas pelo Big Data

Apesar dos desafios, o Big Data oferece vantagens competitivas significativas (Módulo 03 - Aula 01):

* **Tomada de Decisão Baseada em Dados:** Permite decisões mais informadas e precisas, como no setor de varejo onde a análise identifica padrões de comportamento para personalizar campanhas.

* **Personalização da Experiência do Cliente:** Empresas como Netflix e Amazon usam Big Data para recomendar produtos e conteúdos com base no comportamento anterior dos clientes.

* **Prevenção de Fraudes:** Bancos utilizam análise em tempo real para detectar padrões anômalos em transações financeiras através de algoritmos de machine learning.

* **Otimização de Operações:** Sensores IoT em fábricas monitoram equipamentos em tempo real, detectando falhas antes que ocorram (manutenção preditiva).

* **Inovação de Produtos e Serviços:** A análise revela novas oportunidades de mercado e tendências de consumo, permitindo às empresas desenvolver soluções inovadoras.

## 2. Inteligência Artificial (IA): Conceitos, Técnicas e Aplicações

A Inteligência Artificial, formalizada como campo de estudo em 1956 no Dartmouth Workshop, busca replicar processos cognitivos humanos em máquinas (Módulo 03 - Aula 03). Sua evolução recente foi impulsionada pelo Big Data, que serve como "combustível" para treinar algoritmos.

### 2.1. Conceitos Fundamentais e Evolução da IA

O conceito de máquinas inteligentes foi proposto por Alan Turing em 1950 com o "Teste de Turing" no artigo "Computing Machinery and Intelligence" (Módulo 03 - Aula 03). Turing sugeriu que se uma máquina pudesse imitar o comportamento humano de forma indistinguível, poderia ser considerada "inteligente".

A fase inicial da IA enfrentou grandes limitações técnicas, resultando nos chamados "invernos da IA". O verdadeiro potencial se materializou com o aumento exponencial de dados digitais na Era da Informação, permitindo o desenvolvimento de:

* **Machine Learning (ML):** Utiliza dados para que os algoritmos "aprendam" e melhorem seu desempenho sem serem explicitamente programados.
* **Deep Learning:** Subcampo do ML baseado em redes neurais profundas, especialmente eficaz para dados complexos.

**Ciclo de Vida dos Dados na IA:** Dados são coletados, armazenados, pré-processados (limpeza e preparação) e usados para treinar modelos. Este processo contínuo refina a habilidade dos modelos para fornecer insights cada vez mais precisos (Módulo 03 - Aula 03).

### 2.2. Técnicas de IA para Gestão

Diversas técnicas de IA são aplicadas para transformar operações e decisões empresariais (Módulo 03 - Aulas 03 e 04):

**Machine Learning:**
* **Aprendizado Supervisionado:** Usado para prever resultados com base em dados rotulados, como em previsões de vendas e análise de churn.
* **Aprendizado Não Supervisionado:** Utilizado para identificar padrões em dados não rotulados, como na segmentação de clientes.

**Processamento de Linguagem Natural (NLP):** Permite que máquinas entendam a linguagem humana, sendo aplicado em chatbots e análise de sentimento em redes sociais.

**Algoritmos Preditivos (Módulo 03 - Aula 04):**
* **Regressão Linear e Logística:** Preveem valores contínuos e probabilidades de eventos binários (ex: probabilidade de churn, volume de vendas futuras)
* **Árvore de Decisão:** Modelo que funciona como um diagrama onde cada nó representa uma pergunta sobre uma variável, com ramificações levando a resultados possíveis
* **Redes Neurais:** Detectam padrões sutis em dados complexos, aplicadas em diagnósticos médicos, previsão de demanda e detecção de fraudes

**Aplicações Práticas na Gestão (Módulo 03 - Aula 03):**
* **Análise Preditiva e Planejamento de Demanda:** Modelos que usam dados históricos para prever demanda e evitar problemas de estoque
* **Segmentação de Mercado e Personalização:** Algoritmos que segmentam clientes para campanhas direcionadas
* **Otimização da Cadeia de Suprimentos:** Monitoramento e ajuste de rotas, previsão de suprimentos
* **Automação de Processos:** Automatização de tarefas repetitivas como processamento de faturas

### 2.3. IAs Generativas e seu Impacto

As IAs Generativas são modelos avançados capazes de criar novos conteúdos, como textos, imagens e músicas (Módulo 03 - Aulas 03 e 05).

**Ferramentas Principais:**
* **ChatGPT e Jasper:** Modelos de linguagem que revolucionam a produção de conteúdo, permitindo automatizar a criação de relatórios, resumos e materiais de marketing. Compreendem comandos em linguagem natural, tornando-os acessíveis a usuários sem experiência técnica.

* **DALL-E e Midjourney:** IAs de geração de imagens que permitem criar gráficos e ilustrações apenas descrevendo o necessário, útil para materiais visuais personalizados sem equipes de design.

* **Copilot do Excel:** Exemplo de IA generativa integrada a ferramentas de trabalho. Simplifica a análise de dados permitindo perguntas em linguagem natural para gerar gráficos, tabelas e insights. Pode categorizar dados, sumarizar informações e gerar fórmulas complexas automaticamente (Módulo 03 - Aula 05).

**Impacto no Trabalho (Módulo 03 - Aula 03):**
* **Jornalismo e Produção de Conteúdo:** Redatores utilizam IAs para tarefas rotineiras, focando em análises complexas
* **Design e Marketing:** Criação rápida de conteúdo visual de alta qualidade
* **TI e Gestão:** Profissionais se especializam em monitoramento e ajuste de sistemas de IA, gestores otimizam análise de dados e tomada de decisões

## 3. Aplicações Práticas de Dados e IA na Gestão Empresarial

A aplicação de IA e análise de dados permite otimizar processos e tomar decisões mais estratégicas.

### 3.1. Tomada de Decisão com Algoritmos Preditivos

Os algoritmos preditivos são fundamentais para uma gestão baseada em dados (Módulo 03 - Aula 04):

**Previsão de Demanda e Planejamento de Estoque:** Usando algoritmos como regressão e redes neurais, empresas ajustam estoques com base em projeções, evitando excessos ou faltas e reduzindo custos de armazenagem.

**Análise de Risco Financeiro:** Algoritmos de classificação, como florestas aleatórias, estimam a probabilidade de inadimplência de clientes, permitindo ajuste de taxas de juros e condições de crédito para minimizar riscos.

**Retenção de Clientes:** Modelos preditivos de churn identificam clientes com risco de abandono, possibilitando ações preventivas que aumentam a retenção e satisfação.

**Processo de Implementação (Módulo 03 - Aula 04):**
1. **Definição do Problema e Seleção de Dados:** Identificar decisões específicas que precisam ser suportadas e escolher dados relevantes
2. **Treinamento e Validação do Modelo:** Garantir que o modelo generalize bem para novos dados
3. **Monitoramento Contínuo:** Atualizar modelos regularmente pois dados do mundo real mudam constantemente

### 3.2. Estudo de Caso: Cortex Intelligence

A Cortex Intelligence (https://www.cortex-intelligence.com/) é um exemplo de empresa que aplica ferramentas de TI para transformar dados em insights estratégicos (Módulo 03 - Aula 02).

**Cortex Go-to-Market (GTM):**
* Coleta e analisa dados de mercado, concorrentes e consumidores usando tecnologias de data scraping, APIs e integração de dados
* Monitora comportamento dos consumidores, atuação de concorrentes e oportunidades de mercado
* Utiliza SQL e Python para organizar dados e aplicar data cleaning
* Organiza informações em dashboards interativos para facilitar a tomada de decisão
* Permite análise de clientes potenciais, monitoramento de concorrentes e estratégias de marketing

**Cortex PR:**
* Monitora a reputação de marca em tempo real através de APIs que capturam dados de notícias, redes sociais (Twitter, Facebook, LinkedIn), blogs, podcasts e influenciadores
* Utiliza NLP para analisar o sentimento (positivo, negativo ou neutro) das menções
* Identifica crises de reputação através de gráficos de tendência e mapas de calor
* Permite comparação com concorrentes em termos de visibilidade e sentimento
* Apresenta dados em painéis de controle interativos de fácil interpretação

## 4. Ferramentas e Tecnologias para Análise de Dados

Existem diversas ferramentas projetadas para coletar, analisar e visualizar grandes volumes de dados de forma acessível.

### 4.1. Ferramentas de Visualização e Análise com IA

Essas ferramentas democratizam o acesso aos dados, permitindo que usuários sem conhecimento técnico avançado extraiam insights (Módulo 03 - Aulas 01 e 05).

**Power BI e Tableau:**
* Líderes de mercado conhecidos por interfaces intuitivas de "arrastar e soltar"
* Permitem criação rápida de dashboards interativos
* Power BI inclui "Visuals de IA" para análises automatizadas e recursos de AutoML para criar modelos preditivos
* Tableau fornece recomendações visuais automáticas baseadas nos dados importados

**Google Data Studio (Looker Studio):**
* Facilita integração com diversas fontes de dados
* Permite criação de relatórios dinâmicos com filtros interativos
* Design simples e navegação fácil para compartilhamento em tempo real
* Permite automação de relatórios que se atualizam automaticamente

**Vantagens de Usabilidade (Módulo 03 - Aula 05):**
* **Acesso sem Especialização Técnica:** Democratizam insights sem necessidade de programação avançada
* **Velocidade na Tomada de Decisões:** Geram relatórios e visualizações em minutos
* **Personalização e Flexibilidade:** Ajustam outputs conforme necessidades específicas
* **Integração com Fluxos de Trabalho:** Como Copilot do Microsoft 365, integrando Excel, PowerPoint e Teams

### 4.2. Ferramentas de Engenharia de Dados

Para processamento distribuído e armazenamento de Big Data (Módulo 03 - Aulas 01 e 08):

**Apache Hadoop:** Plataforma para armazenamento e processamento distribuído de grandes volumes de dados em clusters.

**Apache Spark:** Plataforma de processamento em tempo real, mais rápida que o Hadoop para certas tarefas, muito usada em Machine Learning.

**Bancos de Dados NoSQL (MongoDB, Cassandra):** Projetados para lidar com dados não estruturados e semiestruturados com alta flexibilidade e velocidade.

**Data Warehouses (BigQuery, Snowflake, Redshift, Azure Synapse):** Ambientes otimizados para armazenar dados estruturados e realizar consultas e análises em larga escala. SQL é fundamental para interagir com esses sistemas.

**Ferramentas de Coleta (Módulo 03 - Aula 08):**
* Airbyte, Fivetran, Zapier para automação de coleta
* Scripts em Python para coletas customizadas

## 5. Desafios Éticos e Sociais da Inteligência Artificial

O uso crescente da IA levanta questões críticas sobre ética, preconceito e responsabilidade (Módulo 03 - Aulas 03, 04 e 06).

### 5.1. Vieses Algorítmicos e o Caso "Coded Bias"

Modelos de IA aprendem com dados históricos que podem conter vieses sociais, raciais e de gênero (Módulo 03 - Aula 04).

**Documentário "Coded Bias" (Módulo 03 - Aula 06):**

Dirigido por Shalini Kantayya, o documentário explora como algoritmos de IA e reconhecimento facial perpetuam preconceitos. Principais pontos:

* **Experimento de Joy Buolamwini (MIT Media Lab):** Descobriu que sistemas de reconhecimento facial de grandes empresas (IBM, Microsoft) falhavam em identificar corretamente rostos de mulheres e pessoas negras, mas funcionavam precisamente para homens brancos. Ela precisava usar uma máscara branca para ser reconhecida.

* **Taxas de Erro Desiguais:** Algoritmos apresentavam taxas de erro muito mais altas ao identificar rostos femininos e de pessoas negras, com vieses embutidos nos dados de treinamento.

* **Impacto Social:** O reconhecimento facial é usado para vigilância populacional (China) e policial (EUA), afetando desproporcionalmente comunidades marginalizadas.

* **Algorithmic Justice League:** Organização fundada por Buolamwini para conscientizar sobre riscos de vieses em IA e pressionar por tecnologias mais justas e transparentes.

* **Falta de Regulamentação:** O documentário destaca a ausência de regulação sobre algoritmos que tomam decisões automáticas em publicidade, crédito e contratação, perpetuando preconceitos históricos sem supervisão.

* **Testemunhos de Afetados:** Relatos de pessoas que sofreram discriminação devido a decisões automatizadas, ilustrando como erros algorítmicos reforçam desigualdades.

**Vieses em Decisões Empresariais (Módulo 03 - Aula 04):**
Se dados históricos contêm preconceitos, modelos reproduzem tendências discriminatórias em áreas como recrutamento e concessão de crédito, levando a decisões injustas.

### 5.2. Privacidade, Transparência e Responsabilidade

Para construir confiança e garantir uso ético da IA (Módulo 03 - Aulas 03 e 04):

**Privacidade e Segurança:** A coleta de dados em larga escala exige práticas rigorosas para proteger a privacidade e cumprir legislações como LGPD (Brasil) e GDPR (Europa).

**Transparência e Explicabilidade:** É crucial que decisões tomadas por algoritmos sejam compreensíveis e justificáveis, especialmente em áreas de alto impacto como saúde e finanças. Modelos como redes neurais são considerados "caixas-pretas" por sua dificuldade de interpretação. Árvores de decisão oferecem maior transparência.

**Responsabilidade:** IA deve ser explicável para que empresas possam entender e justificar decisões, aumentando a confiança dos consumidores.

**Regulação:** Necessidade de regulamentação para prevenir perpetuação de preconceitos históricos e garantir uso responsável de algoritmos.

## Conclusão

Os materiais analisados demonstram que **Big Data e Inteligência Artificial são tecnologias transformadoras** com o potencial de redefinir a gestão empresarial. A capacidade de coletar, processar e analisar grandes volumes de dados permite que as organizações tomem decisões mais inteligentes, otimizem operações e criem experiências personalizadas para os clientes.

A arquitetura de dados moderna, desde as fontes até o consumo final, passando por processos de coleta, armazenamento, processamento e análise, fornece uma estrutura robusta para extrair valor dos dados (Módulo 03 - Aulas 01 e 08). Ferramentas de análise e visualização de dados, juntamente com as IAs Generativas, estão tornando essas tecnologias cada vez mais acessíveis, democratizando o acesso a insights valiosos (Módulo 03 - Aula 05).

No entanto, a implementação dessas tecnologias traz **desafios significativos**, incluindo a necessidade de infraestrutura robusta, profissionais qualificados e, acima de tudo, uma abordagem ética e responsável. O caso "Coded Bias" serve como um alerta contundente sobre os riscos de vieses algorítmicos e a importância de desenvolver sistemas justos e transparentes (Módulo 03 - Aula 06).

Para o futuro, o papel dos gestores será crucial (Módulo 03 - Aula 03). Eles precisarão não apenas entender os fundamentos técnicos da IA e do Big Data, mas também liderar a integração dessas tecnologias de forma estratégica e ética, garantindo que sejam alinhadas aos objetivos organizacionais e aos valores sociais. A colaboração entre humanos e IA, guiada por uma governança de dados sólida, definirá as empresas bem-sucedidas na era digital.

## Referências

**Módulo 03 - Aula 01:** Introdução ao Big Data: Características, Desafios e Oportunidades
* 5 Vs do Big Data
* Arquitetura e fluxo de dados
* Desafios e oportunidades
* Ferramentas e tecnologias (Hadoop, Spark, NoSQL, Tableau, Power BI)

**Módulo 03 - Aula 02:** Tecnologias de Big Data: ferramentas de visualização de grandes volumes de dados
* Estudo de caso: Cortex Intelligence
* Cortex Go-to-Market (GTM)
* Cortex PR

**Módulo 03 - Aula 03:** Inteligência Artificial (IA): conceitos básicos e aplicações na gestão
* Origem da IA (Alan Turing, Dartmouth Workshop 1956)
* Relação IA e Dados (Big Data, Machine Learning, Deep Learning)
* IAs Generativas (ChatGPT, DALL-E)
* Técnicas de IA para gestão
* Aplicações empresariais
* Desafios éticos

**Módulo 03 - Aula 04:** IA para tomada de decisões: machine learning e algoritmos preditivos
* Algoritmos preditivos (Regressão, Árvore de Decisão, Redes Neurais)
* Aplicações práticas (previsão de demanda, análise de risco, retenção de clientes)
* Processo de implementação de modelos
* Desafios éticos e técnicos (vieses, explicabilidade)

**Módulo 03 - Aula 05:** Exploração de ferramentas de IA para análise e visualização de dados empresariais
* Power BI e Tableau (Visuals de IA, AutoML)
* Google Data Studio (Looker Studio)
* IAs Generativas (ChatGPT, Jasper, DALL-E, Midjourney)
* Copilot do Excel
* Vantagens de usabilidade
* Integração com fluxos de trabalho

**Módulo 03 - Aula 06:** Caso de Estudo IA: o documentário Coded Bias
* Documentário dirigido por Shalini Kantayya
* Joy Buolamwini (MIT Media Lab)
* Vieses em reconhecimento facial
* Algorithmic Justice League
* Impacto social e falta de regulamentação

**Módulo 03 - Aula 08:** Análise de Dados e TI aplicado à Gestão - Engenharia de Dados
* Data Sources (fontes de dados)
* Data Collection (coleta de dados)
* Data Storage (armazenamento: Cloud Storage, Data Lake)
* Data Processing (processamento)
* Data Warehouse
* Data Analyses (AI Models, Reports, Data Visualization)
* SQL no Data Warehouse
* Estrutura completa do fluxo de dados