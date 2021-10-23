from src.utils.all_utils import read_yaml, create_directory
import argparse
import pandas as pd
import os


def get_data(config_path):

    config = read_yaml(config_path)
    remote_data_path = config["data_source"]
    df = pd.read_csv(remote_data_path, sep=";") # read the data and store as a dataframe

    # save the data in local
    # Create path to directory: artifacts/raw_loacl_dir/data.csv
    artifacts_dir =  config["artifacts"]["artifacts_dir"]
    raw_local_dir =  config["artifacts"]["raw_local_dir"]
    raw_local_file = config["artifacts"]["raw_local_file"]

    raw_local_dir_path = os.path.join(artifacts_dir, raw_local_dir)

    create_directory(dirs=[raw_local_dir_path]) # create the directory if it does not exist

    raw_local_file_path = os.path.join(raw_local_dir_path, raw_local_file)
    print(raw_local_file_path) # path to data.csv file
    
    df.to_csv(raw_local_file_path, sep=",", index=False) # save the dataframe as a csv file
    # print(raw_local_file_path)

    # print(df.head())

    # print(config)
    




if __name__ == "__main__":
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")

    parsed_args = args.parse_args()
    get_data(config_path=parsed_args.config) # passing the config path