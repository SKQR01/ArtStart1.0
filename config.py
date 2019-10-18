### Класс конфигурации ###
class Conf(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_DATABASE_URI = "sqlite:///C:\\Users\\SKQR\\Desktop\\ArtStat-master\\data\\db.db"

    UPLOAD_FOLDER = "C:\\Users\\SKQR\\Desktop\\ArtStat-master\\static\\img"
    ALLOWED_EXTENSIONS=set(['png', 'jpg', 'jpeg', 'gif', 'webp'])

    SECRET_KEY = 'Something secret'
