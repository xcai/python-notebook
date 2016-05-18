
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, u, e):
        self.username = u
        self.email = e

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body, category, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Category %r>" % self.name



tags = db.Table('tags',
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
                db.Column('page_id', db.Integer, db.ForeignKey('page.id'))
                )


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship('Tag', secondary=tags,
                           backref=db.backref('pages', lazy='dynamic'))


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)


def many2many():
    t = Tag()
    p = Page()
    db.session.add(t)
    db.session.add(p)
    db.session.commit()


def main():
    db.create_all()
    users = [
        User('admin', 'admin@example.com'),
        User('guest', 'guest@example.com'),
        User('cosmo', 'wcosmo@qq.com'),
        User('cai', 'xcai@163.com'),
        User('lili', 'alili@qq.com'),
        User('shiry', 'shiry@126.com')
    ]
    for u in users:
        db.session.add(u)
    db.session.commit()

    print User.query.all()
    print User.query.filter_by(username='lili').all()
    print User.query.filter(User.email.endswith('example.com')).all()
    print User.query.order_by(User.username.desc()).all()
    print User.query.order_by(User.email.asc()).all()
    print User.query.limit(2).all()
    print User.query.get(3)
    print '===  ', User.query.filter(User.id.between(2, 4)).all()

'''
    py = Category('python')
    c = Category('C')
    js = Category('JavaScript')

    Py = Post("hello python !", "python is pretty cool", py)
    C = Post('hello c', 'my first language is c', c)
    Js = Post('hello js', 'i think is too hard', js)

    db.session.add(py)
    db.session.add(Py)
    db.session.add(c)
    db.session.add(C)
    db.session.add(js)
    db.session.add(Js)
    db.session.commit()

    print "======    ", py.posts
    print "------    ", py.posts.all()
    print db.session.query(Category).all()
    print Py.category.id, Py.category.name, Py.category_id
    print '>>>> ', Post.query.all()
    print ">>> ", Category.query.all()[2].name
'''

if __name__ == '__main__':
    main()
    # many2many()