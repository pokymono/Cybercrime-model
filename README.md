# Cybercrime-model
Cybercrime Prediction Using Statistical Models and Deep Learning

## Setup

1. Create and activate virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

## Usage

Run the data loader script to analyze cybercrime datasets:

```bash
python data_loader.py
```

This will:
- Load cybercrime datasets from 2016-2021 
- Display shape, data types and basic statistics for each year
- Compare datasets across years
- Show total unique data columns
