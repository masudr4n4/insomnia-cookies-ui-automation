import random
import datetime
num = random.choice(range(1, 99999999))
first_name = "Tushar"
last_name = "Mathur"
mobile_number = "9876543212"
tip_amt = 10
count_1 = 1
count_2 = 2
count_3 = 3
count_4 = 4
count_5 = 5
count_6 = 6
count_11 = 11
test_project_token = "_GVlq7uzoAQI5vZdQJ8uUt7LzKFsRgxh--Sn8SeddpM1"
cc_number = "4111 1111 1111 1111"
cvc = "325"
zip = "65425"
expire_date = "02/22"
email = "ictusharmathur" + str(num) + "@gmail.com"
pwd = "Judge@123"
uname = "ictest@judge.com"
uname2 = "user_edit@gmail.com"
password = "Judge@1234"
password2 = "Global@123"
gift_card_number = "601000000000001"
address_dict = {
    "Wallstreet": "Insomnia Cookies Wall Street",
    "BrynMawr": "Insomnia Cookies Bryn Mawr",
    "TestStore": "10 Campus Blvd Newtown Square, PA",
    "Athens": "Insomnia Cookies Athens",
    "Greenwich": "Insomnia Cookies Greenwich",
}
product_list = ['Oatmeal Raisin']
wearable_product_lst = ['Tough Cookie Tank']
product_address_dict = {}
contact_page_dict = {
    "orderNumber": "1993410376",
    "fullName": "Prateek Nehra",
    "emailAddress": "icprateeknehra@gmail.com",
    "mobileNumber": "8724657382",
    "comment": "Test Comments",
    "organisationName": "ICTest",
    "eventLocation": "Mainstay suites philadelphia",
    "eventDate": "1st July 2020",
    "eventType": "Birthday Party",
    "proposedLocation": "1084 lancaster avenue Bryn Mawr",
    "phoneNumber": "8927465718",
    "productName": "Insomniac",
    "productCost": "$29"
}
donation_page_dict = {
    "fullName": "Vijay Lachwani",
    "organizationName": "Judge",
    "emailAddress": "icvijaylachwani@gmail.com",
    "mobileNumber": "8724657382",
    "comment": "Test Comments"
}
fullname = "Prateek Nehra"

location_page_dict = {
    "address": "Insomnia Cookies Wall Street",
    "Greenwich": "116 Macdougal St, New York City, NY",
    "TestStore": "10 Campus Blvd Newtown Square, PA",
    "WhiteHouse": "1600 Pennsylvania Avenue",
    "TestStore": "10 campus blvd, newtown square, pa",
    "YoungsTown": "112 w commerce st youngstown"
}
customised_date = "Friday,Jun 5th"

year_from_now = datetime.datetime.now() + datetime.timedelta(days=365)

checkout_page_dict = {
    "firstName": "Judge",
    "lastName": "Test",
    "phoneNumber": "8975674637",
    "email": "icprateeknehra@gmail.com",
    "cardHolderName": "Test",
    "cardNumber": "4111111111111111",
    "expirationDate": year_from_now.strftime("%m%y"),
    "cvvNumber": "111",
    "zipCode": "19010",
    "message": "test message",
    "dormAddress": "Bryn Mawr College - Rockefeller Hall",
    "fedEX_home_del": "FedEx Home Delivery",
    "fedEx_2day": "FedEx 2Day",
    "alphaNumeric_Fname": "Prateek1234",
    "alphanumeric_Lname": "1243Nehra",
    "schoolcash_number": "6010000000000001"
}

coupons_dict = {
    "discountcoupon": "TestCoupon",
    "freedelivery": "DELIVERY10",
    "percentagecoupon": "WarmGifts",
    "productcoupon": "12Free"
}
