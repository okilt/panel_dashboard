import panel as pn
from src.state import state
from src.models.factory import get_available_funds
from src.components.charts.performance import PerformanceChart

# This is the "controller" widget that modifies the global state
fund_selector = pn.widgets.Select(
    name="Select Fund", 
    options=get_available_funds(),
    # The widget's value is bidirectionally linked to the global state
    value=state.param.selected_fund_id 
)

# Instantiate the components needed for this view
# The components will automatically react to state changes initiated by the selector
perf_chart_component = PerformanceChart()

# Define the layout for this specific view
layout = pn.Column(
    "## Fund Deep Dive",
    "This page shows detailed information for a single, selected fund.",
    pn.layout.Divider(),
    perf_chart_component,
    # You would add MetricsTable, etc., here, also linked to state.
)

# A function that returns the controls for this view
def controls():
    return pn.Column(
        pn.pane.Markdown("### Fund Controls"),
        fund_selector
    )

# A function that returns the main content of the view
def view():
    return layout