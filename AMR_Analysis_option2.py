
#This version creates a dataframe and fills it from the selected columns from the file in the directory, which seems like it might work better.
import os
import pandas as pd

def process_and_concat_csvs(input_folder, output_file):
    """
    Concatenates and organizes raw response files in a folder
    
    Parameters
    ----------
    input_folder: str
        Path to the folder containing input CSV files.
    output_file: str
        Path to the file where the processed concatenated CSV will be saved.
    """
    # Initialize an empty DataFrame to store the concatenated data
    concatenated_df = pd.DataFrame()

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".csv"):
            input_file_path = os.path.join(input_folder, file_name)
            df = pd.read_csv(input_file_path)
            # Select the desired columns from the CSV file
            selected_columns = df[["cond", "study_test", "test_match", "rsp", "rsp_time"]]
            # Add a column indicating the source file
            selected_columns['SourceFile'] = os.path.basename(input_file_path)
            # Append the selected columns to the concatenated DataFrame
            concatenated_df = pd.concat([concatenated_df, selected_columns], ignore_index=True)
    
    # Save the concatenated DataFrame to a CSV file
    concatenated_df.to_csv(output_file, index=False)

# Example usage
input_folder = "path/to/input_folder"
output_file = "path/to/output_file.csv"
process_and_concat_csvs(input_folder, output_file)

