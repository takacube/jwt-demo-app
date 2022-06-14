class User:
    def __init__(self, id, username, password):
        self.__id = id
        self.__username = username
        self.__password = password

    # id
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    # username
    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    # password
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password


    # ドキュメントからオブジェクトへ変換
    @classmethod
    def from_doc(cls, doc):
        if doc is None:
            return None
        user = User(doc['id'],
                    doc['name'],
                    doc['password'])
        return user

    # ドキュメントへ変換
    def to_doc(self):
        doc = { 'id': str(self.id),
                'name': str(self.username),
                'password' : str(self.password) }
        return doc


"""
user = User("1", "Taka", "vadsa").to_doc()
print(f"{user}")

docname = User.from_doc({'id': '1', 'username': 'Taka', 'password': 'vadsa'})
print(docname)
"""
