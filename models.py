# from sqlalchemy import Column, Integer, String, create_engine
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import numpy as np
import pandas as pd
from spk_model import WeightedProduct


class Smartphone:
    def __init__(self) -> None:
        self.smartphone = pd.read_csv("main_data/hitung_smartphone.csv")
        self.smartphones = np.array(self.smartphone)

    @property
    def smartphone_data(self):
        data = []
        for smartphone in self.smartphones:
            data.append({"id": smartphone[0], "nama": smartphone[1]})
        return data

    @property
    def smartphone_data_dict(self):
        data = {}
        for smartphone in self.smartphones:
            data[smartphone[0]] = smartphone[1]
        return data

    def get_recs(self, kriteria: dict):
        wp = WeightedProduct(self.smartphone.to_dict(orient="records"), kriteria)
        return wp.calculate
