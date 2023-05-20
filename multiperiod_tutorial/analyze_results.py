from typing import List, Dict

import matplotlib
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter


def prepare_results(results: pd.DataFrame) -> pd.DataFrame:
    """Restructure and then return results"""
    results.index = results.index.astype(str).str.split(expand=True)
    results.index.names = ["from", "to", "year"]
    results.reset_index(inplace=True)

    results["from"] = results["from"].str.strip("(',")
    results["to"] = results["to"].str.strip(")',")
    results["year"] = results["year"].str.strip(")")
    results["label"] = results["from"] + "," + results["to"]
    results.set_index(["label", "year"], inplace=True)
    results.drop(columns=["from", "to"], inplace=True)

    return results


def plot_single_investment_variable_multiple_dfs(
    results_dfs: List[pd.DataFrame],
    variable_name: str,
    ylim: List = None,
    units: List = ["MW", "MWh"],
):
    """Plot investment results for list of given data frames"""
    for no, result_df in enumerate(results_dfs):
        plot_single_investment_variable(
            result_df, variable_name, ylim=ylim, unit=units[no]
        )


def plot_single_investment_variable(
    results: pd.DataFrame,
    variable_name: str,
    ylim: List = None,
    unit: str = "MW",
):
    """Plot a single investment-related variable from results data set"""
    ylabels = {
        "invest": "newly invested capacity",
        "old": "total decommissioned capacity",
        "old_end": "capacity decommissioned because of lifetime",
        "old_exo": "capacity decommissioned because after initial age",
        "total": "total installed capacity",
        "all": "overall installed capacity",
    }
    plot_data = results[[variable_name]].reset_index()
    plot_data = plot_data.pivot(
        index="label",
        columns="year",
        values=variable_name,
    )

    fig, ax = plt.subplots(figsize=(12, 5))
    create_single_plot(
        plot_data, variable_name, ax, ylabels, ylim=ylim, unit=unit
    )
    _ = plt.tight_layout()
    _ = plt.show()
    plt.close()


def create_single_plot(
    plot_data: pd.DataFrame,
    variable_name: str,
    ax: matplotlib.axes,
    ylabels: Dict,
    title: str = None,
    legend: bool = True,
    hide_axis: bool = False,
    ylim: List = None,
    unit: str = "MW",
):
    """Create one single investment results plot"""
    if legend:
        _ = plot_data.T.plot(kind="bar", stacked=True, ax=ax)
    else:
        _ = plot_data.T.plot(kind="bar", stacked=True, ax=ax, legend=False)

    if title:
        _ = ax.set_title(title)
    if legend:
        _ = plt.legend(loc="upper right")

    if hide_axis:
        _ = ax.get_xaxis().set_visible(False)
    else:
        _ = plt.xlabel("year")
        _ = ax.set_ylabel(f"{ylabels[variable_name]} in {unit}")

    if ylim:
        _ = ax.set_ylim(ylim)

    _ = ax.get_yaxis().set_major_formatter(
        FuncFormatter(lambda x, p: format(int(x), ","))
    )
