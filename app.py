from flask import Flask, jsonify
from flask_restful import Api, Resource, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
api = Api(app)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(50), unique=True, nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.now)    
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    customer = db.relationship('Customer', backref='orders')

class CustomerResource(Resource):
    def get(self):
        customers = Customer.query.all()
        return jsonify([{'id': customer.id, 'name': customer.name, 'code': customer.code} for customer in customers])

    def post(self):
        data = request.json
        customer = Customer(name=data['name'], code=data['code'])
        db.session.add(customer)
        db.session.commit()
        return {'message': 'Customer created successfully', 'id': customer.id}, 201

class OrderResource(Resource):
    def get(self):
        orders = Order.query.all()
        return jsonify([{'id': order.id, 'item': order.item, 'amount': order.amount, 'time': order.time, 'customer_id': order.customer_id} for order in orders])

    def post(self):
        data = request.json
        customer_id = data.get('customer_id')
        customer = Customer.query.get(customer_id)
        if customer:
            order = Order(item=data['item'], amount=data['amount'], customer_id=customer_id)
            db.session.add(order)
            db.session.commit()
            return {'message': 'Order created successfully', 'id': order.id}, 201
        return {'message': 'Customer not found'}, 404

api.add_resource(CustomerResource, '/customers')
api.add_resource(OrderResource, '/orders')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
