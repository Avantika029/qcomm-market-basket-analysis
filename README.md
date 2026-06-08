# Q-Comm Market Basket Analysis
> End-to-end MBA system inspired by Zepto, Blinkit, and Instamart

## What this project does
Builds a complete market basket analysis pipeline on 3.4M Instacart orders —
from raw data ingestion through association rule mining, advanced embedding models,
and a production-ready FastAPI recommendation endpoint.

## Progress
- [x] Phase 1: Data setup & EDA
- [ ] Phase 2: Apriori + FP-Growth
- [ ] Phase 3: Q-comm segmentation
- [ ] Phase 4: Advanced models (Prod2Vec, graph, ALS)
- [ ] Phase 5: FastAPI + Streamlit dashboard
- [ ] Phase 6: Portfolio polish

## Dataset
[Instacart Market Basket Analysis](https://www.kaggle.com/datasets/psparks/instacart-market-basket-analysis)
3.4M orders · 49K products · 206K users

## Setup
```bash
pip install -r requirements.txt
python -c "from src.data.loader import get_connection; get_connection()"
jupyter lab
```

## Key EDA findings (Phase 1)
- Median basket size: ~9 items (q-comm baskets are typically 5–8, so Instacart skews larger)
- 59% of all items are reorders — habitual buying dominates
- Strong weekly reorder cycle — 7-day and 30-day spikes
- Produce + dairy + snacks = 60%+ of all order volume