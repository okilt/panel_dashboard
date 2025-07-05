import panel as pn

from src.views import fund_overview, portfolio_level

# Use FastListTemplate for a modern look with a sidebar
template = pn.template.FastListTemplate(
    site="Portfolio Dashboard",
    title="Overview",
    sidebar_width=300,
)

# --- Multi-page Routing Logic ---
# A dictionary mapping URL-friendly names to the view modules
PAGES = {
    "Fund Overview": fund_overview,
    "Portfolio Level": portfolio_level,
}


def get_content(page_name):
    page = PAGES[page_name]
    return page.view()


def get_sidebar(page_name):
    page = PAGES[page_name]
    return page.controls()


# The selector widget to switch between pages
page_selector = pn.widgets.Select(
    name="Select View",
    options=list(PAGES.keys()),
    value="Fund Overview",  # Default page
)

# Bind the main content and sidebar to the page_selector's value
# When the user selects a new page, the main area and sidebar will update
template.main.append(pn.panel(pn.bind(get_content, page_name=page_selector)))
template.sidebar.append(page_selector)
template.sidebar.append(pn.layout.Divider())
template.sidebar.append(pn.panel(pn.bind(get_sidebar, page_name=page_selector)))

# Make the template servable
template.servable()
