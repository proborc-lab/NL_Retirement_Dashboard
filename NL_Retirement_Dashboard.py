import streamlit as st
import pandas as pd
import plotly.express as px

# Data voor de prognoses (2025-2045)
# Deze data is gebaseerd op CBS-prognoses voor levensverwachting en AOW-leeftijd.
levensverwachting_prognose_2045 = {
    'Jaar': [2025, 2030, 2035, 2040, 2045],
    'Levensverwachting bij geboorte (jaren)': [83.5, 84.25, 85.5, 85.75, 86.0],
    'Levensverwachting op 65 jaar (jaren)': [20.1, 20.96, 21.0, 21.4, 21.8]
}

df_levensverwachting_prognose_2045 = pd.DataFrame(levensverwachting_prognose_2045)

gezonde_levensverwachting_prognose_2045 = {
    'Jaar': [2025, 2030, 2035, 2040, 2045],
    'Gezonde levensverwachting in goede gezondheid (jaren)': [78.5, 80.5, 82.0, 83.0, 84.0],
    'Gezonde levensverwachting zonder beperkingen (jaren)': [80.0, 82.0, 83.5, 84.5, 85.5]
}

df_gezonde_levensverwachting_prognose_2045 = pd.DataFrame(gezonde_levensverwachting_prognose_2045)

aow_leeftijd_prognose_2045 = {
    'Jaar': [2025, 2030, 2035, 2040, 2045],
    'AOW-leeftijd (jaren)': [67, 67.25, 67.75, 68, 68.25]  # 3 en 9 maanden omgerekend naar jaren
}

df_aow_leeftijd_prognose_2045 = pd.DataFrame(aow_leeftijd_prognose_2045)

# Titel van het dashboard
st.title('Interactief Dashboard: Levensverwachting en AOW-leeftijd (2025-2045)')

# Tabbladen voor verschillende onderwerpen
# Elke tab bevat een specifieke grafiek of dataset.
tab1, tab2, tab3, tab4 = st.tabs(["Levensverwachting bij geboorte", "Gezonde levensverwachting", "AOW-leeftijd", "Vergelijking"])

# Tab 1: Levensverwachting bij geboorte
with tab1:
    st.header("Levensverwachting bij geboorte (2025-2045)")
    # Maak een lijngrafiek met Plotly voor levensverwachting bij geboorte.
    fig1 = px.line(df_levensverwachting_prognose_2045, x='Jaar', y='Levensverwachting bij geboorte (jaren)',
                  title='Levensverwachting bij geboorte',
                  labels={'Levensverwachting bij geboorte (jaren)': 'Levensverwachting (jaren)', 'Jaar': 'Jaar'},
                  color_discrete_sequence=['#1f77b4'])  # Blauwe kleur voor deze grafiek
    fig1.update_traces(line=dict(width=3))  # Dikkere lijnen voor betere zichtbaarheid
    fig1.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))  # Legenda boven de grafiek
    st.plotly_chart(fig1, width=800)  # Gebruik de nieuwe syntax voor breedte

# Tab 2: Gezonde levensverwachting
with tab2:
    st.header("Gezonde levensverwachting bij geboorte (2025-2045)")
    # Maak een lijngrafiek met Plotly voor gezonde levensverwachting.
    fig2 = px.line(df_gezonde_levensverwachting_prognose_2045, x='Jaar',
                  y=['Gezonde levensverwachting in goede gezondheid (jaren)', 'Gezonde levensverwachting zonder beperkingen (jaren)'],
                  title='Gezonde levensverwachting',
                  labels={'value': 'Gezonde levensverwachting (jaren)', 'variable': 'Type', 'Jaar': 'Jaar'},
                  color_discrete_sequence=['#2ca02c', '#9467bd'])  # Groene en paarse kleuren
    fig2.update_traces(line=dict(width=3))
    fig2.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
    st.plotly_chart(fig2, width=800)

# Tab 3: AOW-leeftijd
with tab3:
    st.header("AOW-leeftijd (2025-2045)")
    # Maak een lijngrafiek met Plotly voor AOW-leeftijd.
    fig3 = px.line(df_aow_leeftijd_prognose_2045, x='Jaar', y='AOW-leeftijd (jaren)',
                  title='AOW-leeftijd',
                  labels={'AOW-leeftijd (jaren)': 'AOW-leeftijd (jaren)', 'Jaar': 'Jaar'},
                  color_discrete_sequence=['#ff7f0e'])  # Oranje kleur
    fig3.update_traces(line=dict(width=3))
    fig3.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
    st.plotly_chart(fig3, width=800)

# Tab 4: Vergelijking
with tab4:
    st.header("Vergelijking levensverwachting, gezonde levensverwachting en AOW-leeftijd (2025-2045)")
    # Combineer alle data voor een vergelijkende grafiek.
    comparison_data_2045 = pd.DataFrame({
        'Jaar': [2025, 2030, 2035, 2040, 2045],
        'Levensverwachting bij geboorte': [83.5, 84.25, 85.5, 85.75, 86.0],
        'Gezonde levensverwachting in goede gezondheid': [78.5, 80.5, 82.0, 83.0, 84.0],
        'Gezonde levensverwachting zonder beperkingen': [80.0, 82.0, 83.5, 84.5, 85.5],
        'Levensverwachting op 65 jaar + 65': [65 + 20.1, 65 + 20.96, 65 + 21.0, 65 + 21.4, 65 + 21.8],
        'AOW-leeftijd': [67, 67.25, 67.75, 68, 68.25]
    })
    # Maak een vergelijkende lijngrafiek.
    fig4 = px.line(comparison_data_2045, x='Jaar', y=comparison_data_2045.columns[1:],
                  title='Vergelijking levensverwachting, gezonde levensverwachting en AOW-leeftijd',
                  labels={'value': 'Jaren', 'variable': 'Onderwerp', 'Jaar': 'Jaar'},
                  color_discrete_sequence=['#1f77b4', '#2ca02c', '#9467bd', '#d62728', '#ff7f0e'])
    fig4.update_traces(line=dict(width=3))
    fig4.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
    st.plotly_chart(fig4, width=800)

# Toon de data in een expandable sectie
with st.expander("Bekijk de data"):
    st.write('### Levensverwachting bij geboorte')
    st.dataframe(df_levensverwachting_prognose_2045)

    st.write('### Gezonde levensverwachting')
    st.dataframe(df_gezonde_levensverwachting_prognose_2045)

    st.write('### AOW-leeftijd')
    st.dataframe(df_aow_leeftijd_prognose_2045)
