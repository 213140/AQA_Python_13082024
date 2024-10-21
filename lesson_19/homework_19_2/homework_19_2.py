import requests
from pathlib import Path

BASE_URL = "http://127.0.0.1:8088/"

def upload_picture():
    # Before executing that command image should be placed in folder 'uploads'
    with open(Path("./uploads/IMG-20241002-WA0002.jpg"), 'rb') as file:
        files = {'image': file}
        response = requests.post(BASE_URL + '/upload', files=files)
        return f"Response status code is: {response.status_code}"

def get_image_url_in_json(file_name):
    response = requests.get(BASE_URL + f"/image/{file_name}")
    if response.status_code in [200, 201]:
        return response
    else:
        return  f"Raised error is {response.status_code}"

def delete_image_from_server(file_name):
    response = requests.delete(BASE_URL + f"/delete/{file_name}")
    if response.status_code in [200, 201]:
        return response
    else:
        return  f"Raised error is {response.status_code}"


if __name__ == '__main__':
    print(upload_picture())
    print(get_image_url_in_json("IMG-20241002-WA0002.jpg"))
    # Try check on web browser: http://127.0.0.1:8088/image/IMG-20241002-WA0002.jpg
    print(delete_image_from_server("image.jpg"))