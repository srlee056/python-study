class Car():
    """
    car class
    Author : Lee
    Date : 2021/08/02
    """

    # 클래스 변수

    car_count = 0


    def __init__(self, company, details):
        self._company = company
        #self.car_count = 10
        self._details = details
        Car.car_count += 1

    #print 함수가 호출될 때, 원하는 포맷으로 출력됨
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    #자료형의 타입에 따른 객체를 그대로 출력할땐 이 함수를 사용
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    def __del__(self):
        print('del?')
        Car.car_count -=1

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))
    
# self?

car1 = Car('Ferrari', {'color':'White', 'horsepower':400, 'price' : 8000})
car2 = Car('Bmw', {'color':'Black', 'horsepower':270, 'price' : 5000})
car3 = Car('Audi', {'color':'Silver', 'horsepower':300, 'price' : 6000})

# ID
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2) #cause ID value is different

# dir & __dict__
print(dir(car1))
print(dir(car2))

print()
print()

print(Car.car_count)
print(car1.car_count)
print(car2.car_count)
print(car1.__dict__)
print(car2.__dict__)



# Doctring
print(Car.__doc__) 
print()

car1.detail_info()
car2.detail_info()

print("hi")
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__))
print()
# error
# Car.detail_info()
# we need SELF

Car.detail_info(car1)
Car.detail_info(car2)

# 접근

del car2
print(car1.car_count)
print(Car.car_count)