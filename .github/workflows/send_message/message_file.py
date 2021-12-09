import random
import yaml

with open('message_file.yaml', 'r') as f:
    messages = yaml.safe_load(f)
    


for i in messages:
    message1 = i['message_name_1']['message']
    message2 = i['message_name_2']['message']
    message3 = i['message_name_3']['message']
    message4 = i['message_name_4']['message']

    message_list = random.choice[message1, message2, message3, message4]
    print(message_list)
    # print(message1)
