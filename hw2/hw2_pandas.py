
import pandas as pd


# Write your functions here!
def parse (file_name):
    return pd.read_csv(file_name)

def species_count(data):
    return len(data['name'].unique())

def max_level(data):
    val = data.loc[data['level'].idxmax()]
    return val['name'], val['level']

def filter_range(data, smallest, largest):
    filtered = data[(data['level'] >= smallest) 
                    & (data['level'] < largest)]
    return list(filtered['name'])

def mean_attack_for_type(data, pokemon_type):
    if pokemon_type in dict(data['type']).values():
        return (data.groupby('type')['atk'].mean())[pokemon_type]
    else:
        return None

def count_types(data):
    return dict(data.groupby('type')['type'].count())

def highest_stage_per_type(data):
    return dict(data.groupby('type')['stage'].max())

def mean_attack_per_type(data):
    return dict(data.groupby('type')['atk'].mean())    
