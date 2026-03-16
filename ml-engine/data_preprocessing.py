import pandas as pd


def clean_events(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=['user_id', 'product_id'])
    df['event_weight'] = df['event_type'].map({'view': 1, 'cart': 2, 'purchase': 5}).fillna(1)
    return df
