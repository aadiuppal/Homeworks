class Person:
    def __init__(self, name, gender= None):
        self.gender = gender
        self.name = name
        self.education = None
    def set_education(self,education):
        self.education = education
