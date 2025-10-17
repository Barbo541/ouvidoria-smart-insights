import pandas as pd
import numpy as np
import os

def gerar_dados(n=1000):
    produtos = ["cartao", "conta", "emprestimo", "app"]
    canais = ["app", "telefone", "chat", "agencia", "email"]
    ufs = ["SP", "RJ", "MG", "BA", "PR", "RS", "SC", "PE", "CE", "DF"]

    causas = [
        "cobranca em duplicidade", "app travando na tela de pagamento",
        "transferencia nao executada no horario", "erro 502 ao contratar emprestimo",
        "fatura com tarifa nao informada", "aplicativo fecha sozinho",
        "atendimento demorado no telefone", "cartao bloqueado sem motivo",
        "limite reduzido sem aviso", "falha para gerar comprovante"
    ]

    rows = []
    rng = np.random.default_rng(42)
    for i in range(1, n+1):
        produto = rng.choice(produtos)
        canal = rng.choice(canais)
        uf = rng.choice(ufs)
        nps = int(np.clip(rng.normal(6, 2), 0, 10))
        trh = int(np.clip(rng.normal(24, 12), 1, 72))  # tempo resposta (h)
        reinc = int(rng.random() < 0.20)
        causa = rng.choice(causas)
        texto = f"{causa}"
        severo = int(any(k in texto for k in ["duplicidade", "bloqueado", "erro 502"]))
        prob = 0.10 + 0.15*severo + 0.10*reinc + 0.05*(nps < 4)
        prob = float(min(0.90, max(0.02, prob)))
        vira = int(rng.random() < prob)
        rows.append([i, produto, canal, uf, nps, trh, reinc, texto, vira])

    df = pd.DataFrame(rows, columns=[
        "id","produto","canal","uf","nps",
        "tempo_resposta_h","reincidente","texto_reclamacao","vira_ouvidoria"
    ])
    return df

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    gerar_dados(1000).to_csv("data/reclamacoes_raw.csv", index=False)
    print(" Arquivo gerado: data/reclamacoes_raw.csv")





