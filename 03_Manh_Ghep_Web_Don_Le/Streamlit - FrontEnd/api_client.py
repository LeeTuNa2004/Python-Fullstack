# Chuyen goi API, khong dinh dang gi toi giao dien Web
import requests

# Goi API lay thong tin cong viec theo ID va tra ve dang Dict
def lay_thong_tin_todo(todo_id, timeout = 5):
    url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.json()

# Goi API lay danh sach cong viec co gioi han so dong (tra ve List cac Dict)
def lay_danh_sach_todos(gioi_han = 5, timeout = 5):
    url = f"https://jsonplaceholder.typicode.com/todos?_limit={gioi_han}"
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.json()
