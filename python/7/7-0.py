dict1 = dict()

dict1 = {
    "name": "홍길동",
    "age": 20
}

dict1["birthday"] = "0000"
print(dict1)

fruits = {"apple": "사과", "banana": "바나나"}

print(fruits.get("peach", "복숭아"))
# -> 존재하는 키로 검색시 기본값을 설정

fruits.update({"grapes": "포도"})
print(fruits)

print(fruits.keys())
print(fruits.values())
print(fruits.items())