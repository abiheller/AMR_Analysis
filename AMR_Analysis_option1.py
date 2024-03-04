#This version pulls the selected columns, puts it into a new df and saves it as a csv. 
import os
import argparse
import pandas as pd

def process_csv(input_file, output_file):
    """ 
    Concatenates and organizes raw response files 
    
    Parameters
    ----------
    input_file: individual csv file
    output_file: name of file you want data organized into
    
    Returns
    -------
    output_file: organized/concatenated CSV
    """
    df = pd.read_csv(input_file)
    selected_columns = df[["cond", "study_test", "test_match", "rsp", "rsp_time"]]
    selected_columns['SourceFile'] = os.path.basename(input_file)
    selected_columns.to_csv(output_file, index=False)

def concat_csvs(input_folder, output_folder):
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".csv"):
            input_file_path = os.path.join(input_folder, file_name)
            output_file_path = os.path.join(output_folder, f"processed_{file_name}")
            process_csv(input_file_path, output_file_path)

def main():
    parser = argparse.ArgumentParser(description="Process data.")
    parser.add_argument("input_folder", help="Path to the input folder")
    parser.add_argument("output_folder", help="Path to the output folder")
    
    args = parser.parse_args()
    
    concat_csvs(args.input_folder, args.output_folder)

if __name__ == "__main__":
    main()

