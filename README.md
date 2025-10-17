<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-informational" alt="Python 3.12">
  <img src="https://img.shields.io/badge/Scikit--learn-ML-blue" alt="scikit-learn">
  <img src="https://img.shields.io/badge/Streamlit-App-success" alt="Streamlit">
  <img src="https://img.shields.io/badge/CRISP--DM-Process-brightgreen" alt="CRISP-DM">
  <a href="#-licença"><img src="https://img.shields.io/badge/License-MIT-yellow" alt="MIT License"></a>
</p>

<h1 align="center">📊 Ouvidoria Smart Insights (-like)</h1>

<p align="center">
  Pipeline de Ouvidoria com <b>ETL → NLP (TF-IDF) → Classificação</b> e app <b>Streamlit</b>.<br/>
  Foco em prevenção de escalonamento à Ouvidoria e melhoria de experiência do cliente.
</p>

---

## 🧠 Tecnologias Utilizadas
- **Linguagem:** Python  
- **Bibliotecas:** Pandas, NumPy, Scikit-learn, SciPy, Matplotlib, NLTK, TextBlob, Streamlit  
- **Ambiente:** VSCode + Virtual Environment (.venv)  
- **Metodologia:** CRISP-DM (Cross Industry Standard Process for Data Mining)  

---

## ▶️ Como Executar o Projeto (Windows PowerShell)
```bash
# Criar ambiente virtual
python -m venv .venv

# Instalar dependências
.\.venv\Scripts\python -m pip install --upgrade pip
.\.venv\Scripts\pip install -r requirements.txt

# Rodar o pipeline ETL e modelo
.\.venv\Scripts\python src\etl_ingest.py
.\.venv\Scripts\python src\etl_transform.py
.\.venv\Scripts\python src\train_classifier.py

# Executar o app Streamlit
.\.venv\Scripts\python -m streamlit run app\Streamlit_demo.py
```
Acesse no navegador:
🔗 http://localhost:8501

📈 Resultados Obtidos (Base Sintética)
Métrica	Valor
AUC	0.68
Precision	0.00
Recall	0.00
F1-score	0.00
Precision@10%	0.30

ℹ️ Os dados são sintéticos e servem para demonstrar o processo completo (ETL → Model → App).

🖼️ Painel (Streamlit)
<p align="center"> <img src="app/screenshot.png" alt="Streamlit - Ouvidoria Smart Insights" width="800"/> </p>
🧩 Metodologia (CRISP-DM)

Entendimento do Negócio — reclamações críticas e reincidentes; objetivo: priorização preventiva.

Dados & Preparação — ETL com pandas; limpeza textual (regex, lower, etc).

Modelagem — TF-IDF (texto) + variáveis tabulares (tempo_resposta, reincidente, NPS); Regressão Logística.

Avaliação — AUC, Precision, Recall, F1 e Precision@10% (priorização da fila).

Entrega — app Streamlit para exploração e decisão do time de negócio.

🔧 Próximos Passos

Balancear classes e ajustar limiar de decisão (otimizar Recall em casos críticos).

Trocar base sintética por dados reais (manter mesmo pipeline).

Explicabilidade (SHAP/LIME) e curvas Precision-Recall.

Migrar para Databricks Community ou AWS (S3 + Athena) para operação enterprise.

👨‍💻 Autor

Marcos Barbosa (Elementar)
📍 Pós-graduação em Engenharia de Dados – UNOPAR
🎓 Formação Profissional em Ciência de Dados – EBAC
🌐 LinkedIn – barbosa-data
 · 🐙 GitHub – Barbo541

📜 Licença

Este projeto é disponibilizado sob a licença MIT. Consulte o arquivo LICENSE
 para detalhes.


## Arquivo LICENSE (crie `LICENSE` na raiz)
```text
MIT License

Copyright (c) 2025 Marcos Barbosa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```





