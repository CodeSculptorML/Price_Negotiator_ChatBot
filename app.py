from flask import Flask, render_template, request

app = Flask(__name__)

# Your chatbot logic goes here
import nltk
from nltk.chat.util import Chat, reflections

extended_price_negotiation_pairs = [
    ["hi|hello|hey", ["Hello!Welcome to Price Negotiation Chatbot"]],
    ["show products", ["We have <br>1.Bikes<br>2.accessories<br>3.fashion<br>4.Watches"]],
    ["show available products", ["We have <br>1.Bikes<br>2.accessories<br>3.fashion<br>4.Watches"]],
    ["available products", ["We have <br>1.Bikes<br>2.accessories<br>3.fashion<br>4.Watches"]],
    ["products", ["We have <br>1.Bikes<br>2.accessories<br>3.fashion<br>4.Watches"]],
    ["Bikes", ["We have <ul><li>touring bikes</li><li>road bikes</li><li> mountain bikes</li></ul>\nSee anything you like? Just ask it."]],
    ["Accessories", ["We have mobile phones, laptops, washing machine. See anything you like? Just ask it."]],
    ["Fashion", ["We have kids fashion, womens fashion, mens fashion. See anything you like? Just ask it."]],
    ["Watches", ["We have smart watch,analog watch. See anything you like? Just ask it."]],

    ["smart watch", ["OK, check the link of the product https://www.flipkart.com/wearable-smart-devices/smart-watches/pr?sid=ajy,buh"]],
    ["analog watch", ["OK, check the link of the product https://www.fastrack.in/shop/analog-watches"]],

    ["touring bikes", ["What do you prefer? We have KTM 390 duke, Royal Enfield Himalayan."]],
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

    ["Negotiate", ["okay..let's begin negotiation.<br>I can Offer 10-20 percent discount.<br>How much discount do you want?<br>1.18 percent<br>2.16 percent<br>3.15 percent<br>4.14 percent.<br>Choose any discount percent from above"]],
    ["Do not negotiate", ["That's fine You can buy the product of your choice at current price"]],
    ["Finalize Deal", ["Hurrah the Deal is finalized at entered percentage amount .Congratulations"]],
    ["Customer Care", ["You can connect with custoner care on the following contact number +91-8378934521 or else you can drop a mail at custonercare12@gmail.com"]],
    
    #["do you wish to negotiate the discount percentage", ["Yes", "No"]],
    ["price", ["Please check the price on website link."]],
    ["yes", ["Ok Great lets Begin then"]],
    ["no", ["Ohh!That's Fine"]],
    ["show discount", ["If you are lucky, you can get a discount of up to 10-20 percent."]],
    ["available discount", ["If you are lucky, you can get a discount of up to 10-20 percent"]],
    ["discount", ["Sure I can Give you a discount of Ranging from 10-20 percent .\n1.18 percent\n2.16 percent\n3.15 percent\n4.14 percent"]],
    ["how much discount", ["If you are lucky, you can get a discount of up to 10-20 percent.How much Discount do you want?"]],
    ["20%", ["That is too much to ask! How about a discount of 10 percent (accept|reject)"]],
    ["accept", ["Tell me your discount percentage?(Just Enter Value)"]],
    ["reject", ["You can continue to negotiate or choose a different product."]],

    ["1", ["Negotiating... How about a discount of 11 percent (Y/N)"]],
    ["2", ["Negotiating... How about a discount of 12 percent(Y/N)"]],
    ["3", ["Negotiating... How about a discount of 12.5 percent (Y/N)"]],
    ["4", ["Negotiating... How about a discount of 13 percent (Y/N)"]],

    ["18 percent", ["Negotiating... How about a discount of 11 percent (Y/N"]],
    
    ["16 percent", ["Negotiating... How about a discount of 12 percent (Y/N)"]],
    ["15 percent", ["Negotiating... How about a discount of 12.5 percent (Y/N)"]],
    ["14 percent", ["Negotiating... How about a discount of 14 percent (Y/N)"]],

    ["Y", ["Ok hurrah the deal is final Discount at 14 percent"]],
    ["N", ["Feel free to propose another discount percentage."]],

    ["help", ["Sure, I can help you with information about available products, negotiations, and more."]],
    ["what else can you help with", ["I can assist you with product recommendations, order tracking, and any questions you may have."]],
    ["bye|goodbye", ["Goodbye! If you have any more questions, feel free to ask.Happy Shopping"]],
    ["Thank You|Thanks|thnx", ["I am Glad that i was able to help you,Happy Shopping"]],
]

extended_price_negotiation_chatbot = Chat(extended_price_negotiation_pairs, reflections)
def chatbot_response(user_input):
    response = extended_price_negotiation_chatbot.respond(user_input)
    if response:
        return response
    else:
        return "I'm sorry, I didn't understand that. Could you please ask me something else?"

# Flask routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form.get("user_input")
    
    # Your chatbot logic goes here
    #bot_response = extended_price_negotiation_chatbot.respond(user_input)
    bot_response=chatbot_response(user_input)
    return render_template("chat.html", user_input=user_input, bot_response=bot_response)

@app.route("/cart")
def cart():
    return render_template("cart.html")

if __name__ == "__main__":
    app.run(debug=True)
