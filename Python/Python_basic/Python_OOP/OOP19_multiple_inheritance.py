class Camera:
    def take_photo(self):
        print("take a photo")
    def delete_photo(self):
        print("delete a photo")
    def browse(self):
        print("browse photo album")

class Phone:
    def call(self, number):
        print("calling {}".format(number))
    def send_sms(self, number, message):
        print("sending {} to {}".format(message, number))

class MediaPlayer:
    def play(self):
        print("playing a song/video")
    def browse(self):
        print("browse media")

# Multiple inheritance
class SmartPhone(Camera, Phone, MediaPlayer):
    print("share ...")

if __name__ == '__main__':
    s = SmartPhone()
    s.take_photo()
    s.send_sms("1234","Hi")
    s.play()
    s.browse()