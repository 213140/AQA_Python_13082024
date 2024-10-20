# Є вiдкритий API NASA який дозволяє за певними параметрами отримати данi
# у виглядi JSON про фото зробленi ровером “Curiosity” на Марсi. Серед цих
# даних є посилання на фото якi потрiбно розпарсити i потiм за допомогою
# додаткових запитiв скачати i зберiгти цi фото як локальнi файли mars_photo1.jpg ,
# mars_photo2.jpg . Завдання потрiбно зробити використовуючи модуль requests

import requests
import json


def request_for_curiosity_data():
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}
    json_data_from_response = requests.get(url, params).json()
    # Additionally save in json file
    with open('requests_output.json', 'w') as json_file:
        json.dump(json_data_from_response, json_file, indent=4)
    return json_data_from_response

def extract_curiosity_image_links(json_response):
    list_of_urls = []
    all_photos_data_as_list = json_response.get('photos')
    for photo in all_photos_data_as_list:
        list_of_urls.append(photo.get('img_src'))
    return list_of_urls


if __name__ == '__main__':
    curiosity_data = request_for_curiosity_data()
    all_curiosity_photos = extract_curiosity_image_links(curiosity_data)

    for photo_url in all_curiosity_photos:
        photo_response = requests.get(photo_url)
        if photo_response.status_code != 200:
            print("Request failed")
            exit()
        else:
            with open(f"mars_photo{all_curiosity_photos.index(photo_url) + 1}.jpg", 'wb') as photo_file:
                photo_file.write(photo_response.content)

