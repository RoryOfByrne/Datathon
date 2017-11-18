import pandas as pd
from src.util.constants import TOTAL_TRAINING
from src.features import preprocess as pp


def train_test_split(df, train_percent=0.8):
    '''Randomly samples and splits data into train/test split.'''
    # Uncomment these lines to maintain ordering:
    #split_index = int(df.shape[0] * train_percent)
    #return (df[:split_index], df[split_index:])

    train = df.sample(frac=0.8, random_state=200)
    test = df.drop(train.index)

    return (train, test)

def get_input():
    total_raw = load_csv(TOTAL_TRAINING)

    # TODO: Implement preprocessing
    total_prep = pp.preprocess(total_raw)

    train, test = train_test_split(total_prep)

    return (train, test)


def load_csv(filename):
    '''Reads the input and returns train/test split dataframes.
       Both dataframes will have N feature columns followed by a column labeled
       y.'''
    input_df = pd.read_csv(filename)

    return input_df