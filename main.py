import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        app_name = "Masaüstü Bildirimi",
        title = "Merhaba Kullanıcı",
        message = "Bir Bilgisayar Bildirimi Görmektesiniz.",

        timeout = 2
    )

    time.sleep(5)