import panel as pn

from src.state import FundViewState
from src.views import fund_overview, portfolio_level

AVAILABLE_VIEWS = {
    "Fund Overview": fund_overview,
    "Portfolio Level": portfolio_level,
}

# --- CONTROLS ---
# These widgets can be defined at the module level because they are simple,
# and their state is not managed by the view's lifecycle.
left_pane_selector = pn.widgets.Select(
    name="Select Left Pane View",
    options=list(AVAILABLE_VIEWS.keys()),
    value="Fund Overview",
)

right_pane_selector = pn.widgets.Select(
    name="Select Right Pane View",
    options=list(AVAILABLE_VIEWS.keys()),
    value="Portfolio Level",
)


def controls():
    """Returns the controls for the Split View page."""
    return pn.Column(
        pn.pane.Markdown("### Split View Controls"),
        left_pane_selector,
        right_pane_selector,
    )


# --- VIEW ---


def _get_split_panes(left_page_name, right_page_name):
    # Create two brand-new, independent state objects for this render.
    left_state = FundViewState()
    right_state = FundViewState()

    left_module = AVAILABLE_VIEWS[left_page_name]
    left_content = pn.Column(
        left_module.controls(state_obj=left_state),
        pn.layout.Divider(),
        left_module.view(state_obj=left_state),
    )

    right_module = AVAILABLE_VIEWS[right_page_name]
    right_content = pn.Column(
        right_module.controls(state_obj=right_state),
        pn.layout.Divider(),
        right_module.view(state_obj=right_state),
    )

    return pn.Row(
        left_content,
        pn.layout.VSpacer(width=1, styles={"background": "lightgray"}),
        right_content,
        sizing_mode="stretch_width",
        min_height=600,
    )


def view():
    """
    Builds and returns the main content for this view.
    This function is called every time the user navigates to this page.
    """
    # Create the dynamic, bound object here, inside the view function.
    # This ensures a fresh, clean object on every navigation.
    return pn.bind(
        _get_split_panes,
        left_page_name=left_pane_selector,
        right_page_name=right_pane_selector,
    )
