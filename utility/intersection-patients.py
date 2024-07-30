import pandas as pd

def read_unique_patient_ids(file_path):
    df = pd.read_csv(file_path)
    return set(df['PatientID'])

def get_unique_and_common_patients(file1, file2, file3):
    patients1 = read_unique_patient_ids(file1)
    patients2 = read_unique_patient_ids(file2)
    patients3 = read_unique_patient_ids(file3)

    unique_count1 = len(patients1)
    unique_count2 = len(patients2)
    unique_count3 = len(patients3)

    common_1_and_2 = len(patients1.intersection(patients2))
    common_1_and_3 = len(patients1.intersection(patients3))
    return unique_count1, unique_count2, unique_count3, common_1_and_2, common_1_and_3

if __name__ == "__main__":
    file1 = 'manifest-RT.csv'
    file2 = 'manifest-CT.csv'
    file3 = 'manifest-MR.csv'


    unique_count1, unique_count2, unique_count3, common_1_and_2, common_1_and_3 = get_unique_and_common_patients(file1, file2, file3)
    
    print(f"Unique Patients in RT: {unique_count1}")
    print(f"Unique Patients in CT: {unique_count2}")
    print(f"Unique Patients in MR: {unique_count3}")
    print(f"Common Patients between RT-CT: {common_1_and_2}")
    print(f"Common Patients between RT-MR: {common_1_and_3}")
