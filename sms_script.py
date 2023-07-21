import keys
import time
from twilio.rest import Client
import random
import schedule

account_sid = keys.account_sid
auth_token = keys.auth_token
client = Client(account_sid, auth_token)
picture_list = ['https://i.pinimg.com/736x/d7/d4/00/d7d400619965cc9e6af0886d27d613ed.jpg', 'https://www.goodmorningwishes.in/wp-content/uploads/2022/01/Good-Morning-for-sweet-gf.png3_.jpg',
            'https://ih1.redbubble.net/image.1739626393.2039/st,small,507x507-pad,600x600,f8f8f8.jpg', 'https://www.autostraddle.com/wp-content/uploads/2012/09/long-distance-relationship-pic.jpg',
            'https://dancingwithher.com/wp-content/uploads/2021/03/Fox-Kin-photography-New-South-Wales-Australia-rainforest-waterfal-older-lesbian-gay-same-sex-couple-love-photos-Dancing-With-Her-Australian-magazine-6.jpg',
            'https://64.media.tumblr.com/24ea7cb334ec48663d1e289b0532a91f/1e4ddfe597c3e030-2d/s1280x1920/07d12fbb288ae66b83d15bfc0886b134ec8c06d0.gif',
            'https://mario.wiki.gallery/images/thumb/3/3e/MPSS_Mario.png/640px-MPSS_Mario.png', 'https://www.bleepstatic.com/content/hl-images/2023/06/23/super-mario-bros.jpg',
            'https://ntvb.tmsimg.com/assets/p184536_b_h8_dg.jpg']

body_list = ['Good morning baby! I hope you slept well', 'I love you Princess, Good morning!', 'I loaf you!', 'Idunoba my love!',
             'I will stand between the heavens and the earth, I wil tell you where you are! Do you love me?', 'I love you Julia!']


def job():
    random.shuffle(body_list)
    random.shuffle(picture_list)

    message = client.messages.create(body=random.choice(body_list),
                                     from_=keys.from_number,
                                     media_url=random.choice(picture_list),
                                     to=keys.to_number)
    print(message.body)

def schedule_job():
    schedule.every().day.at("07:00").do(job)


schedule_job()

while True:
    schedule.run_pending()
    time.sleep(1)