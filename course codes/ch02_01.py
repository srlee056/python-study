car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color':'White'},
    {'horsepower':400},
    {'price' : 8000}
]

car_company_2 = 'Bmw'
car_detail_2 = [
    {'color':'Black'},
    {'horsepower':270},
    {'price' : 5000}
]

car_company_list = ['Ferrari', 'Bmw']
car_detail_list = [
    {'color':'White', 'horsepower':400, 'price' : 8000},
    {'color':'Black', 'horsepower':270, 'price' : 5000}    
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()
print()

#딕셔너리 구조

car_dicts = [
    {'car_company': 'Ferrari', 'car_detail' : {'color':'White', 'horsepower':400, 'price' : 8000}},
    {'car_company': 'Bmw', 'car_detail' : {'color':'Black', 'horsepower':270, 'price' : 5000}}
]

print(car_dicts)

del car_dicts[1]

print(car_dicts)

print()
print()

#Class

class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    #print 함수가 호출될 때, 원하는 포맷으로 출력됨
    #def __str__(self):
    #    return 'str : {} - {}'.format(self._company, self._details)

    #자료형의 타입에 따른 객체를 그대로 출력할땐 이 함수를 사용
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

car1 = Car('Ferrari', {'color':'White', 'horsepower':400, 'price' : 8000})
car2 = Car('Bmw', {'color':'Black', 'horsepower':270, 'price' : 5000})

print(car1)
print(car2)

print(car1.__dict__)

print(dir(car1))

print()
print()

car_list = []

car_list.append(car1)
car_list.append(car2)

print(car_list)

print()
print()

for car in car_list:
    print(car)