import jsonapi_requests

# 'https' will lead to error: "Bad request syntax" from Flask, or
# "jsonapi_requests.request_factory.ApiConnectionError" from the lib
api = jsonapi_requests.orm.OrmApi.config({
    'API_ROOT': 'http://localhost:5000/api/2.0',
    'AUTH': ('basic_auth_login', 'basic_auth_password'),
    'VALIDATE_SSL': False,
    'TIMEOUT': 1,
})

class Person(jsonapi_requests.orm.ApiModel):
    class Meta:
        type = 'person'
        api = api

    name = jsonapi_requests.orm.AttributeField('name')
    married_to = jsonapi_requests.orm.RelationField('married-to')

class Car(jsonapi_requests.orm.ApiModel):
    class Meta:
        type = 'car'
        api = api

    color = jsonapi_requests.orm.AttributeField('color')
    driver = jsonapi_requests.orm.RelationField('driver')

car = Car.from_id(2)

print('car color:', car.color) # request happens here
# Example output: 'red'

print('car driver name:', car.driver.name)
# Example output:  'Kowalski'

print('car driver spouse:', car.driver.married_to.name)
# Example output: 'Kowalska'

print('car driver spouse\'s spouse:', car.driver.married_to.married_to.name)
# Example output: 'Kowalski'

