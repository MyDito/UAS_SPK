from settings import (
    DEV_SCALE_brand,
    DEV_SCALE_ram,
    DEV_SCALE_storage,
    DEV_SCALE_processor,
    DEV_SCALE_battery,
    DEV_SCALE_harga,
)

from collections import OrderedDict  # ascending berdasarkan id
from sqlalchemy.orm import Session
from engine import engine

session = Session(engine)


class BaseMethod:
    def __init__(self, data_dict, **setWeight):
        self.dataDict = data_dict

        # 1-5
        self.raw_weight = {
            "brand": 3,
            "ram_gb": 4,
            "processor": 5,
            "storage_gb": 4,
            "battery": 1,
            "harga": 2,
        }
        if setWeight:
            for item in setWeight.items():
                temp1 = setWeight[item[0]]  # value int
                temp2 = {v: k for k, v in setWeight.items()}[item[1]]  # key str

                setWeight[item[0]] = item[1]
                setWeight[temp2] = temp1

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {k: round(v / total_weight, 2) for k, v in self.raw_weight.items()}

    @property
    def data(self):
        return [
            {
                "id": smartphone["id"],
                "brand": DEV_SCALE_brand[
                    "".join(
                        [
                            x
                            for x in DEV_SCALE_brand.keys()
                            if x.lower() in smartphone["brand"].lower()
                        ]
                    )
                ],
                "ram_gb": smartphone["ram_gb"],
                "storage_gb": smartphone["storage_gb"],
                "processor": DEV_SCALE_processor[smartphone["processor"]],
                "battery": smartphone["battery"],
                "harga": smartphone["harga"],
            }
            for smartphone in self.dataDict
        ]

    @property
    def normalized_data(self):
        # x/max [benefit]
        # min/x [cost]
        brands = []  # max
        rams = []  # max
        storages = []  # max
        prosesors = []  # max
        baterais = []  # max
        hargas = []  # min
        for data in self.data:
            brands.append(data["brand"])
            rams.append(data["ram_gb"])
            storages.append(data["storage_gb"])
            prosesors.append(data["processor"])
            baterais.append(data["battery"])
            hargas.append(data["harga"])
        max_brand = max(brands)
        max_ram = max(rams)
        max_storage = max(storages)
        max_prosesor = max(prosesors)
        max_baterai = max(baterais)
        min_harga = min(hargas)
        return [
            {
                "id": data["id"],
                "brand": data["brand"] / max_brand,  # benefit
                "ram_gb": data["ram_gb"] / max_ram,  # benefit
                "storage_gb": data["storage_gb"] / max_storage,  # benefit
                "processor": data["processor"] / max_prosesor,  # benefit
                "battery": data["battery"] / max_baterai,  # benefit
                "harga": min_harga / data["harga"],  # cost
            }
            for data in self.data
        ]


class WeightedProduct(BaseMethod):
    def __init__(self, dataDict, setWeight: dict):
        super().__init__(data_dict=dataDict, **setWeight)

    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight[WP]
        result = {
            row["id"]: round(
                row["brand"] ** weight["brand"]
                * row["ram_gb"] ** weight["ram_gb"]
                * row["processor"] ** weight["processor"]
                * row["storage_gb"] ** weight["storage_gb"]
                * row["battery"] ** weight["battery"]
                * row["harga"] ** weight["harga"],
                2,
            )
            for row in self.normalized_data
        }
        # sorting
        # return result
        return dict(sorted(result.items(), key=lambda x: x[1], reverse=True))


# class SimpleAdditiveWeighting(BaseMethod):
#     @property
#     def calculate(self):
#         weight = self.weight
#         # calculate data and weight
#         result = {
#             row["id"]: round(
#                 row["brand"] * weight["brand"]
#                 + row["ram_gb"] * weight["ram_gb"]
#                 + row["storage_gb"] * weight["storage_gb"]
#                 + row["processor"] * weight["processor"]
#                 + row["battery"] * weight["battery"]
#                 + row["harga"] * weight["harga"],
#                 2,
#             )
#             for row in self.normalized_data
#         }
#         # sorting
#         return OrderedDict(sorted(result.items(), key=lambda x: x[0]))
