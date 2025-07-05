import panel as pn

from src.state import global_fund_view_state


# This view has no specific controls, so we return an empty pane
def controls(state_obj=global_fund_view_state):
    return pn.pane.Markdown("No portfolio-level controls yet.")


# The main content for the portfolio view
def view(state_obj=global_fund_view_state):
    return pn.Column(
        "## Portfolio Level Overview",
        "This page will contain aggregated metrics for all funds.",
        pn.pane.Alert(
            "Portfolio-level charts and tables to be implemented here.",
            alert_type="info",
        ),
    )
