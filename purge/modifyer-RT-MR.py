import pandas as pd

def read_patient_ids(file_path):
    df = pd.read_csv(file_path)
    return df['PatientID'], df

def filter_common_patients(df, common_patients):
    return df[df['PatientID'].isin(common_patients)]

def main(file1, file2, output1, output2):
    patient_ids1, df1 = read_patient_ids(file1)
    patient_ids2, df2 = read_patient_ids(file2)

    common_patients = set(patient_ids1).intersection(set(patient_ids2))

    filtered_df1 = filter_common_patients(df1, common_patients)
    filtered_df2 = filter_common_patients(df2, common_patients)

    filtered_df1.to_csv(output1, index=False)
    filtered_df2.to_csv(output2, index=False)

    print(f"Filtered data saved to {output1} and {output2}")

if __name__ == "__main__":
    file1 = 'manifest-RT.csv'
    file2 = 'manifest-MR.csv'
    output1 = 'filtered_RTwrtMR.csv'
    output2 = 'filtered_MR.csv'

    main(file1, file2, output1, output2)

