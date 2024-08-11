import random
import pandas as pd

class ClinicalProfile:
    def __init__(self, outputFilename):
        self.output_filename: str | None = outputFilename
        self.num_entries: int = 365

    def calculateBloodPressure(self) -> str:
        systolic = random.randint(110, 180)
        diastolic = random.randint(70, 120)

        if (diastolic < systolic):
            return str(systolic) + "/" + str(diastolic)
        else:
            print(f"**** Diastolic: {diastolic}, Systolic: {systolic} ****")
            return self.calculateBloodPressure()

    def calculateSmoking(self) -> bool:
        s = random.randint(1, 10)
        if s > 5:
            return True
        else:
            return False
        
    def generate_fake_profile(self):
        data = []
        count=0
 
        for _ in range(self.num_entries):
            count += 1
            
            entry = {
                "id": count,
                "smokes": self.calculateSmoking(),
                "glcose": random.randint(80, 130),
                "a1c": round(random.uniform(5.0, 7.0), 2),
                "cholesterol": random.randint(150, 300),
                "bloodPressure": self.calculateBloodPressure()
                }
            data.append(entry)
        
        return pd.DataFrame(data)

if __name__ == "__main__":
    profiler = ClinicalProfile(outputFilename="Outputs/ClinialProfiles.csv")
    fake_data_df = profiler.generate_fake_profile()

## Dataframe with Fake Data
    print(f"Number of Records Generated = {len(fake_data_df)}")
    fake_data_df.to_csv(profiler.output_filename, index=False )