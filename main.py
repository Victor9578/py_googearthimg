import json, requests, random
from PIL import Image

url_googearth: str = "https://earthview.withgoogle.com/_api/photos.json"
url_imgjson1: str = "https://earthview.withgoogle.com/_api/"


def img_fromgoog(url: str) -> str:
    respone = requests.get(url).content
    return respone


def save_jpg() -> str:
    name_img: str = json.loads(img_fromgoog(url_googearth))[int(random.random() * 2000)]["slug"]
    url_imgjson2: str = (
        url_imgjson1
        + name_img
        + ".json"
    )
    url_img: str = json.loads(img_fromgoog(url_imgjson2))["photoUrl"]
    with open("./1.jpg", "wb") as f:
        f.write(img_fromgoog(url_img))
    return name_img

def img_convert():
    Image.open("./1.jpg").convert('L').save("2.jpg")



def __main__():
    save_jpg()
    img_convert()



__main__()