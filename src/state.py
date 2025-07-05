import param

from src.models.factory import get_available_funds


class FundViewState(param.Parameterized):
    """Holds the state for a single instance of a fund view."""

    selected_fund_id = param.String(
        default=next(iter(get_available_funds())), label="Selected Fund"
    )


global_fund_view_state = FundViewState()
