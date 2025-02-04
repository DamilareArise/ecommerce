def cart_length(request):
    """Returns the total number of items in the cart for the navbar badge."""
    cart = request.session.get('cart', {})
    total_items = sum(item["quantity"] for item in cart.values() if isinstance(item, dict))  

    return {'cart_length': total_items}  

# instance of cart
# cart = {
#     "2": {"quantity": 2, "price": 23},
#     "3": {"quantity": 2, "price": 23},
#     "6": {"quantity": 2, "price": 23},
#     "7": {"quantity": 2, "price": 23}
# }


# cart.values() # dict_values([{"quantity": 2, "price": 23},{"quantity": 2, "price": 23}])