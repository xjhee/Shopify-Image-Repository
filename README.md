# Shopify-Image-Repository

## Challenge overview
My aunt owns a lovely restaurant in Lubbock, Texas called Dragon Buffet which serves the local people with delicious traditional Chinese food. </br>
I want to build a website for restaurant Dragon Buffet to help them digitalize their products. </br>



## Tech stacks overview
This project is implemented in Python with sqlite as database storage. It is served with FastAPI as backend and deployed with Docker.


## Features
- Search products based on product name
- Add products into database
- Purchase products

## Usage
### How to run the application
```
# Clone the github repo
git clone https://github.com/xjhee/Shopify-Image-Repository

# Go to current directory 
cd Shopify-Image-Repository

# Build docker image
build -t imageapp .

# Run docker image on local host
docker run -d -p  8000:8000 imageapp

# Go to http://0.0.0.0:8000 for main page

```

### How to test the appliation
#### Add product to database
- Go to http://0.0.0.0:8000/add
- Input id, name, price, stock, file (png file preferred)
- Click on submit buttom
![alt text](https://github.com/xjhee/Shopify-Image-Repository/blob/master/images/app-add.png)

#### Purchase products
- Go to http://0.0.0.0:8000/purchase
- Choose your desired product and click on BUY
![alt text](https://github.com/xjhee/Shopify-Image-Repository/blob/master/images/app-purchase.png)


