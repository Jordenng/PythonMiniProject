import json
import requests


class BasePost:
    res = requests.get("https://jsonplaceholder.typicode.com/posts")
    json_string = json.dumps(res.text)  # string
    data = json.loads(json_string)  # unicode
    json_list = json.loads(res.text)  # list
    my_data = eval(data)  # turn unicode to dict

    def __init__(self, user_id, id, title, body):
        self.id = id
        self.userID = user_id
        self.title = title
        self.body = body
        self.global_dict = dict()

    def from_string(self, my_data1):
        for my_dict in my_data1:  # dict
            for key in my_dict:
                setattr(self, key, my_dict[key])

    def create_dict(self, my_data):
        for my_dict in my_data:  # looping over each dict in the list of dicts
            self.global_dict[my_dict['id']] = my_dict  # add to global dict with the key being 'id'


response = requests.get("https://jsonplaceholder.typicode.com/posts")  # fetch data
json_string = json.dumps(response.text)  # convert res to string
data = json.loads(json_string)  # convert string to readable data in unicode type
my_data = eval(data)  # convert unicode type to list made of dicts

