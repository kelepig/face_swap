import base64
import requests
from tkinter.filedialog import askopenfilename

def img2img():
    url = 'http://127.0.0.1:7000/faceswap/v1/img-img'

    input_path = '1.jpg'
    # with open(input_path, 'rb') as f:
    #     image = f.read()
    #     f.close()
    source_path = '2.jpg'
    # with open(source_path, 'rb') as f:
    #     source = f.read()
    #     f.close()
    data = {
            'input_type' : 'Image',
            'image' : open(input_path, 'rb'),
            'source' : open(source_path, 'rb'),
        }
    resp = requests.post(url=url, data=data) 

    with open('from_server.png', 'wb') as f:
        f.write(resp.content)

def img2imghq():
    url = 'http://127.0.0.1:7000/faceswap/v1/img-img/hq'
    data = {
            'input_type' : 'Image',
            'image_path' : askopenfilename(),
            'source_path' : askopenfilename(),
        }
    resp = requests.post(url=url, data=data) 

    with open('from_server.png', 'wb') as f:
        f.write(resp.content)

def img2vid():
    url = 'http://127.0.0.1:7000/faceswap/v1/img-vid'
    data = {
            'input_type' : 'Video',
            'video_path' : askopenfilename(),
            'source_path' : askopenfilename(),
        }
    resp = requests.post(url=url, data=data) 

    with open('from_server.png', 'wb') as f:
        f.write(resp.content)

def img2vidhq():
    url = 'http://127.0.0.1:7000/faceswap/v1/img-vid/hq'
    data = {
            'input_type' : 'Video',
            'video_path' : askopenfilename(),
            'source_path' : askopenfilename(),
        }
    resp = requests.post(url=url, data=data) 

    with open('from_server.png', 'wb') as f:
        f.write(resp.content)

if __name__ == '__main__':
    img2img()
    # img2imghq()
    # img2vid()
    # img2vidhq()