from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 수입 추가")
        print("2. 수입 목록 보기")
        print("3. 지출 추가")
        print("4. 지출 목록 보기")
        print("5. 현재 잔고 보기")
        print("6. 종료")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 급여, 용돈 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
                if amount < 0:
                    print("음수는 입력할 수 없습니다.\n")
                    continue
            except ValueError:
                print("숫자만 입력할 수 있습니다.\n")
                continue
            budget.add_income(category, description, amount)

        elif choice == "2":
            budget.list_incomes()

        elif choice == "3":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
                if amount < 0:
                    print("음수는 입력할 수 없습니다.\n")
                    continue
            except ValueError:
                print("숫자만 입력할 수 있습니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "4":
            budget.list_expenses()

        elif choice == "5":
            budget.total_spent()

        elif choice == "6":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
