import streamlit as st
import pandas as pd
from pathlib import Path

st.title("Ouvidoria Smart Insights — Demo")
p = Path("data/reclamacoes_clean.csv")
if not p.exists():
    st.error("Execute o pipeline primeiro (ETL e treino).")
else:
    df = pd.read_csv(p)
    st.metric("Tickets (amostra)", len(df))
    st.bar_chart(df["produto"].value_counts())
    st.dataframe(df[["id","canal","produto","nps","texto_reclamacao"]].head(20))

