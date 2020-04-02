# Assignment: Hospital
# You're going to build a hospital with patients in it! Create a hospital class.
class Patient(object):
    def __init__(self, id, patient_name, allergies, bed):
        self.id = id
        self.patient_name = patient_name
        self.allergies = allergies
        self.bed = 0
class Hospital(object):
    def __init__(self):
        self.patients = []
        self.capacity = 0
    def admit(self, id, name, allergies, bed):
        patient_list = Patient(id, name, allergies, bed)
        self.patients.append(patient_list)
        self.capacity += 1
        return self
    def discharge(self):
        self.patients.pop(0)
        self.bed = 0
        return self
    def charts(self):
        print "-Patient List-"
        bed_number = 0
        for patient in range(len(self.patients)):
            print "ID #:", self.patients[patient].id
            print "Name:", self.patients[patient].patient_name
            print "Allergies:", self.patients[patient].allergies
            bed_number += 1
            print "Bed:", bed_number
            print "--"*10
        return self
x = Hospital()
x.admit('1', 'Mark', 'Nuts', '').admit('2', 'Jess', 'Bees', '').discharge()
x.charts()
