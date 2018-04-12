from flask import Flask


app = Flask(__name__)


@app.route('/')
def showRestaurants():
    return "This page will show many restaurants"


@app.route('/restaurant/new')
def newRestaurant():
    return "This page will let you add new restaurant"

@app.route('/restaurant/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    return "This page will let you edit %s restaurant"%restaurant_id

@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    return "This page will let you delete %s restaurant"%restaurant_id

@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    return "This page will show menu for %s restaurant"%restaurant_id

@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
    return "This page will let you add new menu item to %s restaurant"%restaurant_id

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    return "This page will let you edit menu item %s"%menu_id

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id,menu_id):
    return "This page will let you delete menu item %s "%menu_id






if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host ='0.0.0.0',port = 5000)
