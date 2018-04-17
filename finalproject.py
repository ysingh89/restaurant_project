from flask import Flask, render_template, url_for, redirect, request, jsonify, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/restaurants/JSON')
def restaurantsJSON():
    restaurants = session.query(Restaurant)
    # menuItems = session.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()
    return jsonify(Restaurants=[i.serialize for i in restaurants])

@app.route('/restaurant/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    # restaurants = session.query(Restaurant)
    menuItems = session.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()
    return jsonify(Menuitems=[i.serialize for i in menuItems])

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def restaurantMenuItemJSON(restaurant_id,menu_id):
    # restaurants = session.query(Restaurant)
    menuItem = session.query(MenuItem).filter_by(id=menu_id, restaurant_id = restaurant_id).first()
    return jsonify(MenuItem=[menuItem.serialize])

@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    restaurants = session.query(Restaurant)
    if(restaurants):
        return render_template('restaurants.html',restaurants = restaurants)
    else:
        return render_template('nodatafound.html', message = "No restaurants found in the database")
    return "This page will show many restaurants"


@app.route('/restaurant/new', methods = ['GET','POST'])
def newRestaurant():
    if(request.method == "POST"):
        newItem = Restaurant(name = request.form['restaurant_name'])
        session.add(newItem)
        session.commit()
        flash("new restaurant created!")
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('newrestaurant.html')
    return "This page will let you add new restaurant"

@app.route('/restaurant/<int:restaurant_id>/edit', methods = ['GET','POST'])
def editRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).first()
    if(request.method == "POST"):
        if(request.form['new_name']):
            restaurant.name = request.form['new_name']
            session.add(restaurant)
            session.commit()
            flash("Restaurant edited")
            return redirect(url_for('showRestaurants'))
    else:
        return render_template('editrestaurant.html',restaurant = restaurant)
    return "This page will let you edit %s restaurant"%restaurant_id

@app.route('/restaurant/<int:restaurant_id>/delete', methods = ['GET','POST'])
def deleteRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).first()
    if(request.method == 'POST'):
        session.delete(restaurant)
        session.commit()
        flash("Restaurant deleted")
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('deleterestaurant.html',restaurant = restaurant)
    return "This page will let you delete %s restaurant"%restaurant_id

@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).first()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    if(restaurant):
        return render_template('menu.html', restaurant = restaurant, items = items)
    else:
        return render_template('nodatafound.html',message = "No restaurant exists with ID %s"%restaurant_id)
    return "This page will show menu for %s restaurant"%restaurant_id

@app.route('/restaurant/<int:restaurant_id>/menu/new', methods = ['GET','POST'])
def newMenuItem(restaurant_id):
    if(request.method == 'POST'):
        newItem = MenuItem(name = request.form['new_item_name'],
                    description = request.form['new_item_description'],
                    price = request.form['new_item_price'],
                    course = request.form['new_item_course'],
                    restaurant_id = restaurant_id)
        session.add(newItem)
        session.commit()
        flash("New menu item added")
        return redirect(url_for('showMenu',restaurant_id = restaurant_id))
    else:
        return render_template('newmenuitem.html',restaurant_id = restaurant_id)
    return "This page will let you add new menu item to %s restaurant"%restaurant_id

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit', methods = ['GET','POST'])
def editMenuItem(restaurant_id, menu_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).first()
    item = session.query(MenuItem).filter_by(id = menu_id, restaurant_id = restaurant_id).first()
    if(item and restaurant):
        if(request.method == 'POST'):
            if(request.form['new_item_name']):
                item.name = request.form['new_item_name']
            if(request.form['new_item_price']):
                item.price = request.form['new_item_price']
            if(request.form['new_item_course']):
                item.course = request.form['new_item_course']
            if(request.form['new_item_description']):
                item.description = request.form['new_item_description']
            session.add(item)
            session.commit()
            flash("menu item edited")
            return redirect(url_for('showMenu',restaurant_id = restaurant_id))
        else:
            return render_template('editmenuitem.html',restaurant_id = restaurant_id, item = item)
    else:
        return render_template('nodatafound.html',message = "No data found with given IDs")

    return "This page will let you edit menu item %s"%menu_id

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete', methods = ['GET','POST'])
def deleteMenuItem(restaurant_id,menu_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).first()
    item = session.query(MenuItem).filter_by(id = menu_id, restaurant_id=restaurant_id).first()
    if(request.method == 'POST'):
        session.delete(item)
        session.commit()
        flash("menu item edited")
        return redirect(url_for('showMenu',restaurant_id = restaurant_id))
    else:
        return render_template('deletemenuitem.html',restaurant_id = restaurant_id, item = item)
    return "This page will let you delete menu item %s "%menu_id






if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host ='0.0.0.0',port = 5000)
