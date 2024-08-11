import csv
from faker import Faker
from datetime import datetime

class GenderClassifier:
    def __init__(self, inputFilename, outputFilename):
        self.filename = inputFilename
        self.output_filename = outputFilename
        self.fake = Faker()
    
    def classify_gender(self):
        count = 0
        fieldnames = ["ID","FirstName","LastName","Gender","Birthdate","Age","Disease","Fever","Cough","Fatigue","Difficulty Breathing","Blood Pressure","Cholesterol Level","Outcome Variable"]          
        
        with open(self.filename, 'r') as csvfile, open(self.output_filename, 'w') as outputfile:
            reader = csv.DictReader(csvfile)
            writer = csv.DictWriter(outputfile,fieldnames=fieldnames)
            writer.writeheader()  

            for row in reader:
                count += 1
                gender = row['Gender'].strip().lower()
                if gender == 'male':
                    firstName = self.fake.first_name_male()
                elif gender == 'female':
                   firstName = self.fake.first_name_female()
                
                age = int(row['Age'])
                birthdate = self.fake.date_of_birth(minimum_age=18, maximum_age=90)
                month = birthdate.month
                day = birthdate.day
                if (month == 2 and day > 28):
                    day += -1
                
                try:
                    birthdate = datetime(year=datetime.now().year - age,
                                        month=birthdate.month,
                                        day=birthdate.day).strftime("%Y-%m-%d")
                except Exception as ex:
                    print(f"{datetime.now().year - age}, {birthdate.month}, {birthdate.day}")
                    print(ex)

                row["ID"] = count
                row['FirstName'] = firstName
                row['LastName'] = self.fake.last_name()
                row['Birthdate'] = birthdate
                writer.writerow(row)

        
        print(f"Number of records Processed: {count}")

# Example usage:
if __name__ == "__main__":
    classifier = GenderClassifier('../Downloads/Disease_Template_Dataset.csv',
                                   '../GraphData/Disease_Profile.csv')
    classifier.classify_gender()