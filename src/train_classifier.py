import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, precision_recall_fscore_support
from scipy.sparse import hstack
import numpy as np
import os

def precision_at_k(y_true, y_prob, k=0.10):
    n = max(1, int(len(y_prob)*k))
    idx = np.argsort(y_prob)[::-1][:n]
    return (y_true[idx] == 1).mean()

if __name__ == "__main__":
    clean = "data/reclamacoes_clean.csv"
    if not os.path.exists(clean):
        raise FileNotFoundError("Execute antes: etl_ingest.py e etl_transform.py")

    df = pd.read_csv(clean)

    tfidf = TfidfVectorizer(max_features=2500, ngram_range=(1,2))
    X_txt = tfidf.fit_transform(df["texto_limpo"])
    X_num = df[["tempo_resposta_h","reincidente","nps"]].to_numpy()
    X = hstack([X_txt, X_num])
    y = df["vira_ouvidoria"].astype(int).values

    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    clf = LogisticRegression(max_iter=300)
    clf.fit(Xtr, ytr)
    prob = clf.predict_proba(Xte)[:,1]
    pred = (prob>=0.5).astype(int)

    auc = roc_auc_score(yte, prob)
    p, r, f1, _ = precision_recall_fscore_support(yte, pred, average="binary")
    p_at_10 = precision_at_k(yte, prob, 0.10)

    print(f" Treino OK | AUC={auc:.3f} | Precision={p:.3f} | Recall={r:.3f} | F1={f1:.3f} | P@10%={p_at_10:.3f}")


