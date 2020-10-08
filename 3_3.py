"""
Создайте корзину покупок для интернет-магазина.
Каждая корзина создается для определенного человека (можно создать отдельный класс, 
можно просто указать имя человека).
В корзину можно добавлять товары. Каждый товар имеет уникальное название и цену. 
Если такой товар в корзине уже есть, то при добавлении просто пересчитывается стоимость 
этой позиции. 
Из корзины можно удалять товары. Но нужно проверять, что такой товар есть в корзине.
Также нужно следить за суммой чека для этой корзины. 
Пригодится и функция вывода содержимого корзины на экран. 
"""
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def show(self):
        print (self.name, self.price)

def equal(i, item):
    return i.name == item.name and i.price == item.price

class Bucket:
    def __init__(self, name):
        self.items = []
        self.summ = 0
        self.name = name

    def add(self, item):
        self.items.append(item)
        self.summ += item.price
        
    def delete(self, item):
        for i in self.items:
            if equal(i, item):
                self.items.remove(i)
                self.summ -= i.price
                return
    
    def show(self):
        for i in self.items:
            i.show()
        print(self.name, ", your summ =", self.summ)
        
one = Item("one", 10)
two = Item("two", 20)

b = Bucket("Ben")
b.show()

b.add(one)
b.add(two)
b.show()

b.delete(one)
b.show()