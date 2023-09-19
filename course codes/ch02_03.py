#class method
#instance method
#static method

class Car():
    """
    car class
    Author : Lee
    Date : 2021/08/06
    Description : Calss, Static, Instance Method
    """

    # 클래스 변수 (모든 인스턴스가 공유)
    price_per_raise = 1.0
    
    def __init__(self, company, details):
        self._company = company
        self._details = details

    #print 함수가 호출될 때, 원하는 포맷으로 출력됨
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    #자료형의 타입에 따른 객체를 그대로 출력할땐 이 함수를 사용
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    # Instance Method
    # self : 객체의 고유한 속성값을 사용 
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))
    
    # Instance Method
    def get_price(self):
        return 'Before Car Price -> company: {}, price:{}'.format(self._company, self._details.get('price')) 

    # Instance Method
    def get_price_culc(self):
        return 'After Car Price -> company: {}, price:{}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <=1 :
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        print('Succeed! Price increased')
    
    # Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'OK! This car is Bmw'
        else :
            return 'Sorry. This car is {}, not Bmw'.format(inst._company)

# self?
car1 = Car('Ferrari', {'color':'White', 'horsepower':400, 'price' : 8000})
car2 = Car('Bmw', {'color':'Black', 'horsepower':270, 'price' : 5000})

#가격 정보 직접 접근
print(car1._details.get('price'))
print(car1._details['price'])

#가격정보(인스턴스 메소드)
print(car1.get_price())
print(car2.get_price())

#Car.price_per_raise = 1.4
Car.raise_price(1)
Car.raise_price(1.4)

print(car1.get_price_culc())
print(car2.get_price_culc())

#static method. 유연한 특징을 가짐. 
#클래스와 관련이 있고, 공통적인 활용은 가능하지만 전체를 아우르는 특징은 아닐때, 사용하기 좋음
print(Car.is_bmw(car1))
print(car1.is_bmw(car1))
print(Car.is_bmw(car2))