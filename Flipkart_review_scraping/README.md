# Summary:
### **Project Title:** Flipkart review Scraping Application.

### **Project Description:**
`Flipkart review Scraping Application` is a versatile and powerful web scrapping project that allows you to extract reviews for all the different products, store it in a structured manner in Mongo DB database and showcases sample data. This Project combines the capabilities of Flask, a lightweight web framework, Python for scrapping and MongoDB for data storage, and BeautifulSoup for parsing HTML, making it a comprehensive solution for web data extraction and visualization.

### **Key Features:**
* Flexible website scrapping
* User-Friendly Interface
* Data Storage in MongoDB
* Data Visualization

### **Pre Requisites to run the project:**
* Mongo DB atlas Account.
* Python Understanding
* MongoDB CRUD Operations
* Understanding on BeautifulSoup and Flask

### Getting Started.
**Please find the Steps below to Run the Project:**
* Clone the repository onto your local system.
* create `.env` file in project folder. The file should contain USERID and PASSCODE. (Ex: `USERID = 'abc', PASSCODE = 'abc'`)
* Create a python virtual environment and install all the packages mentioned in requirement.txt file.
* Run application.py file.
* Once the application executes, you will be getting a URL in the termina window, that will redirect you to a HTML page.
  
  ![terminal](https://github.com/Kashyap-08/Projects/assets/72156887/8c6076de-5f7f-4919-9d3b-13c6e682be7d)

* The HTML Page is shown below:
  
  ![category](https://github.com/Kashyap-08/Projects/assets/72156887/6f3c632c-bb63-4be0-9a46-c5168daa74ba)

* You can choose  the category from the dropdown box. [**Note:** Every Category has it's own will create a separate DB]
* Then Enter the Product name for which you are extracting data for. [**Note:** Every new product name will create new table/collection]
* Copy and paste the URL from Flipkart official website. Steps to copy the URL is mentioned below.
  - Step1: Visit the Flipkart official website.
  - Step2: Search product for which you want to extract review.
  - Step3: Once you are on the product page. Scroll below and look for `all review` button as shown in image below.
    
    ![flipkart_review](https://github.com/Kashyap-08/Projects/assets/72156887/2bc95560-db59-4057-91fd-9f30d270ccc0)
  
  - Step4: Once you click on the button, you will be able to see all the reviews.
    
    ![copy_url](https://github.com/Kashyap-08/Projects/assets/72156887/023fa902-dace-401e-9a01-3ac4dfefe5f6)
  
  - Step5: Copy the URL of the page and paste it into `Enter URL` text box.

* You may have hundreds of review. Enter the Number of Pages for which you want to extract review for.
* Once the form is filled. Hit search to get the reviews. Below images shoes example.
  
  ![form_filled](https://github.com/Kashyap-08/Projects/assets/72156887/9d40df11-7a2e-42d8-8a21-30dfdc516551)

  Here i am extracting review for `SAMSUNG Galaxy Z Fold5` product and wanted to extract review for only 1 page.
  
* Once all the data is extracted, the data will be stored in mongo DB and displays top 10 records on the page.
  
  ![extracted_review](https://github.com/Kashyap-08/Projects/assets/72156887/addb7aec-8f41-49e6-9086-cc61b8bd1ed2)




**Note:** Feel free to customize this project description to highlight any specific features, benefits, or use cases that are unique to your project.
