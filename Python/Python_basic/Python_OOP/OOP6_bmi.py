class Bmi:
    def __init__(self,w_kg, h_cm):
        self.w_kg = w_kg
        self.h_cm = h_cm
    
    def bmi(self):
        return self.w_kg / (self.h_cm / 100) ** 2
    
    def category(self):
        diag = ""
        if self.bmi() < 18.5:
            diag = "ต่ำกว่าเกณฑ์"
        elif 18.5 <= self.bmi() <= 25:
            diag = "ตามเกณฑ์"
        elif 25 < self.bmi() <= 30:
            diag = "เกินเกณฑ์"
        elif self.bmi() > 30:
            diag = "อ้วน"
        return diag
    
    def __str__(self):
        return f"BMI = {self.bmi()} ({self.category()})"

if __name__ == "__main__":
    a = Bmi(50,164)
    print(a) 