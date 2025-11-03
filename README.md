# pipeline-analise-api-python
Projeto de análise de dados com Python, Requests e Pandas.

# Projeto 1: Analista de API com Python

Este projeto é um script de console que demonstra um pipeline de dados simples:
1.  **Coleta:** Consome dados ao vivo de uma API pública (jsonplaceholder).
2.  **Processamento:** Carrega os dados em uma estrutura de análise.
3.  **Análise:** Filtra os dados para responder a uma pergunta de negócio.

Este projeto foi desenvolvido como parte do meu aprendizado de Python, focando em habilidades de Engenharia e Análise de Dados.

---

### 🚀 Habilidades Demonstradas

* **Requisições de API:** Uso da biblioteca `requests` para fazer chamadas `GET` a um endpoint REST.
* **Análise de Dados:** Uso da biblioteca `pandas` para carregar dados JSON em um DataFrame e realizar filtragem de dados.
* **Robustez de Código:** Implementação de blocos `try/except` para lidar com erros de conexão e falhas na API.
* **Manipulação de Dados:** Conversão de dados do formato JSON para um DataFrame do `pandas`.
* **Ambiente Virtual:** (Este projeto foi executado em um ambiente `conda` para gerenciar dependências).

---

### ⚙️ Como Executar

1.  Clone este repositório.
2.  Crie e ative um ambiente virtual (ex: `conda create --name meu-env python=3.10`).
3.  Instale as dependências:
    ```sh
    pip install requests pandas
    ```
4.  Execute o script:
    ```sh
    python analista_api.py
    ```
