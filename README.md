# 📚 Projeto Inspira - Web Crawler

## Descrição

Este projeto é um Web Crawler desenvolvido com **Scrapy** para coletar informações de livros do site [Books to Scrape](http://books.toscrape.com/). Os dados extraídos são armazenados em um arquivo **JSON** e posteriormente exibidos em uma interface interativa criada com **Streamlit**.

Web scraping, também conhecido como web crawling, é uma ferramenta eficiente para coletar dados da web [1]. Com um web scraper, é possível extrair dados sobre produtos, grandes volumes de texto, dados quantitativos ou dados de sites sem uma API oficial [1]. O Scrapy framework é uma ferramenta poderosa para criar web scrapers em Python [2][4][5].

## 🛠 Tecnologias Utilizadas

- [**Python**](https://www.python.org/)
- [**Scrapy**](https://scrapy.org/) - Para realizar o web scraping [2][4][5]
- [**Streamlit**](https://streamlit.io/) - Para criar a interface web interativa
- [**Pandas**](https://pandas.pydata.org/) - Para manipulação e análise dos dados coletados

## 📂 Estrutura do Projeto

INSPIRA-TEST/
│-- scrapy_crawler/
│ ├── scrapy_crawler/
│ │ ├── spiders/
│ │ │ ├── crawling_spider.py # Spider para coletar dados do site
│ │ │ ├── init.py
│ │ ├── books.json # Arquivo gerado com os dados coletados
│ │ ├── items.py
│ │ ├── middlewares.py
│ │ ├── pipelines.py
│ │ ├── settings.py
│ │ ├── scrapy.cfg
│-- venv/ # Ambiente virtual do Python
│-- requirements.txt # Dependências do projeto
│-- streamlit_app.py # Interface do Streamlit para visualização dos dados


## 🚀 Como Executar o Projeto

1.  **Configurar o ambiente virtual**

    ```
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
    ```
2.  **Instalar dependências**

    ```
    pip install -r requirements.txt
    ```
3.  **Executar o Web Crawler**

    ```
    cd scrapy_crawler
    scrapy crawl booksscraper -o scrapy_crawler/books.json
    ```

    Isso irá coletar os dados do site e armazená-los no arquivo `books.json` [2].
4.  **Rodar a Interface no Streamlit**

    ```
    streamlit run streamlit_app.py
    ```

    Isso abrirá a interface no navegador, permitindo visualizar e interagir com os dados coletados.

## 🎯 Funcionalidades

-   **Coleta de dados de livros**: Extração de título, preço, disponibilidade, gênero e avaliação.
-   **Interface interativa**: Exibição dos dados coletados com filtros e métricas.
-   **Cálculo de preço médio**: Exibe o preço médio geral e por gênero.
-   **Distribuição de avaliações**: Apresenta a quantidade de livros por número de estrelas.

## 📌 Observações

-   O projeto roda em um ambiente virtual para evitar conflitos de dependências.
-   A interface só funcionará corretamente se houver um `books.json` gerado pelo Scrapy.
