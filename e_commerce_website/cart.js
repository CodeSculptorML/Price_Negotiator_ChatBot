const product=[
    {
        id:1,
        image:'D:\\Price_Negotiator_E-Commerce_ChatBot\\e_commerce_website\\images\\KTM 390.jpg',
        title:'KTM 390',
        price:'3.10Lakh',
    },
    {
        id:2,
        image:'D:\\Price_Negotiator_E-Commerce_ChatBot\\e_commerce_website\\images\\Royal_himayalan.avif',
        title:'Royal Enfield Himalayan',
        price:'1.83Lakh',
    },
    {
        id:3,
        image:'D:\\Price_Negotiator_E-Commerce_ChatBot\\e_commerce_website\\images\\iphone15.jfif',
        title:'Iphone 15',
        price:'79,000',
    },
    {
        id:4,
        image:'D:\\Price_Negotiator_E-Commerce_ChatBot\\e_commerce_website\\images\\samsung.jfif',
        title:'Samsung',
        price:'74,999',
    },
    {
        id:5,
        image:'D:\\Price_Negotiator_E-Commerce_ChatBot\\e_commerce_website\\images\\lenovo.jfif',
        title:'Lenovo',
        price:'71,991',
    },
    {
        id:6,
        image:'D:\\Price_Negotiator_E-Commerce_ChatBot\\e_commerce_website\\images\\hp.jfif',
        title:'HP',
        price:'70,199',
    },
]
const categories=[...new Set(product.map((item)=>{return item}))]

let cart=document.getElementById('root')
cart.innerHTML=categories.map((item)=>
{
   var {image,title,price}=item;
   return '<div class="box">' +
    '<div class="img-box">' +
        '<img src="' + image + '"></img>' +
    '</div>' +
    '<div class="left">' +
        '<p>' + title + '</p>' +
        '<h2>' + price + '</h2>' +
        '<button>Add to Cart</button>' +
    '</div>' +
'</div>';


}).join('')
document.addEventListener("DOMContentLoaded", function() {
    // Get the chat container element
    var chatContainer = document.getElementById("chat-container");
 
    // Create an iframe element
    var iframe = document.createElement("iframe");
 
    // Set the attributes for the iframe (adjust the source URL as needed)
    iframe.src = "http://127.0.0.1:5000";  // Replace with the URL of your chatbot
    iframe.width = "400";
    iframe.height = "600";
 
    // Append the iframe to the chat container
    chatContainer.appendChild(iframe);
 });
 