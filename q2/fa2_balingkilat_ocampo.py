class Patient:
    name = []
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = float(bill_amount)
    def get_name(self):
        return self.__name
    def set_name(self):
        if name == "":
            self.__name = name
        else:
            print("Invalid format")
    def get_bill_amount(self):
        return self.__bill_amount
    def set_bill_amount(bill_amount):
        if bill_amount > 0:
            self.bill_amount = bill_amount
    def calculate_bill():
        pass
class SeniorPatient(Patient):
    def calculate_bill(self):
        to_discount = self.get_bill_amount() * 0.20
        new_bill = self.get_bill_amount() - to_discount
        return new_bill
class PhilHealthPatient(Patient):
     def calculate_bill(self):
        to_discount = self.get_bill_amount() * 0.15
        new_bill = self.get_bill_amount() - to_discount
        return new_bill

regular_patient = Patient("Fred Durst", 10000)
senior_patient = SeniorPatient("Wes Borland", 15000)
philhealth_patient = PhilHealthPatient("John Otto", 15000)
print(f"Hospital Billing System\n-------------------------")
print("Patient Name: ",regular_patient.get_name())
print(f"Original Bill:₱{regular_patient.get_bill_amount():.2f}")
print(f"Final Bills:₱{regular_patient.get_bill_amount():.2f}\n")
print("Patient Name: ", senior_patient.get_name())
print(f"Original Bill:₱{senior_patient.get_bill_amount():.2f}")
print(f"Final Bill: ₱{senior_patient.calculate_bill():.2f}\n")
print("Patient Name: ", philhealth_patient.get_name())
print(f"Original Bill:₱{philhealth_patient.get_bill_amount():.2f}")
print(f"Final Bill: ₱{philhealth_patient.calculate_bill():.2f}\n")
