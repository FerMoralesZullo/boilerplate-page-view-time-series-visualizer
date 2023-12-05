import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Clean data
df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(df.index, df["value"], color='r', linewidth=1)
    ax.set(title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019", xlabel="Date", ylabel="Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["Year"] = df_bar.index.year
    df_bar["Month"] = df_bar.index.strftime("%B")

    # Draw bar plot
    df_bar_grouped = df_bar.groupby(["Year", "Month"])["value"].mean().unstack()

    fig, ax = plt.subplots(figsize=(14, 6))
    df_bar_grouped.plot(kind='bar', ax=ax)
    ax.set(title="Average Page Views per Month (2016-2019)", xlabel="Years", ylabel="Average Page Views")
    ax.legend(title="Months", title_fontsize="15", fontsize="10")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))
    sns.boxplot(x=df_box["Year"], y=df_box["value"], ax=axes[0])
    sns.boxplot(x=df_box["Month"], y=df_box["value"], order=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], ax=axes[1])

    axes[0].set(title="Year-wise Box Plot (Trend)", xlabel="Year", ylabel="Page Views")
    axes[1].set(title="Month-wise Box Plot (Seasonality)", xlabel="Month", ylabel="Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

if __name__ == '__main__':
    # Ejecutar las funciones
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()
