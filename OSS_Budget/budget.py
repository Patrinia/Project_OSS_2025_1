import datetime
from expense import Expense
from income import Income

class Budget:
    def __init__(self):
        self.expenses = []
        self.incomes = []
        
        # 기본 수입 항목 추가
        today = datetime.date.today().isoformat()
        default_income = Income(today, "월급", "고정 목록입니다.", 0)
        self.incomes.append(default_income)
        
        # 기본 지출 항목 추가
        default_expenses = [
            Expense(today, "식비", "고정 목록입니다.", 0),
            Expense(today, "교통비", "고정 목록입니다.", 0)
        ]
        self.expenses.extend(default_expenses)

    def add_income(self, category, description, amount):
        today = datetime.date.today().isoformat()
        income = Income(today, category, description, amount)
        self.incomes.append(income)
        print("수입이 추가되었습니다.\n")

    def list_incomes(self):
        if not self.incomes:
            print("수입 내역이 없습니다.\n")
            return
        print("\n[수입 목록]")
        for idx, i in enumerate(self.incomes, 1):
            print(f"{idx}. {i}")
        print()

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total_income = sum(i.amount for i in self.incomes)
        total_expense = sum(e.amount for e in self.expenses)
        balance = total_income - total_expense
        
        print(f"총 수입: {total_income}원")
        print(f"총 지출: {total_expense}원")
        print(f"수지 차액: {balance}원")
        print()
        
        if balance > 0:
            print("흑자입니다.")
        elif balance == 0:
            print("본전입니다.")
        else:
            print("적자입니다.")


