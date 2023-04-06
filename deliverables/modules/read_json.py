#this function reads a single json given its path
# Open the JSON file and read its contents


def read_json(json_path):
    import json
    # Open the JSON file and read its contents
    with open(json_path) as f:
        data = json.load(f)
    
    # Return the loaded data
    return data


# Print the data to verify that it has been loaded correctly
#print(data)
