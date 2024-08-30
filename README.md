# Dashboard Streamlit com Google API
Este script combina FastAPI para a funcionalidade da API e Streamlit para o dashboard. Aqui está uma descrição do código:

1. Importamos as bibliotecas necessárias: Streamlit para o dashboard, pandas para manipulação de dados, plotly para visualização e FastAPI para a API.

2. Definimos um aplicativo FastAPI e um modelo Pydantic para validação de dados.

3. Criamos dois endpoints de API:
    - /add_employee_data: Para adicionar novos dados de funcionários
    - /get_employee_data: Para recuperar todos os dados de funcionários

4. O aplicativo Streamlit busca dados da API e cria dois gráficos:

    - Um gráfico de pizza mostrando a distribuição de "MOTIVO DO DESLIGAMENTO"
    - Um gráfico de barras mostrando "SETOR por motivo"
    - Há um botão de atualização para atualizar o dashboard com os dados mais recentes.

Para executar esta aplicação, você precisará:

1. Instalar as bibliotecas necessárias: streamlit, pandas, plotly, fastapi e uvicorn.
2. Salvar o script como app.py.
3. Executar o servidor FastAPI: uvicorn app:app --reload.
4. Em um terminal separado, executar o aplicativo Streamlit: streamlit run app.py.

O dashboard será atualizado automaticamente à medida que novos dados forem adicionados através da API.

## Como conectar com API:
Para usar este código e conectar-se a uma planilha do Google, você precisará seguir estes passos:

1. Configure uma conta de serviço do Google Cloud:

- Vá para o Google Cloud Console (https://console.cloud.google.com/)
- Crie um novo projeto ou selecione um existente
- Habilite a API do Google Sheets para o projeto
- Crie uma conta de serviço e baixe o arquivo JSON com as credenciais


2. Compartilhe sua planilha do Google com o endereço de e-mail da conta de serviço (encontrado no arquivo JSON de credenciais).

3. No código:

- Substitua 'path/to/your/service_account.json' pelo caminho real para o seu arquivo JSON de credenciais.
- Substitua 'your_spreadsheet_id_here' pelo ID da sua planilha do Google (você pode encontrá-lo na URL da planilha).
- Ajuste RANGE_NAME = 'Sheet1!A:B' para corresponder à estrutura da sua planilha.

## Instalando Bibliotecas necessárias:
```bash
  pip install streamlit pandas plotly google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

## como executar:
no terminal execute:
```bash
  streamlit run app.py
```