import panel as pn


# This view has no specific controls, so we return an empty pane
def controls():
    return pn.pane.Markdown("No portfolio-level controls yet.")


# The main content for the portfolio view
def view():
    return pn.Column(
        "## Portfolio Level Overview",
        "This page will contain aggregated metrics for all funds.",
        pn.pane.Alert(
            "Portfolio-level charts and tables to be implemented here.",
            alert_type="info",
        ),
    )
