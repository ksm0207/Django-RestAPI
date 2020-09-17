import requests


data = (requests.get("http://localhost:8000/todo_board/")).json()
print(data)