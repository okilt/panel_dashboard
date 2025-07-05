import param

from src.models.factory import get_available_funds


class GlobalState(param.Parameterized):
    """
    A state management class. It only holds the raw data and its type.
    """

    default_fund = next(iter(get_available_funds()))
    selected_fund_id = param.String(default=default_fund, label="Selected Fund")


state = GlobalState()
