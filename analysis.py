import math
from typing import List, Dict, Tuple

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare the data for analysis and plotting.
    
    Args:
        df (pd.DataFrame): Input DataFrame containing raw data.
    
    Returns:
        pd.DataFrame: Processed DataFrame with additional columns.
    """
    df['t_log'] = df['logging_time'] - df['logging_time'].iloc[0]
    speeds_df = df[['t_log', 'vEgo', 'longitudinalPlan.speeds_16']].apply(pd.to_numeric, errors='coerce')
    speeds_df['speeds_16_filt'] = speeds_df['longitudinalPlan.speeds_16'].rolling(window=3).median()
    speeds_df['difference'] = speeds_df['speeds_16_filt'] - speeds_df['vEgo']
    return speeds_df

def plot_speeds(ax: plt.Axes, speeds_df: pd.DataFrame) -> None:
    """
    Plot the speed comparison between prediction and actual car speed.
    
    Args:
        ax (plt.Axes): Matplotlib Axes object to plot on.
        speeds_df (pd.DataFrame): DataFrame containing speed data.
    """
    ax.fill_between(speeds_df['t_log'], speeds_df['vEgo'], speeds_df['speeds_16_filt'], 
                    where=(speeds_df['speeds_16_filt'] >= speeds_df['vEgo']),
                    interpolate=True, alpha=0.3, color='green')
    ax.fill_between(speeds_df['t_log'], speeds_df['vEgo'], speeds_df['speeds_16_filt'], 
                    where=(speeds_df['speeds_16_filt'] < speeds_df['vEgo']),
                    interpolate=True, alpha=0.3, color='red')
    speeds_df.plot(x='t_log', y='speeds_16_filt', ax=ax, color='C1', label='AI', linewidth=1.5)
    speeds_df.plot(x='t_log', y='vEgo', ax=ax, color='C0', label='Human', linewidth=1.5)
    ax.set_ylabel('Speed (m/s)', fontsize=10)
    ax.legend(loc='upper right', fontsize=10)
    ax.set_ylim(-2,24)

def plot_difference(ax: plt.Axes, speeds_df: pd.DataFrame) -> None:
    """
    Plot the difference between predicted and actual speeds.
    
    Args:
        ax (plt.Axes): Matplotlib Axes object to plot on.
        speeds_df (pd.DataFrame): DataFrame containing speed data.
    """
    ax.fill_between(speeds_df['t_log'], 0, speeds_df['difference'], 
                    where=(speeds_df['difference'] >= 0),
                    interpolate=True, alpha=0.3, color='green')
    ax.fill_between(speeds_df['t_log'], 0, speeds_df['difference'], 
                    where=(speeds_df['difference'] < 0),
                    interpolate=True, alpha=0.3, color='red')
    speeds_df.plot(x='t_log', y='difference', ax=ax, color='gray', linewidth=1.5, label='Speed Difference (m/s)')
    ax.axhline(0, color='black', linestyle='--', linewidth=1)
    ax.set_ylim(-8, 8)
    ax.set_xlabel('Time (s)', fontsize=10)
    ax.set_ylabel('Difference (m/s)', fontsize=10)
    ax.get_legend().remove()

def style_axes(axes: List[plt.Axes], title: str = None, leftmost: bool = False) -> None:
    """
    Apply consistent styling to the axes.
    
    Args:
        axes (List[plt.Axes]): List of Matplotlib Axes objects to style.
        title (str, optional): Title for the top subplot. Defaults to None.
        leftmost (bool, optional): Whether this is the leftmost column. Defaults to False.
    """
    for ax in axes:
        ax.tick_params(axis='both', which='major', labelsize=10)
        ax.yaxis.label.set_size(10)
        ax.xaxis.label.set_size(10)
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"{int(x)}"))
        ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"{int(x)}"))
        if not leftmost:
            ax.set_yticklabels([])
            ax.set_ylabel('')
    if title:
        axes[0].set_title(title, fontsize=12, fontweight='bold')

def multiplot(dfs: List[pd.DataFrame], condition_names: List[str], xlims: Dict[str, Tuple[int, int]], 
              column_titles: List[str], figsize: Tuple[int, int] = (21, 15), dpi: int = 400) -> plt.Figure:
    """
    Create a multi-panel plot for speed prediction analysis.
    
    Args:
        dfs (List[pd.DataFrame]): List of DataFrames containing data for each condition.
        condition_names (List[str]): Names of the conditions.
        xlims (Dict[str, Tuple[int, int]]): Dictionary of x-axis limits for each condition.
        column_titles (List[str]): Titles for each column of plots.
        figsize (Tuple[int, int], optional): Figure size. Defaults to (21, 15).
        dpi (int, optional): DPI for the figure. Defaults to 400.
    
    Returns:
        plt.Figure: The resulting multi-panel figure.
    """
    n_conditions = len(dfs)
    n_rows = math.ceil(n_conditions / 3)
    n_cols = min(n_conditions, 3)
    
    fig = plt.figure(figsize=figsize, dpi=dpi)
    outer_grid = gridspec.GridSpec(n_rows, n_cols, hspace=0.1, wspace=0.1)
    
    for i, df in enumerate(dfs):
        row, col = divmod(i, 3)
        inner_grid = gridspec.GridSpecFromSubplotSpec(2, 1, subplot_spec=outer_grid[row, col], height_ratios=[2, 1], hspace=0.0)
        
        speeds_df = prepare_data(df)
        
        ax_top = fig.add_subplot(inner_grid[0])
        ax_bottom = fig.add_subplot(inner_grid[1], sharex=ax_top)
        
        plot_speeds(ax_top, speeds_df)
        plot_difference(ax_bottom, speeds_df)
        
        ax_top.set_xlim(xlims[condition_names[i]])
        
        style_axes([ax_top, ax_bottom], title=column_titles[col] if row == 0 else None, leftmost=(col == 0))
        
        ax_top.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
        
        if row == n_rows - 1:
            ax_bottom.set_xlabel('Time (s)', fontsize=10)
        else:
            ax_bottom.set_xlabel('')
    
    plt.tight_layout()
    return fig

def main():
    folder = 'recordings'
    conditions = ['calm', 'aggressive', 'surprise'] 
    # conditions = ['aggressive', 'calm', 'surprise', 'aggressive_2', 'calm_2', 'surprise_2']  # Uncomment for 2 trials

    dfs = [pd.read_csv(f'{folder}/{condition}_openpilot_df.csv.out.csv') for condition in conditions]
    
    frame_len = 15
    xlims = {
        'aggressive': (13, 13 + frame_len),
        'calm': (13, 13 + frame_len),
        'surprise': (22, 22 + frame_len),
        'aggressive_2': (19, 19 + frame_len),
        'calm_2': (10, 10 + frame_len),
        'surprise_2': (22, 22 + frame_len),
    }

    dpi = 600
    fig = multiplot(dfs, conditions, xlims, column_titles=['Calm', 'Aggressive', 'Surprise'], figsize=(10, 5), dpi=dpi)
    plt.tight_layout()
    fig.savefig('output_plot.png', dpi=dpi, bbox_inches='tight')

if __name__ == '__main__':
    main()
