# Shopify-Image-Repository

## Challenge Overview
My aunt owns a lovely restaurant in Lubbock, Texas called Dragon Buffet which serves the local people with delicious traditional Chinese food. </br>
I want to build a website for restaurant Dragon Buffet to help them digitalize their products. </br>
<br/><br/>

## Tech stacks Overview
- Programming languages: Python, HTML, CSS
- Frameworks and tools: FastAPI, Docker, Jinja2, SQLite DB
<br/><br/>


## Application Usage
### Features and endpoints
- /: Application main page 
- /search: Search products based on product name
- /add: Add products into database
- /purchase: Purchase products
<br/><br/>

### How to run the application
- Clone the github repo
```
git clone https://github.com/xjhee/Shopify-Image-Repository

```

- Go to current directory 
```
cd Shopify-Image-Repository

```

- Build docker image
```
build -t imageapp .
```

- Run docker image on local host
```
docker run -d -p  8000:8000 imageapp
```

- Go to http://0.0.0.0:8000 for main page

<br/><br/>

### How to test the appliation features
#### Homepage
- Go to http://0.0.0.0:8000/
![alt text](https://github.com/xjhee/Shopify-Image-Repository/blob/master/images/app-homepage.png)

#### Search product based on product name
- Go to http://0.0.0.0:8000/search
- Input the name of product you want to search
- Click on submit buttom
![alt text](https://github.com/xjhee/Shopify-Image-Repository/blob/master/images/app-search.png)

#### Add product to database
- Go to http://0.0.0.0:8000/add
- Input id, name, price, stock, file (Please refer to the /test folder for test images)
- Click on submit buttom
![alt text](https://github.com/xjhee/Shopify-Image-Repository/blob/master/images/app-add.png)

#### Purchase products
- Go to http://0.0.0.0:8000/purchase
- Choose your desired product and click on BUY
![alt text](https://github.com/xjhee/Shopify-Image-Repository/blob/master/images/app-purchase.png)


