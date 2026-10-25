class OrderService:
    def order_burger(self):
        pass

    def order_fries(self):
        pass

    def order_combo(self):
        pass
class BurgerOrderService(OrderService):
    def order_burger(self):
        print("Ordering burger")

    def order_fries(self):
        raise Exception("Fries not supported")

    def order_combo(self):
        raise Exception("Combo not supported")
#Burger counter only sells burgers
#Forced to implement fries & combo

#this is liskov substitution principle violated.
#solution is interface segration(same as liskov substitution.)