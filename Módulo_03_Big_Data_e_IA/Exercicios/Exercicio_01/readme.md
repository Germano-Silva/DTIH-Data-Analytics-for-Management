# EXERCÍCIO 1 - MÓDULO 3
## SQL para Análise de Dados e Gestão da Informação

**Curso:** Análise de Dados e TI Aplicado à Gestão  
**Módulo:** 3 - Big Data e Inteligência Artificial na tomada de decisões estratégicas  
**Exercício:** 1 - Exercício Prático – Introdução ao SQL  
**Plataforma de Exercícios:** [SQL Teaching](https://www.sqlteaching.com/)

---

## ÍNDICE

### [1. Consultas Básicas de Seleção (Desafios 1-5)](#1-consultas-básicas-de-seleção-desafios-1-5)
- [1.1. Desafio 1: Seleção completa de registros](#11-desafio-1-seleção-completa-de-registros)
- [1.2. Desafio 2: Seleção de colunas específicas](#12-desafio-2-seleção-de-colunas-específicas)
- [1.3. Desafio 3: Filtragem por espécie](#13-desafio-3-filtragem-por-espécie)
- [1.4. Desafio 4: Filtragem por quantidade (maior que)](#14-desafio-4-filtragem-por-quantidade-maior-que)
- [1.5. Desafio 5: Filtragem por quantidade (maior ou igual)](#15-desafio-5-filtragem-por-quantidade-maior-ou-igual)

### [2. Operadores Lógicos (Desafios 6-8)](#2-operadores-lógicos-desafios-6-8)
- [2.1. Desafio 6: Operador AND](#21-desafio-6-operador-and)
- [2.2. Desafio 7: Operador OR](#22-desafio-7-operador-or)
- [2.3. Desafio 8: Operador NOT IN](#23-desafio-8-operador-not-in)

### [3. Consultas com DISTINCT e ORDER BY (Desafios 9-11)](#3-consultas-com-distinct-e-order-by-desafios-9-11)
- [3.1. Desafio 9: Valores distintos com filtro](#31-desafio-9-valores-distintos-com-filtro)
- [3.2. Desafio 10: Ordenação descendente](#32-desafio-10-ordenação-descendente)
- [3.3. Desafio 11: Ordenação com limite](#33-desafio-11-ordenação-com-limite)

### [4. Funções de Agregação (Desafios 12-16)](#4-funções-de-agregação-desafios-12-16)
- [4.1. Desafio 12: Contagem total de registros](#41-desafio-12-contagem-total-de-registros)
- [4.2. Desafio 13: Contagem condicional](#42-desafio-13-contagem-condicional)
- [4.3. Desafio 14: Soma de valores](#43-desafio-14-soma-de-valores)
- [4.4. Desafio 15: Média aritmética](#44-desafio-15-média-aritmética)
- [4.5. Desafio 16: Valor máximo](#45-desafio-16-valor-máximo)

### [5. Agrupamento e Subconsultas (Desafios 17-19)](#5-agrupamento-e-subconsultas-desafios-17-19)
- [5.1. Desafio 17: GROUP BY com função agregada](#51-desafio-17-group-by-com-função-agregada)
- [5.2. Desafio 18: Subconsulta para valor máximo](#52-desafio-18-subconsulta-para-valor-máximo)
- [5.3. Desafio 19: Filtro de valores não nulos](#53-desafio-19-filtro-de-valores-não-nulos)

### [6. Operações com Datas (Desafio 20)](#6-operações-com-datas-desafio-20)
- [6.1. Desafio 20: Comparação de datas](#61-desafio-20-comparação-de-datas)

### [7. Joins entre Tabelas (Desafios 21-27)](#7-joins-entre-tabelas-desafios-21-27)
- [7.1. Desafio 21: INNER JOIN simples](#71-desafio-21-inner-join-simples)
- [7.2. Desafio 22: INNER JOIN múltiplo](#72-desafio-22-inner-join-múltiplo)
- [7.3. Desafio 23: JOIN com múltiplos filtros](#73-desafio-23-join-com-múltiplos-filtros)
- [7.4. Desafio 24: LEFT JOIN múltiplo](#74-desafio-24-left-join-múltiplo)
- [7.5. Desafio 25: Aliases em tabelas](#75-desafio-25-aliases-em-tabelas)
- [7.6. Desafio 26: Aliases em colunas](#76-desafio-26-aliases-em-colunas)
- [7.7. Desafio 27: Auto-relacionamento (Self Join)](#77-desafio-27-auto-relacionamento-self-join)

### [8. Operações Avançadas de Texto (Desafios 28-31)](#8-operações-avançadas-de-texto-desafios-28-31)
- [8.1. Desafio 28: Pattern matching com LIKE](#81-desafio-28-pattern-matching-com-like)
- [8.2. Desafio 29: Expressões CASE](#82-desafio-29-expressões-case)
- [8.3. Desafio 30: Função SUBSTR](#83-desafio-30-função-substr)
- [8.4. Desafio 31: Função COALESCE](#84-desafio-31-função-coalesce)

### [9. Conclusão](#9-conclusão)

---

## 1. CONSULTAS BÁSICAS DE SELEÇÃO (DESAFIOS 1-5)

### 1.1. Desafio 1: Seleção Completa de Registros

**Objetivo:** Retornar todos os registros e todas as colunas de uma tabela.

**Resposta:**
```sql
SELECT * FROM family_members;
```

**Conceito aplicado:** Utilização do asterisco (*) para selecionar todas as colunas disponíveis na tabela `family_members`.

---

### 1.2. Desafio 2: Seleção de Colunas Específicas

**Objetivo:** Retornar apenas colunas específicas de uma tabela.

**Resposta:**
```sql
SELECT name, species FROM family_members;
```

**Conceito aplicado:** Seleção explícita de colunas específicas (name e species), otimizando a consulta e melhorando a legibilidade dos resultados.

---

### 1.3. Desafio 3: Filtragem por Espécie

**Objetivo:** Filtrar registros com base em um valor específico.

**Resposta:**
```sql
SELECT * FROM family_members WHERE species = 'dog';
```

**Conceito aplicado:** Cláusula WHERE para filtrar registros que atendem a uma condição específica (espécie igual a 'dog').

---

### 1.4. Desafio 4: Filtragem por Quantidade (Maior Que)

**Objetivo:** Filtrar registros utilizando operador de comparação numérica.

**Resposta:**
```sql
SELECT * FROM family_members WHERE num_books_read > 190;
```

**Conceito aplicado:** Operador de comparação (>) para filtrar registros onde o número de livros lidos é maior que 190.

---

### 1.5. Desafio 5: Filtragem por Quantidade (Maior ou Igual)

**Objetivo:** Filtrar registros utilizando operador de comparação inclusivo.

**Resposta:**
```sql
SELECT * FROM family_members WHERE num_books_read >= 180;
```

**Conceito aplicado:** Operador de comparação (>=) para incluir valores iguais ou maiores que o limite especificado.

---

## 2. OPERADORES LÓGICOS (DESAFIOS 6-8)

### 2.1. Desafio 6: Operador AND

**Objetivo:** Combinar múltiplas condições que devem ser verdadeiras simultaneamente.

**Resposta:**
```sql
SELECT * FROM friends_of_pickles 
WHERE species = 'dog' AND height_cm < 45;
```

**Conceito aplicado:** Operador lógico AND para filtrar registros que satisfazem ambas as condições (cães com altura inferior a 45 cm).

---

### 2.2. Desafio 7: Operador OR

**Objetivo:** Combinar condições onde pelo menos uma deve ser verdadeira.

**Resposta:**
```sql
SELECT * FROM friends_of_pickles 
WHERE species = 'dog' OR height_cm < 45;
```

**Conceito aplicado:** Operador lógico OR para filtrar registros que atendem a pelo menos uma das condições especificadas.

---

### 2.3. Desafio 8: Operador NOT IN

**Objetivo:** Excluir registros que correspondam a valores específicos.

**Resposta:**
```sql
SELECT * FROM friends_of_pickles 
WHERE species NOT IN ('cat', 'dog');
```

**Conceito aplicado:** Operador NOT IN para excluir múltiplos valores de uma só vez, simplificando a consulta.

---

## 3. CONSULTAS COM DISTINCT E ORDER BY (DESAFIOS 9-11)

### 3.1. Desafio 9: Valores Distintos com Filtro

**Objetivo:** Retornar valores únicos de uma coluna com condição aplicada.

**Resposta:**
```sql
SELECT DISTINCT species FROM friends_of_pickles 
WHERE height_cm > 50;
```

**Conceito aplicado:** Palavra-chave DISTINCT para eliminar duplicatas nos resultados, combinada com filtro WHERE.

---

### 3.2. Desafio 10: Ordenação Descendente

**Objetivo:** Ordenar resultados do maior para o menor valor.

**Resposta:**
```sql
SELECT * FROM friends_of_pickles 
ORDER BY height_cm DESC;
```

**Conceito aplicado:** Cláusula ORDER BY com DESC para ordenação decrescente dos valores.

---

### 3.3. Desafio 11: Ordenação com Limite

**Objetivo:** Retornar apenas o primeiro registro após ordenação.

**Resposta:**
```sql
SELECT * FROM friends_of_pickles 
ORDER BY height_cm DESC 
LIMIT 1;
```

**Conceito aplicado:** Combinação de ORDER BY e LIMIT para obter o registro com o maior valor de altura.

---

## 4. FUNÇÕES DE AGREGAÇÃO (DESAFIOS 12-16)

### 4.1. Desafio 12: Contagem Total de Registros

**Objetivo:** Contar o número total de registros em uma tabela.

**Resposta:**
```sql
SELECT COUNT(*) FROM friends_of_pickles;
```

**Conceito aplicado:** Função COUNT(*) para contar todos os registros da tabela.

---

### 4.2. Desafio 13: Contagem Condicional

**Objetivo:** Contar registros que atendem a uma condição específica.

**Resposta:**
```sql
SELECT COUNT(*) FROM friends_of_pickles 
WHERE species = 'dog';
```

**Conceito aplicado:** Combinação de COUNT com WHERE para contagem condicional.

---

### 4.3. Desafio 14: Soma de Valores

**Objetivo:** Calcular a soma total de valores numéricos.

**Resposta:**
```sql
SELECT SUM(num_books_read) FROM family_members;
```

**Conceito aplicado:** Função SUM() para agregação de valores numéricos, retornando o total de livros lidos.

---

### 4.4. Desafio 15: Média Aritmética

**Objetivo:** Calcular a média de valores numéricos.

**Resposta:**
```sql
SELECT AVG(num_books_read) FROM family_members;
```

**Conceito aplicado:** Função AVG() para calcular a média aritmética dos livros lidos.

---

### 4.5. Desafio 16: Valor Máximo

**Objetivo:** Identificar o maior valor em uma coluna numérica.

**Resposta:**
```sql
SELECT MAX(num_books_read) FROM family_members;
```

**Conceito aplicado:** Função MAX() para retornar o valor máximo encontrado na coluna.

---

## 5. AGRUPAMENTO E SUBCONSULTAS (DESAFIOS 17-19)

### 5.1. Desafio 17: GROUP BY com Função Agregada

**Objetivo:** Agrupar dados e aplicar função agregada em cada grupo.

**Resposta:**
```sql
SELECT MAX(height_cm), species
FROM friends_of_pickles 
GROUP BY species;
```

**Conceito aplicado:** Cláusula GROUP BY para agrupar registros por espécie e calcular a altura máxima de cada grupo.

---

### 5.2. Desafio 18: Subconsulta para Valor Máximo

**Objetivo:** Utilizar subconsulta para filtrar registros com base em valor agregado.

**Resposta:**
```sql
SELECT * FROM family_members 
WHERE num_books_read = (SELECT MAX(num_books_read) FROM family_members);
```

**Conceito aplicado:** Subconsulta (subquery) no WHERE para identificar o registro com o maior número de livros lidos.

---

### 5.3. Desafio 19: Filtro de Valores Não Nulos

**Objetivo:** Filtrar registros excluindo valores nulos.

**Resposta:**
```sql
SELECT * FROM family_members 
WHERE favorite_book IS NOT NULL;
```

**Conceito aplicado:** Operador IS NOT NULL para filtrar registros que possuem valor definido na coluna.

---

## 6. OPERAÇÕES COM DATAS (DESAFIO 20)

### 6.1. Desafio 20: Comparação de Datas

**Objetivo:** Filtrar registros com base em comparação de datas.

**Resposta:**
```sql
SELECT * FROM celebs_born 
WHERE birthdate > '1980-09-01';
```

**Conceito aplicado:** Comparação de datas utilizando formato ISO (YYYY-MM-DD) para filtrar nascimentos posteriores a setembro de 1980.

---

## 7. JOINS ENTRE TABELAS (DESAFIOS 21-27)

### 7.1. Desafio 21: INNER JOIN Simples

**Objetivo:** Relacionar duas tabelas através de chave estrangeira.

**Resposta:**
```sql
SELECT character.name, character_actor.actor_name
FROM character
INNER JOIN character_actor
ON character.id = character_actor.character_id;
```

**Conceito aplicado:** INNER JOIN para combinar dados de duas tabelas relacionadas, retornando apenas registros com correspondência em ambas.

---

### 7.2. Desafio 22: INNER JOIN Múltiplo

**Objetivo:** Relacionar três tabelas simultaneamente.

**Resposta:**
```sql
SELECT character.name, actor.name
FROM character
INNER JOIN character_actor
ON character.id = character_actor.character_id
INNER JOIN actor
ON character_actor.actor_id = actor.id;
```

**Conceito aplicado:** Múltiplos INNER JOINs para navegar por uma tabela intermediária (character_actor) e conectar personagens aos atores.

---

### 7.3. Desafio 23: JOIN com Múltiplos Filtros

**Objetivo:** Combinar joins com filtros complexos.

**Resposta:**
```sql
SELECT character.name, tv_show.name
FROM character
INNER JOIN character_tv_show
ON character.id = character_tv_show.character_id
INNER JOIN tv_show
ON character_tv_show.tv_show_id = tv_show.id 
WHERE character.name != 'Willow Rosenberg' 
AND tv_show.name != 'How I Met Your Mother';
```

**Conceito aplicado:** Combinação de múltiplos JOINs com cláusula WHERE contendo múltiplas exclusões.

---

### 7.4. Desafio 24: LEFT JOIN Múltiplo

**Objetivo:** Incluir todos os registros da tabela principal, mesmo sem correspondência.

**Resposta:**
```sql
SELECT character.name, actor.name
FROM character
LEFT JOIN character_actor
ON character.id = character_actor.character_id
LEFT JOIN actor
ON character_actor.actor_id = actor.id;
```

**Conceito aplicado:** LEFT JOIN para manter todos os personagens no resultado, mesmo aqueles sem ator associado.

---

### 7.5. Desafio 25: Aliases em Tabelas

**Objetivo:** Simplificar consultas utilizando apelidos para tabelas.

**Resposta:**
```sql
SELECT c.name, a.name
FROM character AS c
LEFT JOIN character_actor AS ca
ON c.id = ca.character_id
LEFT JOIN actor AS a
ON ca.actor_id = a.id;
```

**Conceito aplicado:** Uso de aliases (AS) para criar nomes abreviados de tabelas, melhorando a legibilidade.

---

### 7.6. Desafio 26: Aliases em Colunas

**Objetivo:** Renomear colunas no resultado para maior clareza.

**Resposta:**
```sql
SELECT c.name AS character, a.name AS actor
FROM character AS c
LEFT JOIN character_actor AS ca
ON c.id = ca.character_id
LEFT JOIN actor AS a
ON ca.actor_id = a.id;
```

**Conceito aplicado:** Aliases em colunas para diferenciar campos com mesmo nome provenientes de tabelas distintas.

---

### 7.7. Desafio 27: Auto-relacionamento (Self Join)

**Objetivo:** Relacionar uma tabela consigo mesma.

**Resposta:**
```sql
SELECT e.name AS employee_name, b.name AS boss_name
FROM employees AS e
INNER JOIN employees AS b
ON e.boss_id = b.id;
```

**Conceito aplicado:** Self Join para criar relacionamento hierárquico entre funcionários e seus superiores na mesma tabela.

---

## 8. OPERAÇÕES AVANÇADAS DE TEXTO (DESAFIOS 28-31)

### 8.1. Desafio 28: Pattern Matching com LIKE

**Objetivo:** Buscar padrões específicos em strings.

**Resposta:**
```sql
SELECT * FROM robots 
WHERE name LIKE '%Robot 20__';
```

**Conceito aplicado:** Operador LIKE com wildcards (% para múltiplos caracteres, _ para um caractere) para busca de padrões.

---

### 8.2. Desafio 29: Expressões CASE

**Objetivo:** Criar lógica condicional dentro da consulta.

**Resposta:**
```sql
SELECT *,
CASE 
    WHEN species = 'human' THEN 'talk'
    WHEN species = 'dog' THEN 'bark' 
    WHEN species = 'cat' THEN 'meow'
END AS sound
FROM friends_of_pickles;
```

**Conceito aplicado:** Expressão CASE para criar coluna calculada com base em condições múltiplas, similar a estruturas IF-THEN-ELSE.

---

### 8.3. Desafio 30: Função SUBSTR

**Objetivo:** Extrair parte de uma string.

**Resposta:**
```sql
SELECT * FROM robots 
WHERE SUBSTR(location, -2) = 'NY';
```

**Conceito aplicado:** Função SUBSTR com índice negativo para extrair os últimos caracteres de uma string.

---

### 8.4. Desafio 31: Função COALESCE

**Objetivo:** Retornar o primeiro valor não nulo de uma lista.

**Resposta:**
```sql
SELECT name, COALESCE(tank, gun, sword) AS weapon 
FROM fighters;
```

**Conceito aplicado:** Função COALESCE para tratamento de valores nulos, retornando a primeira arma disponível na ordem de prioridade.

---

## 9. CONCLUSÃO

O Exercício 1 do Módulo 3 apresentou uma progressão estruturada e abrangente dos conceitos fundamentais e avançados de SQL (Structured Query Language), demonstrando a aplicabilidade prática da linguagem na análise de dados e na gestão da informação.

---

**Documento elaborado para o Curso de Análise de Dados e TI Aplicado à Gestão**  
**Módulo 3 - Exercício 1: Fundamentos de SQL**