class Patient:
    def __init__(self,name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount
    @property
    def get_name(self):
        return self.name
    @property
    def get_bill_amount(self):
        return self.bill_amount
    def bill_amount(self,bill_amount):
        self.bill_amount = bill_amount
    def name(self,name):
        self.name = name
    def calculate_bill(self):
        return self.bill_amount
class SeniorPatient(Patient):
    def __init__(self,name,bill_amount):
        super().__init__(self,name)
        super().__init__(name,bill_amount)
    def calculate_bill(self):
        return self.bill_amount - (self.bill_amount * 0.15)
class PhilHealthPatient(Patient):
    def __init__(self,name,bill_amount):
        super().__init__(self, name)
        super().__init__(name, bill_amount)
    def calculate_bill(self):
        return self.bill_amount - (self.bill_amount * 0.20)

def print_patient(patient):
    print("Hospital Bill System")
    print("-"*15)
    print(f"Patient Name: {patient.name}")
    print(f"Original Bill: {patient.bill_amount:,.2f}")
    print(f"Final Bill {super(patient).bill_amount}")

#main
regular_patient = Patient("Juan Dela Cruz",15000)
phil_health_patient = Patient("Juan Dela Cruz",15000)
senior_patient = Patient("Juan Dela Cruz",15000)
print_patient(regular_patient)
print_patient(phil_health_patient)
print_patient(senior_patient)

