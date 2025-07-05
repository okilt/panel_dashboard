import hvplot.pandas
import panel as pn

from src.models.factory import get_performance_data

pn.extension()


class PerformanceChart(pn.viewable.Viewer):
    def __init__(self, state_obj, **params):
        self.state = state_obj
        super().__init__(**params)

        # This component's view is bound to the passed-in state's parameter
        self._view = pn.panel(
            pn.bind(self._get_plot, fund_id=self.state.param.selected_fund_id)
        )

    async def _get_plot(self, fund_id):
        yield pn.indicators.LoadingSpinner(
            value=True, width=50, height=50, align="center"
        )
        perf_df = await get_performance_data(fund_id)
        plot = perf_df.hvplot.line(
            title=f"Performance for {fund_id}", height=350, responsive=True, grid=True
        ).opts(yformatter="%.2f")
        yield plot

    def __panel__(self):
        return self._view
