from abc import ABC, abstractmethod

electricity_usage = {
    {"date": "2024-11-01", "usage": 12.5},
    {"date": "2024-11-02", "usage": 15.3},
    {"date": "2024-11-03", "usage": 10.8},
    {"date": "2024-11-04", "usage": 14.2},
    {"date": "2024-11-05", "usage": 13.6},
}

class ElectricityData:
    @abstractmethod
    def calculate_total_usage():
        pass

    @abstractmethod
    def get_usage_on_date():
        pass

class HomeElectricityData(ElectricityData):
    electricity_usage = []  

class ElectrricityUtility:
    @staticmethod
    def find_max():
        pass