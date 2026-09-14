class Employee:
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle, PayYear2022):
        self.__HourlyPay = HourlyPay
        self.__EmployeeNumber = EmployeeNumber
        self.__JobTitle = JobTitle
        self.__PayYear2022 = []
        for x in range(0, 52):
            self.__PayYear2022.append(0.00)

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    def SetPay(self, WeekNumber, Hours):
        self.__PayYear2022[WeekNumber-1] = Hours * self.__HourlyPay

    def GetTotalPay(self):
        TotalPay = 0
        for X in range (0, 52):
            TotalPay += self.__PayYear2022[X]
        return TotalPay