import requests
import uuid
import threading

class image_downloader(threading.Thread):
    def __init__(self, url):
        self.url = url
        threading.Thread.__init__(self)
    
    def run(self):
        # download image
        print(f"Downloading image: {self.url}")
        response = requests.get(self.url)
        image_name = f"images/{str(uuid.uuid4())}.jpg"
        with open(image_name, 'wb') as file:
            file.write(response.content)
            print(f"Image downloaded: {image_name}")