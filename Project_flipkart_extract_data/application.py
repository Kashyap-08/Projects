from connection import mongoDB
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
import sys
from geocoder import osm
from datetime import date
from dateutil.relativedelta import relativedelta

def get_state_country(city_name):
    '''
    :param city_name: Get the city name for which state and country name needed to be extracted.

    :return: state and country name
    '''
    location = osm(city_name)

    if location.ok:
        state = location.state
        country = location.country
    else:
        state = 'Not Found'
        country = 'Not Found'
    
    return state, country

def fetch_records(url, pages):
    '''
    :param url: Flipkart product review url
    :param pages: Number of pages for which records needed to be fetched.

    :return: data in the from of list containing sets
    '''

    # Store all record in list containing dictionary
    review_data = []

    for i in range(1, int(pages)+1):
        print("------------ FETCHING RECORDS FROM PAGE: ",i, " -----------------------")
        page_no = f'page={i}'
        if 'page=' in url:
            replace_val = url.split('&')[-1]
            url = url.replace(replace_val, page_no)
        else:
            url = url+page_no

        # Get all the script from url
        response = requests.get(url) 

        # parse the html content   
        soup = BeautifulSoup(response.content, 'html.parser')

        # select perticular segemetn form the html
        review_block = soup.find_all('div', {'class':'_27M-vq'})


        for block in review_block:

            try:
                # There are multiple different class names.
                # # TO extract the existing class name and extract value for it we need to execute below code
                all_div = block.find_all('div', class_=True)
                dev_class = all_div[3]['class']
                class_name = ' '.join(dev_class)
                rating_elem = block.find('div', {'class':class_name}).text
                
                review_elem = block.find('p', {'class':'_2-N8zT'}).text
                
                add_on_review = block.find('div', {'class':"t-ZTKy"})

                name_elem = block.find('p',{'class':"_2sc7ZR _2V5EHH"}).text

                location_elem = block.find('p', {'class': '_2mcZGG'}).text

                description = add_on_review.find('div').find('div').text

                
                if 'Certified Buyer' in location_elem:
                    location_elem = location_elem.replace('Certified Buyer, ', '')

            
                date_elem = block.find_all('p', {'class':'_2sc7ZR'})[1].text

            except Exception as e:
                print(e)




            # Get State and country name
            state, country = get_state_country(location_elem)

            # Get the actual date
            
            purchase_month = 0
            if 'months ago' in date_elem:
                purchase_month = int(date_elem[0])

            current_date = date.today() # get todays date
            historic_date = current_date - relativedelta(month = purchase_month) # Subtract month from currrent date
            historic_date = historic_date.strftime('%Y-%m-%d')
        

            dict = {
                'name' : name_elem,
                'rating' : rating_elem,
                'review' : review_elem,
                'description': description,
                'city' : location_elem,
                'state' : state,
                'country' : country,
                'date' : historic_date
            }

            print(dict)

            review_data.append(dict)
    return review_data



application = Flask(__name__)

@application.route('/', methods=['GET','POST'])
def search():
    if request.method == 'GET':
        # redirect to the html page if GET method found
        return render_template('search.html')
    
    else:
        # Get url from the html page
        print("=============== GETTING URL DATA ==========================")
        url, pages = request.form['search'], request.form['num_pages']
        product_name = request.form['product_name']
        DB_name = request.form['category']
        print("-------------- NUMBER OF RECORDS TO FETCH THE DATA FROM -------", pages)
        #print("**************************************** ",DB_name)

        # call fetch_records that will extract all info form the given url
        data = fetch_records(url, pages)

        # get DB connection object
        db_conn = mongoDB.get_db_conn(DB_name)

        # insert data into table
        print("=============== INSERTING DATA TO MONGODB ====================")
        mongoDB.insert(db_conn, product_name, data)

        # Once the data is stored in mongoDB. Get all the data from it
        DB_records = mongoDB.get_all(db_conn, product_name)
        print("=============== EXTRACTED DATA FROM MONGODB ====================")

        # give the data to the result.html page to print it out
        
        return render_template('search.html', results=list(DB_records)[:10])


if __name__ == '__main__':
    application.run(debug=True)