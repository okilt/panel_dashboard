import param
from src.models.factory import get_available_funds

class GlobalState(param.Parameterized):
    """Holds the shared, reactive state for the entire application."""
    
    # Get the first fund from our available funds as the default
    default_fund = next(iter(get_available_funds()))
    
    # Define the shared parameters
    selected_fund_id = param.String(default=default_fund, label="Selected Fund")

# Create a single, global instance that the rest of the app will import
state = GlobalState()