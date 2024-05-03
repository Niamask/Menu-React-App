from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS')
    return response


@app.route("/")
def hello_world():
    return "Hello, Customers!"


dishes = [
    {
      "id": 1,
      "name": "Meat And Prune Tagine",
      "unitPrice": 12,
      "imageUrl": "https://img.cuisineaz.com/660x660/2013/12/20/i29276-tajine-de-veau-aux-pruneaux.jpeg",
      "ingredients": [
        "beef",
        "Prunes",
        "Onion",
        "Garlic"
      ],
      "soldOut": False
    },
    {
      "id": 2,
      "name": "Meatball Tagine And Eggs",
      "unitPrice": 16,
      "imageUrl": "https://tasteofmaroc.com/wp-content/uploads/2018/02/kefta-tagine-oysy-bigstock-kofta-tajine-kefta-tagine-mo-65105917.jpg",
      "ingredients": [
        "beef",
        "Onion",
        "Fresh Herbs",
        "Tomatoe",
        "Garlic",
        "Eggs"
      ],
      "soldOut": True
    },
    {
      "id": 3,
      "name": "Fish Tagine and Veggies",
      "unitPrice": 15,
      "imageUrl": "https://www.allrecipes.com/thmb/lInWVYJvgpXBGJc14ONsYZu_iIw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/4476673-4b09584e68af4d4e907dc9a34a7f3999.jpg",
      "ingredients": [
        "Fish",
        "Tomatoe",
        "Carrot",
        "Green Bell Pepper",
        "Coriandre"
      ],
      "soldOut": False
    },
    {
      "id": 4,
      "name": "Chicken Tagine With Olives",
      "unitPrice": 16,
      "imageUrl": "https://www.cuisinonsencouleurs.fr/wp-content/uploads/2021/07/tajine-poulet-frites-15-scaled.jpg",
      "ingredients": [
        "Chicken",
        "Red Olive",
        "Onion",
        "French Fried Potatoe",
      ],
      "soldOut": False
    },
    {
      "id": 5,
      "name": "Vegetarian Chickpea Tagine",
      "unitPrice": 16,
      "imageUrl": "https://www.myweekendkitchen.in/wp-content/uploads/2019/09/moroccan_tagine_vegetarian.jpg",
      "ingredients": [
        "chickpea",
        "Onion",
        "Garlic",
        "Tomatoes",
        "Coriandre"
      ],
      "soldOut": False
    },
    {
      "id": 6,
      "name": "Veggies Tagine",
      "unitPrice": 13,
      "imageUrl": "https://fitmencook.com/wp-content/uploads/2020/10/moroccan-chicken-tagine-5.jpg",
      "ingredients": [
        "Onion",
        "Potatoe",
        "Carrot",
        "Zucchini",
        "olive"
      ],
      "soldOut": False
    },
    {
      "id": 7,
      "name": "Artichokes Tagine",
      "unitPrice": 16,
      "imageUrl": "https://www.thespruceeats.com/thmb/Zg0Cunx3TpxdvTatO_dRyuCnwjc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/peasartichoketagine1a-56c1cc085f9b5829f86774dd.jpg",
      "ingredients": [
        "lamb",
        "Artichoke",
        "Green peas",
        "Onion",
        "Lemon"
      ],
      "soldOut": False
    },
    {
      "id": 8,
      "name": "Kefta Tagine",
      "unitPrice": 16,
      "imageUrl": "https://pommedambre.com/app/uploads/2021/04/tajine-boeuf-boulettes_38320782-scaled.jpeg",
      "ingredients": [
        "beef",
        "Onion",
        "Fresh herbs",
        "Garlic",
      ],
      "soldOut": True
    },
    {
      "id": 9,
      "name": "Whiting Meatball Tagine",
      "unitPrice": 14,
      "imageUrl": "https://verygoodrecipes.com/images/blogs/couscous-and-pudding/moroccan-fish-tagine-with-green-olives-72.640x480.jpg",
      "ingredients": [
        "Whiting",
        "Lemon",
        "Fresh herbs",
        "Olive",
        "Red Chilly"
      ],
      "soldOut": False
    },
    {
      "id": 10,
      "name": "Pil Pil Tagine",
      "unitPrice": 15,
      "imageUrl": "https://cache.marieclaire.fr/data/photo/w1000_ci/6k/recette-tajine-crevettes-pil-pil.jpg",
      "ingredients": [
        "Shrimp",
        "Tomatoe",
        "Olive Oil",
        "Garlic",
        "Lemon"
      ],
      "soldOut": False
    },
    {
      "id": 11,
      "name": "Sardine Tagine",
      "unitPrice": 15,
      "imageUrl": "https://www.la-cuisine-marocaine.com/photos-recettes/tajine-sardines-marocaine.jpg",
      "ingredients": [
        "Sardine",
        "tomato",
        "Garlic",
        "Lemon"
      ],
      "soldOut": False
    },
    {
      "id": 12,
      "name": "Mussel Tagine",
      "unitPrice": 16,
      "imageUrl": "https://recettespecial.com/wp-content/uploads/2015/12/Tajine-de-moules-%C3%A0-la-marocaine-1-1.jpg",
      "ingredients": [
        "Mussel",
        "tomato",
        "Garlic",
        "Coriandre",
        "Lemon"
      ],
      "soldOut": False
    },
    {
      "id": 13,
      "name": "Cauliflower Tagine",
      "unitPrice": 12,
      "imageUrl": "https://i.ytimg.com/vi/VUXucp28KoI/maxresdefault.jpg",
      "ingredients": [
        "Cauliflower",
        "Onion",
        "Garlic"
        "Olive",
      ],
      "soldOut": True
    },
    {
      "id": 14,
      "name": "kebda Tagine",
      "unitPrice": 16,
      "imageUrl": "https://pbs.twimg.com/media/FZF8L35WIAEmuT5.jpg",
      "ingredients": [
        "beef liver",
        "tomatoe",
        "Onion",
        "Garlic"
      ],
      "soldOut": False
    },
    {
      "id": 15,
      "name": "Lamb Tagine With Quince",
      "unitPrice": 16,
      "imageUrl": "https://www.deliciousmagazine.co.uk/wp-content/uploads/2018/07/603321-1-eng-GB_lamb-and-quince-tagine-with-chermoula-and-buttered-couscous-768x960.jpg",
      "ingredients": [
        "Lamb",
        "Quince",
        "chicken",
        "Onion",
        "Garlic",
        "almond"
      ],
      "soldOut": False
    },
    {
      "id": 16,
      "name": "Okra Tagine",
      "unitPrice": 15,
      "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiBOAaLnS2iRO3gp2Yy3TYfJ3Mz-xP8xIRJgpz-EOo8w&s",
      "ingredients": [
        "Okra",
        "tomatoe",
        "Onion",
        "Garlic"
      ],
      "soldOut": False
    },
   {
      "id": 17,
      "name": "Eggs Tagine",
      "unitPrice": 15,
      "imageUrl": "https://www.thedeliciouscrescent.com/wp-content/uploads/2017/11/Moroccon-Eggs-Square.jpg",
      "ingredients": [
        "Eggs",
        "tomato",
        "Garlic",
        "Fresh herbs",
      ],
      "soldOut": False
    },

    {
      "id": 18,
      "name": "Apricot Chicken Tagine",
      "unitPrice": 15,
      "imageUrl": "https://4passionfood.com/en/wp-content/uploads/sites/4/2020/09/F3057E4A-85C5-4CAC-B17A-B19FF08C1BC8.jpeg",
      "ingredients": [
        "Chicken",
        "Apricot",
        "Onion",
        "Garlic",
        "almond"
      ],
      "soldOut": False
    }
  
  ]

tajines = ["Meat And Prune Tagine", "Chicken Tagine With Olives", "Fish Tagine and Veggies", "Meatball Tagine And Eggs", "Vegetarian Chickpea Tagine", "Veggies Tagine", "Artichokes Tagine", "Kefta Tagine" ,  "Whiting Meatball Tagine", "Pil Pil Tagine", "Sardine Tagine", "Mussel Tagine", "Eggs Tagine", "kebda Tagine", "Lamb Tagine With Quince", "Okra Tagine", "Cauliflower Tagine", "Apricot Chicken Tagine"]
EXTERNAL_API_URL = "https://react-fast-pizza-api.onrender.com/api/order"

all_dishes = {
    "status":'success',
    "data": dishes
}

@app.route("/all_dishes")
def get_menu():
    return jsonify(all_dishes)

# Order 18 different dishes
@app.route("/order", methods=['POST'])
def create_order():
    # EXTERNAL_API_URL = "https://react-fast-pizza-api.onrender.com/api/order"
    data = request.get_json()
    response = requests.post(EXTERNAL_API_URL, json=data)
    myResponse = response.json()
    for item in myResponse["data"]["cart"]:
        # print(item)
        # print(item["pizzaId"])
        # print(tajines[item["pizzaId"]-1])
        item["name"] = tajines[item["pizzaId"]-1]
        
    # print("the response is : ", myResponse)
    return jsonify(myResponse)

# get order by id
@app.route("/order/<string:id>")
def get_order(id):
    API = "https://react-fast-pizza-api.onrender.com/api/order/"
    EXTERNAL_API_URL = f"{API}{id}"
    response = requests.get(EXTERNAL_API_URL)
    myResponse = response.json()
    for item in myResponse["data"]["cart"]:
        #  print(item)
        #  print(item["pizzaId"])
        #  print(tajines[item["pizzaId"]-1])
         item["name"] = tajines[item["pizzaId"]-1]
        

    print("the get response is : ", myResponse)
    return jsonify(myResponse)


if __name__ == "__main__":
    app.run(debug=True)

