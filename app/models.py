from app import db

role_user = 0
role_admin = 1


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    role = db.Column(db.SmallInteger, default=role_user)

    def __repr__(self):
        return '<User,%r>' % self.name


class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    body = db.Column(db.String(140))

    timestamp = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):

        return '<Post %r>' % (self.body)