from flask import Flask, render_template, request

app = Flask(__name__)

# Your chatbot logic goes here
import nltk
from nltk.chat.util import Chat, reflections

extended_price_negotiation_pairs = [
    ["hi|hello|hey", ["Hello! How may I help you?"]],
    ["show products", ["We have Bikes, accessories, fashion, etc."]],
    ["show available products", ["We have Bikes, accessories, fashion, etc."]],
    ["available products", ["We have Bikes, accessories, fashion, etc."]],
    ["products", ["We have Bikes, accessories, fashion, etc."]],
    ["bikes", ["We have touring bikes, road bikes, mountain bikes. See anything you like? Just ask it."]],
    ["accessories", ["We have mobile phones, laptops, washing machine. See anything you like? Just ask it."]],
    ["fashion", ["We have kids fashion, womens fashion, mens fashion. See anything you like? Just ask it."]],

    ["touring bikes", ["What do you prefer? We have KTM 390, Royal Enfield Himalayan."]],
    ["ktm 390 duke", ["OK, check the link of the product https://www.zigwheels.com/ktm-bikes/duke-390"]],
    ["Royal Enfield Himalayan", ["OK, check the link of the product https://www.royalenfield.com/in/en/motorcycles/new-himalayan/"]],
    ["road bikes", ["What do you prefer? We have Polygon Bend R2,Rockfire ridge 29"]],
    ["Polygon Bend R2", ["OK, check the link of the product https://www.choosemybicycle.com/en/bicycles/polygon-bend-r2-2022"]],
    ["Rockfire ridge 29", ["OK, check the link of the product https://www.choosemybicycle.com/en/bicycles/rockfire-ridge-29"]],
    ["mountain bikes bikes", ["What do you prefer? We have Hercules CX70 18S 26T Black/Fresh Green,Montra Chord Medium Ruby Red"]],
    ["Hercules CX70 18S 26T Black/Fresh Green", ["OK, check the link of the product https://www.trackandtrail.in/cycles/hercules-mtb-single-speed/hercules-topgear-cx70-18s?id=2606"]],
    ["Montra Chord Medium Ruby Red", ["OK, check the link of the product https://www.trackandtrail.in/cycles/offers/montra-chord-offers?id=3834"]],

    ["mobile phones", ["What do you prefer? We have iphone,samsung"]],
    ["iphone", ["OK, check the link of the product https://www.apple.com/in/iphone-15-pro/"]],
    ["samsung", ["OK, check the link of the product https://www.samsung.com/in/"]],
    ["laptops", ["What do you prefer? We have Lenovo,HP"]],
    ["Lenovo", ["OK, check the link of the product https://www.lenovo.com/in/en/"]],
    ["HP", ["OK, check the link of the product https://www.hp.com/in-en/shop/laptops-tablets.html"]],
    ["washing machine", ["What do you prefer? We have LG,Samsung"]],
    ["LG", ["OK, check the link of the product https://www.lg.com/in/refrigerators"]],
    ["Samsung", ["OK, check the link of the product https://www.samsung.com/in/refrigerators/all-refrigerators/"]],


    ["kids fashion", ["What do you prefer? We have T-Shirts, Jeans"]],
    ["T-Shirts", ["OK, check the link of the product https://www.myntra.com/kids-tshirts"]],
    ["Jeans", ["OK, check the link of the product https://www.myntra.com/kids-jeans"]],
    ["womens fashion", ["What do you prefer? We have Western Wear , Ethnic wear"]],
    ["Western Wear", ["OK, check the link of the product https://www.myntra.com/womens-western-wear"]],
    ["Ethnic Wear", ["OK, check the link of the product https://www.myntra.com/womens-ethnic%20wear"]],
    ["mens fashion", ["What do you prefer? We have Shirt,Jeans"]],
    ["Shirt", ["OK, check the link of the product https://www.ajio.com/men-shirts/c/830216013"]],
    ["Jeans", ["OK, check the link of the product https://www.myntra.com/men-jeans"]],

    ["negotiate", ["Do you wish to negotiate?"]],
    #["do you wish to negotiate the discount percentage", ["Yes", "No"]],
    ["price", ["Please check the price on website link."]],
    ["yes", ["Ok Great lets Begin then"]],
    ["no", ["Ohh!That's Fine"]],
    ["show discount", ["If you are lucky, you can get a discount of up to 10-20 percent."]],
    ["available discount", ["If you are lucky, you can get a discount of up to 10-20 percent"]],
    ["discount", ["If you are lucky, you can get a discount of up to 10-20 percent"]],
    ["how much discount", ["If you are lucky, you can get a discount of up to 10-20 percent.How much Discount do you want?"]],
    ["20%", ["That is too much to ask! How about a discount of 10 percent (accept|reject)"]],
    ["accept", ["Tell me your discount percentage?(Just Enter Value)"]],
    ["reject", ["You can continue to negotiate or choose a different product."]],

    ["discount of 18 ", ["Negotiating... How about a discount of 11 percent (Y/N)"]],
    ["discount of 16 ", ["Negotiating... How about a discount of 12 percent(Y/N)"]],
    ["discount of 15 ", ["Negotiating... How about a discount of 12.5 percent (Y/N)"]],
    ["discount of 14 ", ["Negotiating... How about a discount of 13 percent (Y/N)"]],

    ["18", ["Negotiating... How about a discount of 11 percent (Y/N"]],
    
    ["16", ["Negotiating... How about a discount of 12 percent (Y/N)"]],
    ["15", ["Negotiating... How about a discount of 12.5 percent (Y/N)"]],
    ["14", ["Negotiating... How about a discount of 13 percent (Y/N)"]],

    ["how about a discount of 18", ["Negotiating... How about a discount of 11 percent (Y/N)"]],
    ["how about a discount of 16", ["Negotiating... How about a discount of 12 percent (Y/N)"]],
    ["how about a discount of 15", ["Negotiating... How about a discount of 12.5 percent(Y/N)"]],
    ["how about a discount of 14", ["Negotiating... How about a discount of 13 percent (Y/N)"]],
    ["Y", ["Ok hurrah the deal is final Discount at 14 percent"]],
    ["N", ["Feel free to propose another discount percentage."]],

    ["help", ["Sure, I can help you with information about available products, negotiations, and more."]],
    ["what else can you help with", ["I can assist you with product recommendations, order tracking, and any questions you may have."]],
    ["bye|goodbye", ["Goodbye! If you have any more questions, feel free to ask.Happy Shopping"]],
    ["Thank You|Thanks|thnx", ["I am Glad that i was able to help you,Happy Shopping"]],
]

extended_price_negotiation_chatbot = Chat(extended_price_negotiation_pairs, reflections)

# Flask routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form.get("user_input")
    
    # Your chatbot logic goes here
    bot_response = extended_price_negotiation_chatbot.respond(user_input)

    return render_template("chat.html", user_input=user_input, bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)
