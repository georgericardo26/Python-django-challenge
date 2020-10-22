from main.models import User


class Dispatcher:
    def __init__(self, obj, qtd):
        self.obj = obj
        self.qtd = qtd
        self.save()

    def save(self):

        for item in self.obj:
            if not User.objects.filter(username=item["login"]).exists():
                user = User()
                user.login = item["login"]