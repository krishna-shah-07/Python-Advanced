from image_downloader import image_downloader

if __name__ == "__main__":
    urls = [
        "https://images.pexels.com/photos/14484311/pexels-photo-14484311.jpeg",
        "https://images.pexels.com/photos/12130817/pexels-photo-12130817.jpeg",
        "https://images.pexels.com/photos/14661923/pexels-photo-14661923.jpeg"
    ]

threads = []

for url in urls:
    thread = image_downloader(url)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()