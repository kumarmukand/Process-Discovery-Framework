import json


if __name__ == "__main__":
    with open('config.json', 'r') as f:
        config = json.load(f)  
      
    # For description use this format    
    print("".join(config['ALPHA_MINER']['DESCRIPTION']))
    
    # For all other properties
    print(config['ALPHA_MINER']['INPUT'])