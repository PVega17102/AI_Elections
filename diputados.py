from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from zlib import crc32
from sklearn.model_selection import train_test_split
from scipy.stats import binom



def read_csv(filename):
    data = pd.read_csv(filename, error_bad_lines=False, skip_blank_lines=True)
    return data

# Example usage
filename = 'diputados_modificado.csv'  # Replace with the path to your CSV file
csv_data = read_csv(filename)

# Accessing the data
print(csv_data.head())  # Print the first few rows of the data
print(csv_data.info()) 
print(csv_data['ID_CASILLA'].value_counts())
print(csv_data.describe())

#This code help to 
IMAGES_PATH = Path() / "images" / "end_to_end_project"
IMAGES_PATH.mkdir(parents=True, exist_ok=True)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = IMAGES_PATH / f"{fig_id}.{fig_extension}"
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)

plt.rc('font', size=14)
plt.rc('axes', labelsize=14, titlesize=14)
plt.rc('legend', fontsize=14)
plt.rc('xtick', labelsize=10, color='#DE0058')
plt.rc('ytick', labelsize=10, color='#DE0058')

csv_data.hist(bins=50, figsize=(12, 8), color='purple')
save_fig("attribute_histogram_plots")
plt.show()

def shuffle_and_split_data(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

train_set, test_set = shuffle_and_split_data(csv_data, 0.2)
len(train_set)
len(test_set)
def is_id_in_test_set(identifier, test_ratio):
    return crc32(np.int64(identifier)) < test_ratio * 2**32

def split_data_with_id_hash(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: is_id_in_test_set(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]
csv_data_with_id = csv_data.reset_index()  # adds an `index` column
train_set, test_set = split_data_with_id_hash(csv_data_with_id, 0.2, "index")
csv_data_with_id["id"] = csv_data["ESTADO"] * 1000 + csv_data["TOTAL_VOTOS"]
train_set, test_set = split_data_with_id_hash(csv_data_with_id, 0.2, "id")

train_set, test_set = train_test_split(csv_data, test_size=0.2, random_state=42)
test_set["NUM_BOLETAS_EXTRAIDAS"].isnull().sum()

sample_size = 1000
ratio_female = 0.511
proba_too_small = binom(sample_size, ratio_female).cdf(485 - 1)
proba_too_large = 1 - binom(sample_size, ratio_female).cdf(535)
print(proba_too_small + proba_too_large)

