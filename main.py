from app import app


from posts.blueprint import posts
from users.blueprint import users


### Регистрация Blueprint-ов ###

app.register_blueprint(posts, url_prefix='/posts')
app.register_blueprint(users, url_prefix='/users')

### Админка ###
# admin.add_view(ModelView(User, db.session))
# admin.add_view(ModelView(Post, db.session))



### Запуск приложения ###

if __name__ == '__main__':
    app.run(host='')