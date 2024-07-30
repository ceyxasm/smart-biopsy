import sys
import pandas as pd

def concat_csv(files):
    # Read and concatenate the CSV files
    dataframes = [pd.read_csv(file) for file in files]
    concatenated_df = pd.concat(dataframes, ignore_index=True)

    return concatenated_df

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python concat_csv.py <file1.csv> <file2.csv> <file3.csv> [output.csv]")
    else:
        input_files = sys.argv[1:4]
        output_file = sys.argv[4] if len(sys.argv) > 4 else "output.csv"

        concatenated_df = concat_csv(input_files)
        concatenated_df.to_csv(output_file, index=False)

        print(f"CSV files concatenated and saved to {output_file}")

