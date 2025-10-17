##  Tecnologias Utilizadas

- **Linguagem:** Python  
- **Bibliotecas:** Pandas, NumPy, Scikit-learn, SciPy, Matplotlib, NLTK, TextBlob, Streamlit  
- **Ambiente:** VSCode + Virtual Environment (.venv)  
- **Metodologia:** CRISP-DM (Cross Industry Standard Process for Data Mining)  

---

##  Como Executar o Projeto (Windows PowerShell)

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
 http://localhost:8501

 ##  Resultados Obtidos (Base Sintética)

| Métrica         | Valor |
|-----------------|------:|
| AUC             | 0.68  |
| Precision       | 0.00  |
| Recall          | 0.00  |
| F1-score        | 0.00  |
| Precision@10%   | 0.30  |

>  Os dados são sintéticos e servem para demonstrar o processo completo (ETL → Model → App).

##  Painel (Streamlit)

<p align="center">
  <img src="app/screenshot.png" alt="Streamlit - Ouvidoria Smart Insights" width="800"/>
</p>



 Próximos Passos
🔹 Balancear classes e ajustar limiar de decisão.

🔹 Substituir base sintética por dados reais de Ouvidoria.

🔹 Adicionar explicabilidade com SHAP ou LIME.

🔹 Migrar o pipeline para Databricks Community ou AWS S3.

 Autor
 Marcos Barbosa 
 Pós-graduação em Engenharia de Dados – UNOPAR
 Formação Profissional em Ciência de Dados – EBAC
 Especialista em Engenharia de Dados, MLOps e Ciência de Dados Aplicada a Negócios
 LinkedIn – barbosa-data
 GitHub – Barbo541






