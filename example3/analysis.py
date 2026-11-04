"""Shared data loading, plotting and group means for example 3."""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

MIN_SIO2 = 0.0  # Change to 58.0 and render again.
ERUPTIONS = ["Monte Nuovo", "Astroni 6", "Fondi di Baia"]
DATA_URL = (
    "https://raw.githubusercontent.com/ELSTE-Master/Data-Science/main/"
    "Data/Smith_glass_post_NYT_data_majors.csv"
)


def load_data():
    data = pd.read_csv(DATA_URL)
    data = data[data["Eruption"].isin(ERUPTIONS)]
    return data[data["SIO2"] >= MIN_SIO2].dropna(subset=["SIO2", "K2O"])


def scatter_plot(data):
    plt.figure(figsize=(6.6, 2.7))
    sns.scatterplot(data=data, x="SIO2", y="K2O", hue="Eruption")
    plt.xlabel("SiO₂ (wt. %)")
    plt.ylabel("K₂O (wt. %)")
    plt.tight_layout()
    plt.show()


def summary_table(data):
    return data.groupby("Eruption")[["SIO2", "K2O"]].mean().round(2)
