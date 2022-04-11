import pandas as pd
import datetime
import os

# data
TRAINING_DATA_FILE = "data/dow_30_2009_2020.csv"

now = datetime.datetime.now()
# TRAINED_MODEL_DIR = f"trained_models/{now}"
TRAINED_MODEL_DIR = os.path.join("trained_models", datetime.datetime.now().strftime("%m-%d-%Y %H-%M-%S"))
os.makedirs(TRAINED_MODEL_DIR)
TURBULENCE_DATA = "data/dow30_turbulence_index.csv"

TESTING_DATA_FILE = "test.csv"


