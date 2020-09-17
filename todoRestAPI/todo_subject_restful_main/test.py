import requests


data_d = {
    "title": "CURD",
    "content": "끝!!!!",
    "is_complete": 0,
    "end_date": "2020-09-18",
}

data = requests.post("http://127.0.0.1:8000/todo_list/create/", data=data_d)
print(data)
