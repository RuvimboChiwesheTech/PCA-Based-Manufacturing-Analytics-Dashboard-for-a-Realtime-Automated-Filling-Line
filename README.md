# PCA‑Based Manufacturing Analytics Dashboard for an Automated Filling Line

This project applies Principal Component Analysis (PCA) to real-world automated filling line data to uncover variability, detect anomalies, and support continuous improvement. The final deliverable is an interactive dashboard that visualises PCA insights, process stability, and early warning indicators.

All data in this repository is anonymised and modified to protect confidentiality.

## Project Overview
Modern automated filling lines generate large volumes of sensor and process data. Traditional univariate control charts often fail to capture the complex, multivariate relationships that drive process behaviour.

This project uses:

- PCA to reduce dimensionality  
- Hotelling’s T² and Q‑residuals for anomaly detection  
- Clustering to group similar process behaviours  
- Interactive visualisation to support root‑cause analysis  

The dashboard enables engineers and analysts to monitor process health in real time and identify deviations before they escalate into rejects or downtime.

## Key Features

### Data Explorer
Browse cleaned process data, inspect variables, and understand the dataset structure.

### PCA Insights
- PCA scores and loadings  
- T² and Q‑residuals  
- Anomaly flags  
- Timestamp, reject type, and part ID filtering  
- Cluster-level behaviour  

### KPI Summary
- Total parts processed  
- Total anomalies  
- Percentage out of control  
- Most common reject type  

## Modular Code Structure
- `src/` contains reusable PCA utilities  
- `notebooks/` contains preprocessing and PCA modelling  
- `app/` contains the Streamlit dashboard  
- `data/` contains raw and processed datasets

- ## Visual Representation of Key Features
- The following screenshots illustrate key components of the dashboard interface:
<img width="707" height="369" alt="Image" src="https://github.com/user-attachments/assets/b5fb055d-fabf-40d9-b663-d133a4daea25" />
<img width="720" height="312" alt="Image" src="https://github.com/user-attachments/assets/7d9fbb7f-258f-44cc-8a7d-81cc16b4a329" />
<img width="711" height="382" alt="Image" src="https://github.com/user-attachments/assets/c36eef93-d449-4097-82a6-7ae87a9ed61b" />
<!-- Uploading "pca_score_plot.PNG"... -->
<img width="703" height="378" alt="Image" src="https://github.com/user-attachments/assets/b5efcb45-9eee-40b2-b618-bed503f93f93" />
<img width="719" height="391" alt="Image" src="https://github.com/user-attachments/assets/62883ba7-976a-4450-8150-0eea15a09136" />

## Repository Structure

PCA-Based-Manufacturing-Analytics-Dashboard
 ┣  app
 ┃ ┗ app.py
 ┣  data
 ┃ ┣  raw
 ┃ ┣  processed
 ┃ ┃ ┣ cleaned_data.csv
 ┃ ┃ ┗ pca_results.csv
 ┣  notebooks
 ┃ ┣ 01_data_preprocessing.ipynb
 ┃ ┗ pca_analysis.ipynb
 ┣  src
 ┃ ┗ pca_utils.py
 ┣ README.md
 ┗ requirements.txt

## How to Run the Dashboard

### 1. Clone the repository

 git clone https://github.com/RuvimboChiwesheTech/PCA-Based-Manufacturing-Analytics-Dashboard-for-a-Realtime-Automated-Filling-Line
cd PCA-Based-Manufacturing-Analytics-Dashboard-for-a-Realtime-Automated-Filling-Line

### 2. Install dependencies
pip install -r requirements.txt

### 3. Launch the Streamlit app
streamlit run app.py

## Data Processing & PCA Modelling

The PCA workflow includes:

- Data cleaning and preprocessing  
- Scaling and standardisation  
- PCA decomposition  
- Calculation of T² and Q‑residuals  
- Setting statistical control limits  
- Generating anomaly flags  
- Exporting results to `pca_results.csv`  

All modelling steps are documented in the Jupyter notebooks.

## Future Enhancements

- Add PCA score plots and loading plots  
- Add anomaly timelines  
- Add cluster visualisation  
- Add reject‑type drill‑downs  
- Add model retraining pipeline  
- Deploy dashboard to Streamlit Cloud or Azure  

## Author
**Ruvimbo Chiweshe**  
MSc Computing (Data Science)  
Passionate about data analytics, manufacturing intelligence, and building real‑world data products.
