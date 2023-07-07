class HealthCheck:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def check_health(self):
        bmi = self.calculate_bmi()
        result = self.get_result(bmi)

        print("=== 건강검진 결과 ===")
        print(f"이름: {self.name}")
        print(f"나이: {self.age}")
        print(f"신장: {self.height}cm")
        print(f"체중: {self.weight}kg")
        print(f"BMI: {bmi:.2f}")
        print(f"결과: {result}")

    def calculate_bmi(self):
        height_in_meters = self.height / 100
        bmi = self.weight / (height_in_meters ** 2)
        return self.get_result(bmi)

    def get_result(self, bmi):
        if bmi < 18.5:
            return "저체중"
        elif 18.5 <= bmi < 23:
            return "정상체중"
        elif 23 <= bmi < 25:
            return "과체중"
        elif 25 <= bmi < 30:
            return "경도비만"
        else:
            return "고도비만"
        
    def backup_records(self):
        with open(f"backup_{self.name}.txt", "w") as f:
            f.write(f"{self.name}, {self.age}, {self.height}, {self.weight}, {self.bmi}")

my_patient = HealthCheck(name="김도언", age=20, height=180, weight=65)
my_patient2 = HealthCheck(name="이예원", age=21, height=160, weight=50)

my_patient.check_health() # bmi
my_patient.backup_records() # 파일로 저장.
my_patient2.check_health()
my_patient2.backup_records()
# backup_{name}

patients_list = [my_patient,my_patient2]
age_sum=0
for p in patients_list:
    age_sum+=p.age
print(age_sum/len(patients_list))