import pandas as pd
import re
import os

def limpar_texto(txt: str) -> str:
    txt = str(txt).lower()
    txt = re.sub(r"[^a-z0-9à-ú\s]", " ", txt)
    txt = re.sub(r"\s+", " ", txt).strip()
    return txt

if __name__ == "__main__":
    raw = "data/reclamacoes_raw.csv"
    if not os.path.exists(raw):
        raise FileNotFoundError("Execute primeiro: python src/etl_ingest.py")
    df = pd.read_csv(raw)
    df["texto_limpo"] = df["texto_reclamacao"].map(limpar_texto)
    df.to_csv("data/reclamacoes_clean.csv", index=False)
    print(" Arquivo limpo salvo: data/reclamacoes_clean.csv")


