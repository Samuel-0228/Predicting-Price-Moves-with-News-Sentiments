# Financial News Sentiment Analysis - Final Submission

## Overview
Week 1 full pipeline: EDA (Task 1), indicators (Task 2), correlations (Task 3) on `raw_analyst_ratings.csv`. Modular class-based utils in `src/`. Insights: Sentiment r=0.15–0.18 with returns.

## Setup
1. Clone: `git clone https://github.com/Samuel-0228/Predicting-Price-Moves-with-News-Sentiments.git`
2. `pip install -r requirements.txt`
3. LFS: `git lfs pull` (data).
4. Pipeline: `python src/main.py` (runs full analysis).
5. Notebooks: `jupyter notebook notebooks/01_news_eda.ipynb` (step-by-step).
6. Tests: `pytest tests/ -v` (CI green).

## Structure
- `src/utils/`: Class-based modules (data load, sentiment, indicators, corr).
- Notebooks: Numbered (01 EDA → 02 Tech → 03 Corr).
- Outputs: Plots in root (e.g., `output3.png`).

## Branches
- `main`: Merged (PRs for tasks).


## Report
`reports/final_report.md` (export PDF).

References: [Investopedia](https://www.investopedia.com/terms/s/stockmarket.asp), [PyNance](https://github.com/mqandil/pynance).
