from flask import Flask, render_template

#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}

app = Flask(__name__)


@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    return render_template('restaurants.html',restaurants = restaurants)
    # return "This page will show many restaurants"


@app.route('/restaurant/new')
def newRestaurant():
    return render_template('newrestaurant.html')
    # return "This page will let you add new restaurant"

@app.route('/restaurant/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    return render_template('editrestaurant.html',restaurant_name = restaurant['name'])
    # return "This page will let you edit %s restaurant"%restaurant_id

@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    return render_template('deleterestaurant.html',restaurant_name = restaurant_name)
    # return "This page will let you delete %s restaurant"%restaurant_id

@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    return render_template('menu.html',restaurant_name = restaurant['name'], items = items)
    # return "This page will show menu for %s restaurant"%restaurant_id

@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
    return render_template('newmenuitem.html',restaurant_name = restaurant['name'])
    # return "This page will let you add new menu item to %s restaurant"%restaurant_id

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    return render_template('editmenuitem.html',restaurant_name = restaurant['name'], item = item)
    # return "This page will let you edit menu item %s"%menu_id

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id,menu_id):
    return render_template('deletemenuitem.html',restaurant_name = restaurant['name'], item = item)
    # return "This page will let you delete menu item %s "%menu_id






if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host ='0.0.0.0',port = 5000)
