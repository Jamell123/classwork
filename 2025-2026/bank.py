#jamell coleman
#04-07-26
from tkinter import Variable


class Bank_Account:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance


class Smart_Phone:
    def __init__(self,owner,phone_bill,monthly_installments,sales_tax,one_time_activation,):
        self.owner=owner
        self.phone_bill=phone_bill
        self.monthly_installments=monthly_installments
        self.sales_tax=sales_tax
        self.one_time_activation=one_time_activation


def main():
    account1=Bank_Account("jamell",19)
    account2=Bank_Account("jayson",20)
    account3=Bank_Account("chris",21)
    print(account1.owner, account1.balance, account2.owner, account2.balance, account3.owner, account3.balance)

    Variable=Smart_Phone("jamell",500,3,10,5)
    Variable2=Smart_Phone("benji",300,4,20,6)
    Variable3=Smart_Phone("chris",800,5,30,8)
    print(Variable.owner, Variable.phone_bill, Variable.monthly_installments, Variable.sales_tax, Variable.one_time_activation,Variable2.owner, Variable2.phone_bill, Variable2.monthly_installments, Variable2.sales_tax, Variable2.one_time_activation
         ,Variable3.owner, Variable3.phone_bill, Variable3.monthly_installments, Variable3.sales_tax, Variable3.one_time_activation )





if __name__ == '__main__':
    main()
