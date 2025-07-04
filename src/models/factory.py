import asyncio
import pandas as pd
import numpy as np

# A simplified mock data provider
async def get_performance_data(fund_id: str):
    """Simulates a slow network/DB call."""
    await asyncio.sleep(1)
    dates = pd.to_datetime(pd.date_range(end='today', periods=365, freq='D'))
    price_series = (1 + np.random.randn(len(dates), 1) * 0.05).cumprod() * 100
    return pd.DataFrame(price_series, index=dates, columns=[fund_id])

def get_available_funds():
    """Returns a dictionary of fund_id -> fund_name."""
    return {
        "FUND_A": "Global Tech Leaders",
        "FUND_B": "Emerging Markets Bond",
        "FUND_C": "Sustainable Energy Fund",
    }