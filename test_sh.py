import pytest
from app import app, db, Customer, Order


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()


# def test_customer_resource_get(client):
#     # Create sample customers
#     customer1 = Customer(name='Customer 1', code='C001')
#     customer2 = Customer(name='Customer 2', code='C002')
#     db.session.add(customer1)
#     db.session.add(customer2)
#     db.session.commit()

#     # Test GET request to /customers
#     response = client.get('/customers')
#     assert response.status_code == 200
#     data = response.get_json()
#     assert len(data) == 2
#     assert data[0]['name'] == 'Customer 1'


def test_customer_resource_post(client):
    # Test POST request to /customers
    data = {'name': 'New Customer', 'code': 'C003'}
    response = client.post('/customers', json=data)
    assert response.status_code == 201
    assert 'id' in response.get_json()


def test_order_resource_get(client):
    # Create sample customer
    customer = Customer(name='Test Customer', code='TEST')
    db.session.add(customer)
    db.session.commit()

    # Create sample orders
    order1 = Order(item='Item 1', amount=10.0, customer_id=customer.id)
    order2 = Order(item='Item 2', amount=20.0, customer_id=customer.id)
    db.session.add(order1)
    db.session.add(order2)
    db.session.commit()

    # Test GET request to /orders
    response = client.get('/orders')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2
    assert data[0]['item'] == 'Item 1'


def test_order_resource_post(client):
    # Create sample customer
    customer = Customer(name='Test Customer', code='TEST')
    db.session.add(customer)
    db.session.commit()

    # Test POST request to /orders
    data = {'item': 'New Item', 'amount': 30.0, 'customer_id': customer.id}
    response = client.post('/orders', json=data)
    assert response.status_code == 201
    assert 'id' in response.get_json()


if __name__ == '__main__':
    pytest.main(['-v', __file__])
