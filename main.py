from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)

def dashboard_stats():
    total_users = User.query.count()

    total_orders = Order.query.count()

    revenue = db.session.query(
        func.sum(Order.amount)
    ).scalar()

    return {
        "users": total_users,
        "orders": total_orders,
        "revenue": revenue
    }

with app.app_context():
    db.create_all()

    db.session.add(User())
    db.session.add(Order(amount=500))

    db.session.commit()

    print(dashboard_stats())
