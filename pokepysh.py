import pandas as pd
import json


# Read the CSV File
csv_file = 'pokemon.csv'
df = pd.read_csv(csv_file)


# Selecting the relevant columns from the CSV file

columns = [
    'pokedex_number', 'name', 'type1', 'type2', 'hp', 'attack', 'defense',
    'sp_attack', 'sp_defense', 'speed', 'base_total', 'abilities', 'generation',
    'is_legendary', 'against_bug', 'against_dark', 'against_dragon', 'against_electric',
    'against_fairy', 'against_fight', 'against_fire', 'against_flying', 'against_ghost',
    'against_grass', 'against_ground', 'against_ice', 'against_normal', 'against_poison',
    'against_psychic', 'against_rock', 'against_steel', 'against_water'
]
# Filter added to select only above mentioned column

# Hotfix done to the NaN values from CSV 
#JSON file few data manually edited, pls add checks for NaN and Null 

df = df[columns]

# Parsing the abilities from String to List 

df['abilities'] = df['abilities'].apply(lambda x: json.loads(x.replace("'", "\"")))

#Only taking generation 1  pokemons
df = df[df['generation'] == 1] 


# Converting the dataframe to list of dicitionaries 

data = df.to_dict(orient='records')

#Saving to JSON File

json_file = 'pokemon.json'

with open(json_file, 'w', encoding='utf-8') as f:
	json.dump(data, f, indent=2)

print(f"Successfully Converted {len(data)} Pokemon to {json_file}")

