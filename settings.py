# settings.py
USER = "root"
PASSWORD = ""
HOST = "localhost"
PORT = "3306"
DATABASE_NAME = "smartphone"


DEV_SCALE_brand = {
    "Samsung Galaxy A01": 5,
    "Samsung Galaxy M01": 5,
    "Oppo A15": 4,
    "Oppo A53": 4,
    "Vivo Y12s": 4,
    "Vivo Y20": 4,
    "Realme C11": 3,
    "Realme C21": 3,
    "Xiaomi Redmi 9": 2,
    "Xiaomi Redmi 9A": 2,
}


DEV_SCALE_ram = {
    "2": 3,
    "3": 4,
    "4": 5,
}
DEV_SCALE_storage = {
    "16": 2,
    "32": 3,
    "64": 4,
    "128": 5,
}
DEV_SCALE_processor = {
    "Qualcomm Snapdragon 439": 5,
    "Qualcomm Snapdragon 460": 4,
    "Mediatek Helio G35": 3,
    "Mediatek Helio G80": 4,
    "Mediatek Helio P35": 3,
}
DEV_SCALE_battery = {"3000": 1, "4000": 2, "4230": 2, "5000": 3, "5020": 3}
DEV_SCALE_ram = {"2": 3, "3": 4, "4": 5}
DEV_SCALE_harga = {
    "1499000": 2,
    "1699000": 3,
    "1799000": 3,
    "1899000": 3,
    "1999000": 4,
    "2099000": 4,
    "2299000": 5,
}
