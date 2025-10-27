import random


class Subject:
    
    def __init__(self):

        self.id = self.generate_id()
        self.mark = random.randint(25, 100)
        self.grade = self.calculate_grade()
    
    def generate_id(self, existing_subjects=None):

        if existing_subjects:
            existing_ids = {subject.id for subject in existing_subjects}
            while True:
                new_id = f"{random.randint(1, 999):03d}"
                if new_id not in existing_ids:
                    return new_id
        else:
            return f"{random.randint(1, 999):03d}"
    
    def calculate_grade(self):

        if self.mark >= 85:
            return "HD"
        elif self.mark >= 75:
            return "D"
        elif self.mark >= 65:
            return "C"
        elif self.mark >= 50:
            return "P"
        else:
            return "Z"
    
    def __str__(self):
        """String representation of subject"""
        return f"Subject ID: {self.id}, Mark: {self.mark}, Grade: {self.grade}"
