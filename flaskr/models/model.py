from flaskr import db


class UserInfo(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(1024), nullable=False)
    c_time = db.Column(db.DateTime, nullable=False)
    u_time = db.Column(db.DateTime, nullable=False)
    is_delete = db.Column(db.Boolean, default=0, nullable=False)

    # def __str__(self):
    #     return self.username


class SessionInfo(db.Model):
    __tablename__ = 'session_info'
    id = db.Column(db.BigInteger, primary_key=True)
    session_id = db.Column(db.String(1024), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    c_time = db.Column(db.DateTime, nullable=False)

    # def __str__(self):
    #     return self.session_id









