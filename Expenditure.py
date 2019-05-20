class Expenditure:
    total_money = 0
    peoples = []
    money = []
    total_collected_rupee = 0
    no = 0

    def __init__(self):
        Expenditure.total_money = int(input("Enter Total Expenditure of Hole Purchase : "))
        Expenditure.no = int(input("Enter How Many Peoples are takes Part: "))
        for i in range(0, Expenditure.no):
            name = input("\nEnter Name of People : ")
            Expenditure.peoples.append(name)
            rupee = int(input("Enter How Many Rupuees He Give : "))
            Expenditure.money.append(rupee)
            Expenditure.total_collected_rupee = Expenditure.total_collected_rupee + rupee

    def calculation(self):
        divide_money = int(Expenditure.total_money / Expenditure.no)
        for i in range(0,Expenditure.no):
            if Expenditure.money[i] < divide_money:
                required_give_money = divide_money - Expenditure.money[i]
                print("\n>>>"+Expenditure.peoples[i]+" Gives "+str(Expenditure.money[i])+" RS")
                print("Total Expenditure is : "+str(divide_money)+" RS Then")
                print(Expenditure.peoples[i]+" will Give "+str(required_give_money)+" RS")
            else:
                required_take_money = Expenditure.money[i] - divide_money
                print("\n>>>"+Expenditure.peoples[i] + " Gives " + str(Expenditure.money[i])+" RS")
                print("Total Expenditure is : " + str(divide_money) + " RS Then")
                print(Expenditure.peoples[i] + " will Take " + str(required_take_money)+" RS")


print("\n*****Expenditure Management System***")
day = Expenditure()
print("\n\n\t****Total Money Expenditure****\nRemaining Money after Paying :",(Expenditure.total_collected_rupee-Expenditure.total_money),"RS\n")
day.calculation()


