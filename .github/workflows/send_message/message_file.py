import random
import yaml

with open('message_file.yaml', 'r') as f:
    messages = yaml.safe_load(f)
    
message_block_chosed = random.choice(messages)
print(message_block_chosed['message_name']['message'])
   
    


