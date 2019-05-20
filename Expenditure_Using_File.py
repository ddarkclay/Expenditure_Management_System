class Expenditure:
    total_money = 0
    peoples = []
    money = []
    total_collected_rupee = 0
    no = 0

    def __init__(self):
        Expenditure.total_money = int(input("Enter Total Expenditure of Hole Purchase : "))
        f.write("Time is  : "+str(Expenditure.getdate(self)))
        f.write("\nTotal Money Paid : "+str(Expenditure.total_money)+" RS\n")
        Expenditure.no = int(input("Enter How Many Peoples are takes Part: "))
        for i in range(0, Expenditure.no):
            name = input("\nEnter Name of People : ")
            Expenditure.peoples.append(name)
            rupee = int(input("Enter How Many Rupuees He Give : "))
            Expenditure.money.append(rupee)
            f.write("\t"+name+" \t"+str(rupee)+"\n")
            Expenditure.total_collected_rupee = Expenditure.total_collected_rupee + rupee

    def calculation(self):
        divide_money = int(Expenditure.total_money / Expenditure.no)
        for i in range(0,Expenditure.no):
            if Expenditure.money[i] < divide_money:
                required_give_money = divide_money - Expenditure.money[i]
                print(">>>"+Expenditure.peoples[i]+" Gives "+str(Expenditure.money[i])+" RS")
                print("Total Expenditure is : "+str(divide_money)+" RS Then")
                print(""+Expenditure.peoples[i]+" will Give "+str(required_give_money)+" RS\n")
                f.write("\n>>>" + Expenditure.peoples[i] + " Gives " + str(Expenditure.money[i]) + " RS")
                f.write("\nTotal Expenditure is : " + str(divide_money) + " RS Then")
                f.write("\n" + Expenditure.peoples[i] + " will Give " + str(required_give_money) + " RS\n")
            else:
                required_take_money = Expenditure.money[i] - divide_money
                print(">>>"+Expenditure.peoples[i] + " Gives " + str(Expenditure.money[i])+" RS")
                print("Total Expenditure is : " + str(divide_money) + " RS Then")
                print(""+Expenditure.peoples[i] + " will Take " + str(required_take_money)+" RS\n")
                f.write("\n>>>" + Expenditure.peoples[i] + " Gives " + str(Expenditure.money[i]) + " RS")
                f.write("\nTotal Expenditure is : " + str(divide_money) + " RS Then")
                f.write("\n" + Expenditure.peoples[i] + " will Take " + str(required_take_money) + " RS\n")
        f.write("\n\n")

    def getdate(self):
        import datetime
        return datetime.datetime.now()


f = open("Expenditure_log.txt","a")
print("\n*****Expenditure Management System***")
day = Expenditure()
print("\n\n\t****Total Money Expenditure****\nRemaining Money after Paying :",str(Expenditure.total_collected_rupee-Expenditure.total_money),"RS\n")
f.write("Remaining Money after Paying :"+str(Expenditure.total_collected_rupee-Expenditure.total_money)+" RS\n")
day.calculation()
f.close()