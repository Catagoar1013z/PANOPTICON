import pandas as pd

from data.generator import generate_dataset


def create_dataset(size=100, filename="security_events.csv"):
    """
    Genera eventos sintéticos y los guarda en un archivo CSV.
    """

    data = generate_dataset(size)

    dataframe = pd.DataFrame(data)

    dataframe.to_csv(filename, index=False)

    return dataframe