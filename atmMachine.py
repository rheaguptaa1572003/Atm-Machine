class ATM:
    def __init__(self):
        self.account = {'1234':{'saving':6000000, 'checking':980000}}
        self.__pin = None
        self.enter_pin()
    
    def get_pin(self):
        return self.__pin
    
    def set_pin(self, pin):
        self.__pin = pin
    
    def enter_pin(self):
        while True:
            a, b = input("Enter pin: "), input("Verify pin: ")
            if (len(a) + len(b) == 8) and (a == b) and (a in self.account):
                self.set_pin(a)
                self.choise()
            print("Enter pin again!")
    
    def choise(self):
        while True:
            ch = input("Enter choice: ")
            if ch == '1':
                self.ch1()
            elif ch == '2':
                self.ch2()
            elif ch == '3':
                self.ch3()
            elif ch == '4':
                self.ch4()
            else:
                print("Invalid choice!")
                self.enter_pin()
    
    def ch1(self):
        print(self.account[self.get_pin()]['saving'])
    
    def ch2(self):
        deposit = int(input("Enter deposit money: "))
        self.account[self.get_pin()]['saving'] += deposit
        print(self.account[self.get_pin()]['saving'])
    
    def ch3(self):
        withdraw = int(input("Enter withdraw money: "))
        if self.account[self.get_pin()]['saving'] >= withdraw:
            self.account[self.get_pin()]['saving'] -= withdraw
            print(self.account[self.get_pin()]['saving'])
        else:
            print("Not enough balance!")
    
    def ch4(self):
        transfer = int(input("Enter transfer amount: "))
        if self.account[self.get_pin()]['checking'] >= transfer:
            self.account[self.get_pin()]['checking'] -= transfer
            self.account[self.get_pin()]['saving'] += transfer
            print("Saving balance:", self.account[self.get_pin()]['saving'])
            print("Checking balance:", self.account[self.get_pin()]['checking'])
        else:
            print("Not enough balance!")

if __name__ == '__main__':
    atm = ATM()