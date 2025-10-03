# Resumo - Módulo 02 - Ferramentas de Análise de Dados

## Índice
1. [Introdução à Análise de Dados e suas Ferramentas](#introducao-a-analise-de-dados-e-suas-ferramentas)
   - 1.1 [O que é Business Intelligence (BI)?](#o-que-e-business-intelligence-bi)
   - 1.2 [Ferramentas Essenciais](#ferramentas-essenciais)
2. [Power BI: Curso Básico Completo](#power-bi-curso-basico-completo)
   - 2.1 [O Processo de BI no Power BI](#o-processo-de-bi-no-power-bi)
   - 2.2 [Instalação e Primeiros Passos](#instalacao-e-primeiros-passos)
   - 2.3 [Tratamento de Dados com Power Query](#tratamento-de-dados-com-power-query)
   - 2.4 [Modelagem de Dados e Relacionamentos](#modelagem-de-dados-e-relacionamentos)
   - 2.5 [Cálculos e Análises com Fórmulas DAX](#calculos-e-analises-com-formulas-dax)
   - 2.6 [Criação de Dashboards Interativos](#criacao-de-dashboards-interativos)
3. [Python: Uma Linguagem Versátil para Dados e Automação](#python-uma-linguagem-versatil-para-dados-e-automacao)
   - 3.1 [Importância e Aplicações no Mercado](#importancia-e-aplicacoes-no-mercado)
   - 3.2 [Python na Análise e Coleta de Dados](#python-na-analise-e-coleta-de-dados)
   - 3.3 [Automação de Processos com Python](#automacao-de-processos-com-python)
   - 3.4 [Cargos que Utilizam Python](#cargos-que-utilizam-python)
4. [Outras Ferramentas Relevantes](#outras-ferramentas-relevantes)
   - 4.1 [SQL e Bancos de Dados](#sql-e-bancos-de-dados)
   - 4.2 [Excel para Análises Rápidas](#excel-para-analises-rapidas)
   - 4.3 [Linguagem R para Estatística](#linguagem-r-para-estatistica)
5. [Caso de Uso: Otimização em uma Rede de Varejo](#caso-de-uso-otimizacao-em-uma-rede-de-varejo)
6. [Referências](#referencias)

---

## 1. Introdução à Análise de Dados e suas Ferramentas
A análise de dados é um processo fundamental para transformar dados brutos em insights valiosos que orientam decisões estratégicas em um negócio. Este processo depende de ferramentas que auxiliam na coleta, organização, limpeza, interpretação e apresentação eficiente dos dados.

### 1.1 O que é Business Intelligence (BI)?
**Business Intelligence (BI)** é o processo de analisar os dados de uma empresa para auxiliar na tomada de decisões baseada em dados, e não em "achismos". As ferramentas de BI, como Power BI, Tableau e QlikView, são projetadas para gerenciar, visualizar e analisar grandes volumes de dados, transformando-os em informações acionáveis. Elas permitem a integração de múltiplas fontes de dados (internas e externas) e a criação de dashboards interativos para monitoramento em tempo real.

O produto final visual de uma ferramenta de BI é, geralmente, um **relatório ou dashboard**, que apresenta métricas e indicadores de forma clara e intuitiva. O Power BI, por exemplo, é uma ferramenta da Microsoft que tem se destacado no mercado de BI.

### 1.2 Ferramentas Essenciais
As principais ferramentas utilizadas na análise de dados incluem:
- **Excel:** Para análises rápidas, tabelas dinâmicas e gráficos.
- **SQL:** Linguagem padrão para acessar e manipular grandes bancos de dados.
- **Python e R:** Linguagens de programação poderosas para análise de dados, automação e machine learning.

## 2. Power BI: Curso Básico Completo
O Power BI é uma ferramenta que permite ao usuário sair do zero e criar seu primeiro dashboard, abrangendo todo o ciclo de análise de dados.

### 2.1 O Processo de BI no Power BI
O processo de análise de dados dentro do Power BI segue etapas bem definidas:
1.  **Extração, Transformação e Carga (ETL):** Os dados são extraídos de diversas fontes (Excel, bancos de dados, sites), tratados e carregados na ferramenta. O tratamento, ou transformação, consiste em organizar e limpar os dados, removendo informações desnecessárias, preenchendo lacunas e ajustando formatos.
2.  **Modelagem de Dados e Relacionamentos:** Múltiplas tabelas são conectadas através de relacionamentos para que suas informações possam ser combinadas em uma única análise.
3.  **Cálculos e Análises (Fórmulas DAX):** Utilização de fórmulas DAX (Data Analysis Expressions) para criar cálculos e métricas, desde as mais simples até as mais complexas.
4.  **Criação de Relatórios e Dashboards:** Desenvolvimento da parte visual, com gráficos e outros elementos interativos.
5.  **Compartilhamento Online:** Os relatórios são publicados online, permitindo o acesso via link, com dados que podem ser atualizados automaticamente.

### 2.2 Instalação e Primeiros Passos
O Power BI Desktop pode ser baixado diretamente do site da Microsoft ou pela Microsoft Store. A vantagem de instalar pela Microsoft Store é que as atualizações são automáticas. A interface do Power BI possui três guias principais:
- **Relatório:** Onde os dashboards e gráficos são criados.
- **Tabela (antiga Dados):** Para visualizar as tabelas carregadas.
- **Modelo:** Onde os relacionamentos entre as tabelas são gerenciados.

### 2.3 Tratamento de Dados com Power Query
Ao importar dados, a opção **"Transformar dados"** abre o **Power Query**, um ambiente de edição onde os dados são limpos e organizados antes de serem carregados no Power BI. As edições feitas no Power Query não alteram o arquivo original (ex: a planilha de Excel).

Principais tarefas de tratamento no Power Query:
- **Renomear tabelas:** Dar nomes intuitivos e sem caracteres especiais.
- **Remover linhas e colunas:** Excluir linhas em branco ou colunas desnecessárias.
- **Promover cabeçalhos:** Utilizar a primeira linha de dados como cabeçalho das colunas.
- **Dividir colunas:** Separar informações que estão juntas em uma única coluna (ex: País e Continente) em colunas distintas.
- **Coluna de Exemplos:** Ferramenta de IA que preenche uma nova coluna com base em exemplos fornecidos pelo usuário, útil para reformatar textos.
- **Substituir valores:** Trocar textos específicos por outros (ex: "F" por "Feminino").
- **Juntar tabelas:**
    - **Acrescentar Consultas:** Empilha tabelas uma embaixo da outra (ex: juntar vendas de 2021, 2022 e 2023 em uma única base).
    - **Mesclar Consultas:** Traz uma coluna de uma tabela para outra, similar à função PROCV do Excel.

### 2.4 Modelagem de Dados e Relacionamentos
Após carregar as tabelas limpas, é crucial criar relacionamentos entre elas. A modelagem de dados envolve dois tipos de tabelas:
- **Tabela Fato:** Tabela grande com registros de eventos históricos (ex: tabela de vendas).
- **Tabela Dimensão (ou Características):** Tabela menor que descreve algo (ex: cadastro de produtos, clientes ou lojas).

Os relacionamentos são criados conectando uma **chave primária** (coluna com valores únicos em uma tabela dimensão, como `ID_Produto`) a uma **chave estrangeira** (coluna correspondente em uma tabela fato, onde os valores podem se repetir). Com os relacionamentos corretos, é possível cruzar informações de diferentes tabelas em um único gráfico.

### 2.5 Cálculos e Análises com Fórmulas DAX
As fórmulas DAX, escritas em inglês, permitem criar "medidas" para realizar cálculos. As principais são:
- **`SUM`:** Soma os valores de uma coluna.
- **`AVERAGE`:** Calcula a média dos valores de uma coluna.
- **`COUNTROWS`:** Conta o número de linhas de uma tabela.
- **`DISTINCTCOUNT`:** Conta o número de valores únicos em uma coluna.
- **`CALCULATE`:** **A fórmula mais importante do Power BI**, permite fazer cálculos com filtros e condições. Exemplo: calcular as vendas apenas de lojas físicas.

### 2.6 Criação de Dashboards Interativos
A etapa final é a criação do dashboard, onde os dados são visualizados.
- **Layout e Inspiração:** É recomendado buscar inspiração em sites como Pinterest e Dribble para o design do dashboard. Um plano de fundo pode ser criado no PowerPoint e importado como imagem.
- **Hierarquia Visual:** As informações mais importantes devem ser posicionadas na parte superior esquerda, seguindo o padrão de leitura em "Z".
- **Interatividade:** Uma das maiores vantagens do Power BI é a **interatividade entre os gráficos**. Clicar em um elemento de um gráfico (ex: uma barra ou uma fatia de pizza) filtra automaticamente todos os outros visuais do dashboard.
- **Segmentação de Dados:** Permite adicionar filtros interativos ao dashboard, como um filtro de período, para que o usuário possa analisar os dados de forma personalizada.

## 3. Python: Uma Linguagem Versátil para Dados e Automação
Python é uma das linguagens de programação mais populares e valorizadas no mercado de trabalho, especialmente na área de ciência de dados. Sua combinação de simplicidade e versatilidade a torna aplicável em diversas áreas.

### 3.1 Importância e Aplicações no Mercado
Python é importante por ser uma das linguagens mais usadas e valorizadas no mercado. Sua versatilidade permite que seja aplicada em:
- **Desenvolvimento de sites e aplicativos:** Empresas como Google, Netflix, Spotify e Uber utilizam Python.
- **Desenvolvimento de jogos:** Jogos como The Sims 4 e Battlefield 2 foram desenvolvidos com Python.
- **Ciência de dados e Inteligência Artificial:** É a linguagem número um para essas áreas, sendo um pré-requisito para quem deseja atuar nelas.
- **Automação de processos:** Automatizar tarefas repetitivas é uma de suas maiores aplicações no ambiente corporativo.

A "comunidade Python" é um grande diferencial, pois muitos códigos e soluções para desafios comuns são compartilhados abertamente, permitindo que os usuários não precisem construir tudo do zero.

### 3.2 Python na Análise e Coleta de Dados
Python é uma excelente escolha para análise de dados, especialmente ao lidar com grandes volumes e machine learning. Sua vasta quantidade de bibliotecas (ferramentas prontas) facilita o trabalho. Para a coleta de dados, Python é amplamente utilizado em:
- **Web Scraping:** Capturar dados diretamente de sites públicos quando não há uma API disponível.
- **APIs:** Coletar dados de forma estruturada de plataformas como redes sociais.

### 3.3 Automação de Processos com Python
A automação é um dos grandes diferenciais do Python no ambiente de trabalho. É possível automatizar tarefas repetitivas para economizar tempo e reduzir erros humanos. Exemplos de automação:
- **Coleta automática de dados:** Criar scripts que coletam periodicamente informações de sites, redes sociais ou APIs.
- **Envio de e-mails e SMS:** Automatizar a comunicação.
- **Análise de dados e geração de relatórios:** Um script pode analisar uma base de dados e enviar um relatório por e-mail automaticamente.
- **Emissão de notas fiscais e automação no WhatsApp:** Exemplos práticos de automações que otimizam processos empresariais.

### 3.4 Cargos que Utilizam Python
Diversos profissionais utilizam Python em suas rotinas:
- **Cientista de Dados:** Para analisar dados e construir modelos de machine learning.
- **Engenheiro de Dados:** Para construir e manter infraestruturas de dados.
- **Analista de Dados:** Para processar, limpar e visualizar grandes conjuntos de dados.
- **Desenvolvedor de Software:** Em desenvolvimento web, automação e scripts.
- **Engenheiro de Automação:** Para automatizar tarefas repetitivas e testes de software.

## 4. Outras Ferramentas Relevantes

### 4.1 SQL e Bancos de Dados
**SQL (Structured Query Language)** é a linguagem padrão para interagir com bancos de dados. Bancos de dados organizam informações de forma estruturada, como uma grande planilha, facilitando o armazenamento e a consulta. Com SQL, é possível realizar operações como:
- **`SELECT`:** Buscar dados.
- **`INSERT`:** Adicionar novos registros.
- **`UPDATE`:** Modificar dados existentes.
- **`DELETE`:** Remover informações.

A limpeza e higienização dos dados (remover duplicatas, corrigir erros) é uma etapa crucial antes da análise, e pode ser feita com o auxílio de SQL.

### 4.2 Excel para Análises Rápidas
O Excel é uma ferramenta acessível e presente em quase todas as empresas, sendo muito útil para análises de dados. Suas funcionalidades poderosas incluem **fórmulas avançadas, gráficos interativos e, principalmente, as Tabelas Dinâmicas**, que permitem resumir e analisar dados rapidamente para descobrir tendências e padrões.

### 4.3 Linguagem R para Estatística
R é uma linguagem de programação com forte foco em **análise estatística e visualização de dados avançada**. É amplamente utilizada em ambientes acadêmicos e de pesquisa, sendo ideal para modelagem estatística complexa e cálculos matemáticos avançados. Profissionais como estatísticos e analistas de pesquisa frequentemente utilizam R. Muitos profissionais de dados dominam tanto Python quanto R, escolhendo a melhor ferramenta de acordo com o projeto.

## 5. Caso de Uso: Otimização em uma Rede de Varejo
Um estudo de caso demonstra como uma rede de varejo utilizou um conjunto de ferramentas de BI para otimizar suas operações.

- **Coleta e Organização:** A empresa integrou fontes de dados internas (vendas, estoque, CRM) e externas (tendências de mercado) usando **Power BI** como plataforma central. **SQL** foi usado para limpar e estruturar os dados, enquanto scripts em **Python** automatizaram a coleta de dados de e-commerce.
- **Análise e Dashboards:** Foram criados dashboards interativos no Power BI para monitorar o **desempenho de vendas** e a **gestão de estoque** em tempo real.
- **Relatórios para a Gestão:** Relatórios detalhados, combinando **Power BI e Excel**, foram gerados para a alta gestão, incluindo análises preditivas sobre tendências de vendas com algoritmos de machine learning.
- **Resultados:** A análise permitiu tomar decisões estratégicas mais ágeis, como prever a demanda regional, otimizar o inventário e ajustar campanhas de marketing, aumentando a competitividade da empresa.

---

## Referências

  - [Modulo_02-Aula_01.pdf - Introdução às ferramentas de TI essenciais para análise de dados](/Módulo_02_Ferramentas_de_TI/Teoria/Modulo_02-Aula_01.pdf)
  
 - [Modulo 02 Aula 02 - Importância e Aplicações do Python no Mercado de Trabalho (Vídeo do YouTube, Canal: Hashtag Programação)](https://www.youtube.com/watch?v=Vh6FS-pqjsM)

  - [Modulo_02-Aula_03.pdf - Coleta de dados: fontes internas e externas e automação de coleta de dados](/Módulo_02_Ferramentas_de_TI/Teoria/Modulo_02-Aula_03.pdf)
  - [Modulo_02-Aula_04.pdf - Organização de dados: banco de dados, estruturação e limpeza de dados](/Módulo_02_Ferramentas_de_TI/Teoria/Modulo_02-Aula_04.pdf)
  - [Modulo_02-Aula_05.pdf - Análise de dados com ferramentas práticas: dashboards, relatórios e gráficos interativos](/Módulo_02_Ferramentas_de_TI/Teoria/Modulo_02-Aula_05.pdf)
  - [Modulo_02-Aula_06.pdf - Introdução ao uso de softwares especializados para análise de dados empresariais](/Módulo_02_Ferramentas_de_TI/Teoria/Modulo_02-Aula_06.pdf)
  - [Modulo_02-Aula_07.pdf - Caso de estudo de análise de dados](/Módulo_02_Ferramentas_de_TI/Teoria/Modulo_02-Aula_07.pdf)
   - [Modulo 02 Aula 08 - Curso Power BI para Iniciantes - Aprenda Power BI em 3 Horas! (Vídeo do YouTube, Canal: Hashtag Treinamentos)](https://www.youtube.com/watch?v=UBLgxgSjECw)