import random
import pandas as pd

from icecream import ic
from faker import Faker
from datetime import datetime

class PersonProfile:
    def __init__(self, outputFilename):
        self.output_filename: str | None = outputFilename
        self.num_entries: int = 365
        self.fake:Faker = Faker()

    def is_leap_year(sekf,year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False


    def generate_fake_profile(self):
        data = []
        count=0

        for _ in range(self.num_entries):
            if (self.fake.passport_gender() == "M"):
                gender_ = "Male"
                first_name = self.fake.first_name_male()
            else:
                gender_ = "Female"
                first_name = self.fake.first_name_female()
            
            birthdate = self.fake.date_of_birth(minimum_age=18, maximum_age=90)
            year=datetime.now().year
            age = year - birthdate.year
            month = birthdate.month
            day = birthdate.day
            if (month == 2 and day > 28):
                if (self.is_leap_year(year)):
                    if day == 30:
                       day += -1
                    elif day > 30:
                       day += -2
                else:
                    day += -1

            try:
                birthdate = datetime.strftime("%Y-%m-%d")
            except Exception as ex:
                print(f"{datetime.now().year - age}, {birthdate.month}, {birthdate.day}")
                print(ex)
            count += 1
            entry = {
                "id": count,
                "FirstName": first_name,
                "LastName": self.fake.last_name(),
                "Gender": gender_,
                "Date of Birth": birthdate,
                "Age":age,
                "Height": random.randint(48, 72),
                "Weight": random.randint(90,350)
                #"SSN": self.fake.ssn(),
                #"Address": fake.address(),
                #"Email": fake.email(),
                #"Phone Number": fake.phone_number(),
                #"Random Number": random.randint(1, 100),
                #"Job Title": fake.job(),
                #"Company": fake.company(),
                #"Lorem Ipsum Text": fake.text(),
            }
            data.append(entry)

        return pd.DataFrame(data)

if __name__ == "__main__":
    profiler = PersonProfile(outputFilename="../Outputs/PersonProfiles-rbd.csv")
    fake_data_df = profiler.generate_fake_profile()
    today = datetime.now()
    print(f"18 years ago = {today.year - 18}/{today.month}/{today.day}")
## Dataframe with Fake Data
    print(f"Number of Records Generated = {len(fake_data_df)}")
    fake_data_df.to_csv(profiler.output_filename, index=False )
    