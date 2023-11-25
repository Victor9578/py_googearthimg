import json,requests,random

url_googearth: str = "https://earthview.withgoogle.com/_api/photos.json"
url_imgjson:str = "https://earthview.withgoogle.com/_api/"

def img_fromgoog(url: str) -> str:
    respone = requests.get(url).content
    return respone

def main():
    photo_json:str = img_fromgoog(url_googearth)
    url_photo = url_imgjson + json.loads(photo_json)[int(random.random()*2000)]["slug"] + '.json'
    urlending = json.loads(img_fromgoog(url_photo))['photoUrl']
    print(urlending)
    print(type(img_fromgoog(urlending)))
    with open('./1.jpg','wb') as f:f.write(img_fromgoog(urlending))
main()

