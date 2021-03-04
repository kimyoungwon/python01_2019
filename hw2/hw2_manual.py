
def parse(file_name, int_cols):
    """
    Parses the CSV file specified by file_name and returns the data as a list
    of dictionaries where each row is represented by a dictionary that
    has keys for each column and value which is the entry for that column
    at that row.

    Also takes a list of column names that should have the data for that column
    converted to integers. All other data will be str.
    """
    data = []
    with open(file_name) as f:
        headers = f.readline().strip().split(',')
        num_cols = len(headers)

        for line in f.readlines():
            row_data = line.strip().split(',')
            row = {}
            for i in range(num_cols):
                if headers[i] in int_cols:
                    row[headers[i]] = int(row_data[i])
                else:
                    row[headers[i]] = row_data[i]
            data.append(row)
    return data


# Write your solutions here!
def species_count(data):
    """
    Returns the number of unique Pokemon species found in the dataset. 

    Takes the dataset(dictationary as an arguments.
    """
    species = []
    for line in data: 
        if line['name'] not in species:
            species.append(line['name']) 
    return len(species)

def max_level(data):
    """
    Returns a tuple of length 2, where the first element is 
    the name of the Pokemon and the second is its level. 

    Takes the dataset(dictationary as an arguments.   
    """
    max_key = None
    max_value = 0
    for line in data:
        if line['level'] > max_value:
            max_key = line['name']
            max_value = line['level'] 
    return (max_key, max_value)

def filter_range(data, smallest, largest):
    """
    Returns a list of Pokemon names having a level within that range. 

    Takes as arguments a smallest (inclusive) and largest (exclusive) level value .   
    """
    species = []
    for line in data:
        if line['level'] >= smallest and line['level'] < largest:
            species.append(line['name'])
    return (species) 
    
def mean_attack_for_type(data, pokemon_type):
    """
    Returns the average attack stat for all the Pokemon in the dataset with that type.
    If there are no Pokemon of the given type, this function should return None.
    
    Take a Pokemon type (string) as an argument
    """
    all_type = []
    attack = []
    for line in data:
        all_type.append(line['type'])
    
    for line in data:       
        if line['type'] == pokemon_type and pokemon_type in all_type:
            attack.append(line['atk'])
    
        elif pokemon_type not in all_type:
            return None
    average = sum(attack)/len(attack)
    return average

def count_types(data):
    """
    Returns a dictionary with keys that are Pokemon types and values 
    that are the number of times that type appears in the dataset.

    Takes the dataset(dictationary as an arguments.
    """
    type_data = {}
    for line in data:
        if line['type'] in type_data.keys():
            type_data[line['type']] += 1
        else:
            type_data[line['type']] = 1            
    return type_data

def highest_stage_per_type(data):
    types_stages = {}
    for line in data:
        if line['type'] in types_stages.keys():
            if line['stage'] >= types_stages[line['type']]:
                types_stages[line['type']] = line['stage']
            else:
                types_stages[line['type']] = types_stages[line['type']]
        else:
            types_stages[line['type']] = line['stage']
    return types_stages

def mean_attack_per_type(data):
    types_atks = {}
    type_count = count_types(data)
    for line in data:
        if line['type'] in types_atks.keys():
            types_atks[line['type']] = types_atks[line['type']] + line['atk']
        else:
            types_atks[line['type']] = line['atk']
    
    for key in type_count.keys():
        types_atks[key] = types_atks[key]/type_count[key]
    return types_atks

    