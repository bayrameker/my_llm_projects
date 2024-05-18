import argparse
import os
from utils.data_utils import load_data, preprocess_data, split_data, save_preprocessed_data

def main(input_file, output_dir, text_column):
    """
    :param input_file:
    :param output_dir:
    :param text_column:
    :return:
    """

    #Preprocesses the data
    df = load_data(input_file)

    #Split the data into training and test sets
    df = preprocess_data(df, text_column)


    train_df, test_df = split_data(df)


    #Save the processed data
    train_file_path = os.path.join(output_dir, 'train.csv')
    test_file_path = os.path.join(output_dir, 'test.csv')
    save_preprocessed_data(train_df, train_file_path)
    save_preprocessed_data(test_df, test_file_path)

    print(f"Data preprocessing completed. Train data saved to {train_file_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Preprocess data for model training')
    parser.add_argument( '--input_file', required=True, type=str, help='Path to input file')
    parser.add_argument( '--output_dir', required=True, type=str, help='Directory to save preprocessed data')
    parser.add_argument( '--text_column', required=True, type=str, help='Name of the column containing text data')

    args = parser.parse_args()

    main(args.input_file, args.output_dir, args.text_column)
