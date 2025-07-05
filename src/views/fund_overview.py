import panel as pn

from src.components.charts.performance import PerformanceChart
from src.models.factory import get_available_funds
from src.state import global_fund_view_state


def controls(state_obj=global_fund_view_state):
    """
    The view layer is responsible for presentation. It takes the raw state
    and declaratively builds a UI for it, specifying the widget and its options.
    """
    fund_controls_pane = pn.Param(
        state_obj.param,  # Target the state object
        parameters=["selected_fund_id"],  # Pick which state parameter to show
        # Explicitly configure the UI widget for this parameter
        widgets={
            "selected_fund_id": {
                "type": pn.widgets.Select,
                "options": get_available_funds(),
            }
        },
    )

    return pn.Column(pn.pane.Markdown("### Fund Controls"), fund_controls_pane)


# A function that returns the main content of the view
def view(state_obj=global_fund_view_state):
    """
    A function that builds and returns the main content for this view.
    This function is called every time the user navigates to this page.
    """
    # The components will automatically react to state changes initiated by the selector
    perf_chart_component = PerformanceChart(state_obj=state_obj)

    # Define the layout for this specific view
    layout = pn.Column(
        "## Fund Deep Dive",
        "This page shows detailed information for a single, selected fund.",
        pn.layout.Divider(),
        perf_chart_component,
        # You would add other components like MetricsTable() here as well.
    )

    # Return the newly created layout.
    return layout
