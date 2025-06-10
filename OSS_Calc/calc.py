import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""
        self.current_base = 10  # 현재 화면에 출력되고 있는 숫자의 진수를 저장하는 변수

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=',],
            ['Bin', 'Oct', 'Hex', 'Dec']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
            self.current_base  = 10
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
                self.current_base = 10
            except Exception:
                self.expression = "에러"
        elif char in ['Bin', 'Oct', 'Hex', 'Dec']:
            try:
                # 현재 숫자를 10진수로 변환
                if self.current_base == 2:  # 현재 2진수
                    current_num = int(self.expression[2:], 2)
                elif self.current_base == 8:  # 현재 8진수
                    current_num = int(self.expression[2:], 8)
                elif self.current_base == 16:  # 현재 16진수
                    current_num = int(self.expression[2:], 16)
                else:  # 현재 10진수
                    current_num = int(float(self.expression))
                
                # 진수 변환 (접두어도 함꼐 출력하여 사용자가 현재 진수를 파악하기 용이하기 한다.)
                if char == 'Bin':
                    self.expression = bin(current_num)  # '0b' 2진수
                    self.current_base = 2
                elif char == 'Oct':
                    self.expression = oct(current_num)  # '0o' 8진수
                    self.current_base = 8
                elif char == 'Hex':
                    self.expression = hex(current_num).upper()  # '0x' 16진수
                    self.current_base = 16
                elif char == 'Dec': # 10진수는 접두어 없이 출력
                    self.expression = str(current_num)
                    self.current_base = 10
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)
            if self.current_base != 10:  # 숫자나 연산자 입력 시 10진수로 변환하여 계산시킨다
                self.current_base = 10

        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)



