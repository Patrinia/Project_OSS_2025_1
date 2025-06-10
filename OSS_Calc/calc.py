import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""
        self.is_roman = False  # 현재 로마자 표시 여부

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['='],
            ['Roman', 'Arabic']  # 로마자, 아라비아 숫자 변환 버튼 추가
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

    def to_roman(self, num):
        if not 0 < num < 4000:
            return "로마숫자는 1~3999까지만 존재한다."
            
        roman_values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        
        result = ""
        for value, numeral in roman_values:
            while num >= value:
                result += numeral
                num -= value
        return result

    def from_roman(self, roman_str):
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        for char in reversed(roman_str):
            current_value = roman_values[char]
            if current_value >= prev_value:
                total += current_value
            else:
                total -= current_value
            prev_value = current_value
            
        return str(total)

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
            self.is_roman = False
        elif char == '=':
            if not self.expression:  # 입력이 없는 경우
                return
            try:
                # 현재 식에 로마자가 포함되어 있는지 확인
                if self.is_roman:
                    # 식에서 로마자를 아라비아 숫자로 변환
                    expr = self.expression
                    # 연산자를 기준으로 분리
                    operators = ['+', '-', '*', '/']
                    current_num = ''
                    converted_expr = ''
                    
                    for c in expr:
                        if c in operators:
                            if current_num:
                                converted_expr += str(self.from_roman(current_num))
                                current_num = ''
                            converted_expr += c
                        else:
                            current_num += c
                    
                    if current_num:  # 마지막 숫자 처리
                        converted_expr += str(self.from_roman(current_num))
                    
                    # 계산 수행
                    result = eval(converted_expr)
                    
                    # 결과가 정수인지 확인
                    if result == int(result):
                        self.expression = self.to_roman(int(result))
                    else:
                        self.expression = "로마자에 소수는 존재하지 않는다."
                else:
                    self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        elif char == 'Roman':
            try:
                if self.is_roman or not self.expression:  # 이미 로마자이거나 입력이 없는 경우
                    self.is_roman = True  # 입력이 없어도 로마자 모드로 전환
                    return
                if '.' in self.expression:  # 소수점이 있는 경우
                    self.expression = "로마자에 소수는 존재하지 않는다."
                else:
                    num = int(float(self.expression))
                    self.expression = self.to_roman(num)
                self.is_roman = True
            except Exception:
                if self.expression:  # 입력이 있는 경우에만 에러 메시지 표시
                    self.expression = "에러"
        elif char == 'Arabic':
            try:
                if not self.is_roman or not self.expression:  # 이미 아라비아 숫자이거나 입력이 없는 경우
                    return
                self.expression = self.from_roman(self.expression)
                self.is_roman = False
            except Exception:
                if self.expression:  # 입력이 있는 경우에만 에러 메시지 표시
                    self.expression = "에러"
        elif char in ['+', '-', '*', '/']:
            # 연산자는 공백 없이 추가
            self.expression += char
        else:
            if self.is_roman:
                if char.upper() in ['I', 'V', 'X', 'L', 'C', 'D', 'M']:
                    # 로마자 직접 입력
                    self.expression += char.upper()
                elif char.isdigit():  # 소수점 입력은 제외
                    try:
                        # 현재 입력된 숫자를 바로 로마자로 변환
                        num = int(char)
                        if 0 < num < 4000:
                            self.expression += self.to_roman(num)
                    except:
                        pass
            else:
                if char == '.' or (self.expression and (self.expression[-1].isdigit() or self.expression[-1] == '.')):
                    # 소수점이거나 직전 문자가 숫자 또는 소수점인 경우 공백 없이 추가
                    self.expression += char
                else:
                    self.expression += char

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def from_roman_dict(self):
        return {
            'M': '1000',
            'CM': '900',
            'D': '500',
            'CD': '400',
            'C': '100',
            'XC': '90',
            'L': '50',
            'XL': '40',
            'X': '10',
            'IX': '9',
            'V': '5',
            'IV': '4',
            'I': '1'
        }



