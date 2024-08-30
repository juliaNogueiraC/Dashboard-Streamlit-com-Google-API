import streamlit as st
import pandas as pd
import plotly.express as px
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import os

# Set up Google Sheets API
def get_google_sheets_data():
    # Load credentials from the JSON file
    creds = Credentials.from_service_account_file(
        '/workspace/Dashboard-Streamlit-com-Google-API/rh.json',
        scopes=['https://www.googleapis.com/auth/spreadsheets.readonly']
    )

    # Build the service
    service = build('sheets', 'v4', credentials=creds)

    # ID of your Google Sheet
    SPREADSHEET_ID = '1OjN2OjLFECGCXJ14sCWWXXHzx-USCMbH03SAWEuAvEk'
    RANGE_NAME = 'entrevistas!C:D'  # Adjust this to match your sheet's structure

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        st.error('No data found in the Google Sheet.')
        return pd.DataFrame()

    # Convert to DataFrame
    df = pd.DataFrame(values[1:], columns=values[0])
    return df

def main():
    st.title("Employee Turnover Dashboard")

    # Fetch data from Google Sheets
    data = get_google_sheets_data()

    if not data.empty:
        # Chart 1: MOTIVO DO DESLIGAMENTO (Horizontal Bar Chart)
        st.header("Motivo do Desligamento")
        motivo_counts = data['MOTIVO DO DESLIGAMENTO'].value_counts()
        fig_motivo = px.bar(
            x=motivo_counts.values,
            y=motivo_counts.index,
            orientation='h',
            title="Distribuição dos Motivos de Desligamento",
            labels={'x': 'Contagem', 'y': 'Motivo'}
        )
        st.plotly_chart(fig_motivo)

        # Chart 2: Quantidade de Demissões por Setor (Pie Chart)
        st.header("Quantidade de Pedidos de Demissão por Setor")
        demissoes_por_setor = data['SETOR'].value_counts()
        fig_setor = px.pie(
            values=demissoes_por_setor.values,
            names=demissoes_por_setor.index,
            title="Quantidade de Pedidos de Demissão por Setor"
        )
        st.plotly_chart(fig_setor)


    else:
        st.write("No data available. Please check your Google Sheet.")

    

          # Add a button to refresh the dashboard
    if st.button("Refresh Dashboard"):
        st.experimental_rerun()
        

if __name__ == "__main__":
    main()