from abc import ABC, abstractmethod

electricity_usage = [
    {"date": "2024-11-01", "usage": 12.5},
    {"date": "2024-11-02", "usage": 15.3},
    {"date": "2024-11-03", "usage": 10.8},
    {"date": "2024-11-04", "usage": 14.2},
    {"date": "2024-11-05", "usage": 13.6},
]

class ElectricityData(ABC):
    __total_usage = 0
    
    def __init__(self, usage_data):
        self.__usage_data = usage_data

    @abstractmethod
    def calculate_total_usage(self):
        pass

    @abstractmethod
    def get_usage_on_date(self, date):
        pass
    
    @property
    def usage_data(self):
        return self.__usage_data
    
    @usage_data.setter
    def set_usage_data(self, value):
        self.__usage_data = value
        
    @property
    def total_usage(self):
        return self.__total_usage

class HomeElectricityData(ElectricityData):
    ElectricityData.__total_usage = 0
    
    def __init__(self, usage_data):
        super().__init__(usage_data)
    
    def calculate_total_usage(self):
        return sum(data["usage"] for data in self.__usage_data)

    def get_usage_on_date(self, date):
        for entry in self.__usage_data:
            if entry["date"] == date:
                return entry["usage"]
        return None
    

class ElectricityUtility:
    @staticmethod
    def find_max(usage_data):
        return max(usage_data, key=lambda x: x["usage"])


home_data = HomeElectricityData(electricity_usage)

print(home_data.usage_data)
print(home_data.total_usage)
# print(home_data.__usage_data)

print(f"총 전력 사용량: ")  
print(f"의 사용량: ")
print(f"추가후 총전력 사용량: ")  
print(f"특정 범위 날짜내 사용량: ")
print(f"가장 높은 사용량: ")  