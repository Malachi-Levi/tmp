from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins='*')


# Dummy user data for demonstration
usersAuth = {
    "Malachi": {"password": "1452", "userID": "1001", "nickname": "M.Levi"},
    "Yuval": {"password": "7854", "userID": "1002", "nickname": "Y.Goddard"},
    # Add more users as needed
}



userList = [
    { 'id': 1, 'title': 'Shaked 1', 'price': 2950000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://rimh2.domainstatic.com.au/iMdZec6ODzasRhO123Hgspg5SV8=/fit-in/1920x1080/filters:format(jpeg):quality(80):no_upscale()/2019018973_1_1_240130_110207-w4000-h2667' },
    { 'id': 2, 'title': 'Oren 2', 'price': 2330000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrato83TcHAL_nD-RexyZ3Ux6qU2yEEMwpprb4U7uPmoz3WtBNPWpvXVXjA9YoqzcKppI&usqp=CAU' },
    { 'id': 3, 'title': 'Shaked 3', 'price': 2870000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://i2.au.reastatic.net/800x600/da835f8a5054cd9ee32fa73b35a6e7ff9a3ade93c27c905bd54011bd3ec56d18/main.jpg' },
    { 'id': 4, 'title': 'Oren 4', 'price': 2290000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=2' },
    { 'id': 5, 'title': 'Shaked 5', 'price': 2400000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=6' },
    { 'id': 6, 'title': 'Oren 6', 'price': 1940000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=8' },
    { 'id': 7, 'title': 'Shaked 7', 'price': 1970000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=3' },
    { 'id': 8, 'title': 'Oren 8', 'price': 1440000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=1' },
    { 'id': 9, 'title': 'Shaked 9', 'price': 2240000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=10' },
    { 'id': 10, 'title': 'Oren 10', 'price': 2380000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=4' },
    { 'id': 11, 'title': 'Shaked 11', 'price': 2480000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=2' },
    { 'id': 12, 'title': 'Oren 12', 'price': 2130000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=7' },
    { 'id': 13, 'title': 'Shaked 13', 'price': 1410000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=8' },
    { 'id': 14, 'title': 'Oren 14', 'price': 2810000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=4' },
    { 'id': 15, 'title': 'Shaked 15', 'price': 1470000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=1' },
    { 'id': 16, 'title': 'Oren 16', 'price': 2530000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=10' },
    { 'id': 17, 'title': 'Shaked 17', 'price': 2010000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=5' },
    { 'id': 18, 'title': 'Oren 18', 'price': 2710000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=2' },
    { 'id': 19, 'title': 'Shaked 19', 'price': 1130000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=8' },
    { 'id': 20, 'title': 'Oren 20', 'price': 1850000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=4' },
    { 'id': 21, 'title': 'Shaked 21', 'price': 2200000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=1' },
    { 'id': 22, 'title': 'Oren 22', 'price': 2140000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=3' },
    { 'id': 23, 'title': 'Shaked 23', 'price': 2570000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=7' },
    { 'id': 24, 'title': 'Oren 24', 'price': 1650000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=9' },
    { 'id': 25, 'title': 'Shaked 25', 'price': 1350000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=10' },
    { 'id': 26, 'title': 'Oren 26', 'price': 1990000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=4' },
    { 'id': 27, 'title': 'Shaked 27', 'price': 2100000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=1' },
    { 'id': 28, 'title': 'Oren 28', 'price': 1900000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=8' },
    { 'id': 29, 'title': 'Shaked 29', 'price': 2260000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=7' },
    { 'id': 30, 'title': 'Oren 30', 'price': 1150000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=9' },
    { 'id': 31, 'title': 'Shaked 31', 'price': 1040000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=2' },
    { 'id': 32, 'title': 'Oren 32', 'price': 2230000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=6' },
    { 'id': 33, 'title': 'Shaked 33', 'price': 2050000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=3' },
    { 'id': 34, 'title': 'Oren 34', 'price': 1550000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=5' },
    { 'id': 35, 'title': 'Shaked 35', 'price': 2640000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=8' },
    { 'id': 36, 'title': 'Oren 36', 'price': 2170000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=10' },
    { 'id': 37, 'title': 'Shaked 37', 'price': 1620000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=2' },
    { 'id': 38, 'title': 'Oren 38', 'price': 1430000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=1' },
    { 'id': 39, 'title': 'Shaked 39', 'price': 2940000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=9' },
    { 'id': 40, 'title': 'Oren 40', 'price': 1680000,'link': 'https://www.yad2.co.il/realestate/item/33biz3x3?opened-from=feed&component-type=main_feed&spot=standard&location=1', 'url_image': 'https://img.yad2.co.il/Pic/202312/17/2_5/o/y2_1pa_010968_20231217131916.jpeg?c=4' }
]

clientsList = [
    { 'id': 1,'clientID': 10001, 'nickname': 'Reuben ', 'userID': "1001", 'minPrice': 1500000,'maxPrice': 2000000, 'minRoom': 4,'maxRoom': 5 },
    { 'id': 2,'clientID': 10002, 'nickname': 'Simeon ', 'userID': "1002",'minPrice': 1950000,'maxPrice': 2200000, 'minRoom': 5,'maxRoom': 6 },
    { 'id': 3,'clientID': 10003, 'nickname': 'Levi ', 'userID': "1001", 'minPrice': 1400000,'maxPrice': 2000000, 'minRoom': 3,'maxRoom': 3 },
    { 'id': 4,'clientID': 10004, 'nickname': 'Judah  ', 'userID': "1002",'minPrice': 1500000,'maxPrice': 1700000, 'minRoom': 4,'maxRoom': 6 },
    { 'id': 5,'clientID': 10005, 'nickname': 'Dan ', 'userID': "1001", 'minPrice': 1750000,'maxPrice': 1950000, 'minRoom': 5,'maxRoom': 5 },
    { 'id': 6,'clientID': 10006, 'nickname': 'Naphtali  ', 'userID': "1002",'minPrice': 1800000,'maxPrice': 2000000, 'minRoom': 6,'maxRoom': 6 },
    { 'id': 7,'clientID': 10007, 'nickname': 'Gad ', 'userID': "1001", 'minPrice': 1100000,'maxPrice': 1300000, 'minRoom': 3,'maxRoom': 4 },
    { 'id': 8,'clientID': 10008, 'nickname': 'Asher ', 'userID': "1002",'minPrice': 1000000,'maxPrice': 1100000, 'minRoom': 4,'maxRoom': 4 },
    { 'id': 9,'clientID': 10009, 'nickname': 'Issachar  ', 'userID': "1001", 'minPrice': 2600000,'maxPrice': 3000000, 'minRoom': 5,'maxRoom': 5 },
    { 'id': 10,'clientID': 10010, 'nickname': 'Zebulun  ', 'userID': "1002",'minPrice': 2350000,'maxPrice': 2800000, 'minRoom': 5,'maxRoom': 6 },
    { 'id': 11,'clientID': 10011, 'nickname': 'Joseph  ', 'userID': "1001", 'minPrice': 2000000,'maxPrice': 2200000, 'minRoom': 4,'maxRoom': 4 },
    { 'id': 12,'clientID': 10012, 'nickname': 'Benjamin ', 'userID': "1002",'minPrice': 1920000,'maxPrice': 2050000, 'minRoom': 5,'maxRoom': 5 }
  ]  

clientsSearch = [
    { 
        'id': 1,
        'clientID': 10001,
        'nickname': 'Reuben',
        'userID': "1001",
        'minPrice': 1500000,
        'maxPrice': 2000000,
        'minRoom': 4,
        'maxRoom': 5,
        'resultId1':1,
        'resultId2':2,
        'resultId3':3,
        'Neighborhood':'Hahoresh' ,
    },
    {   
        'id': 2,
        'clientID': 10002,
        'nickname': 'Simeon',
        'userID': "1002",
        'minPrice': 1950000,
        'maxPrice': 2200000,
        'minRoom': 5,
        'maxRoom': 6,
        'resultId1':1,
        'resultId2':2,
        'resultId3':3,
        'Neighborhood': 'Hahoresh', 
    },
    {   
        'id': 3,
        'clientID': 10003,
        'nickname': 'Levi',
        'userID': "1001",
        'minPrice': 1400000,
        'maxPrice': 2000000,
        'minRoom': 3,
        'maxRoom': 3,
        'resultId1':1,
        'resultId2':2,
        'resultId3':3,
        'Neighborhood': 'Hahoresh',
    },
    {   
        'id': 4,
        'clientID': 10004,
        'nickname': 'Judah',
        'userID': "1002",
        'minPrice': 1500000,
        'maxPrice': 1700000,
        'minRoom': 4,
        'maxRoom': 6,
        'resultId1':1,
        'resultId2':2,
        'resultId3':3,
        'Neighborhood':'Hahoresh' , 
    },
    { 
        'id': 5,
        'clientID': 10005,
        'nickname': 'Dan',
        'userID': "1001",
        'minPrice': 1750000,
        'maxPrice': 1950000,
        'minRoom': 5,
        'maxRoom': 5,
        'resultId1':1,
        'resultId2':2,
        'resultId3':3,
        'Neighborhood': 'Avnei-Chen', 
    },
    {   
        'id': 6,
        'clientID': 10006,
        'nickname': 'Naphtali',
        'userID': "1002",
        'minPrice': 1800000,
        'maxPrice': 2000000,
        'minRoom': 6,
        'maxRoom': 6,
        'resultId1':1,
        'resultId2':2,
        'resultId3':3,
        'Neighborhood': 'Avnei-Chen', 
    },
    {   
        'id': 7,
        'clientID': 10007,
        'nickname': 'Gad',
        'userID': "1001",
        'minPrice': 1100000,
        'maxPrice': 1300000,
        'minRoom': 3,
        'maxRoom': 4,
        'resultId1':1,
        'resultId2':2,
        'resultId3':3,
        'Neighborhood': 'Avnei-Chen',
    },
    { 
        'id': 8,
        'clientID': 10008,
        'nickname': 'Asher',
        'userID': "1002",
        'minPrice': 1000000,
        'maxPrice': 1100000,
        'minRoom': 4,
        'maxRoom': 4,
        'resultId1':1,
        'resultId2':2,
        'resultId3':3,
        'Neighborhood':'Avnei-Chen' ,
    },
    {   
        'id': 9,
        'clientID': 10009,
        'nickname': 'Issachar',
        'userID': "1001",
        'minPrice': 2600000,
        'maxPrice': 3000000,
        'minRoom': 5,
        'maxRoom': 5,
        'resultId1':1,
        'resultId2':2,
        'resultId3':3,
        'Neighborhood': 'Haprachim', 
    },
    {   
        'id': 10,
        'clientID': 10010,
        'nickname': 'Zebulun',
        'userID': "1002",
        'minPrice': 2350000,
        'maxPrice': 2800000,
        'minRoom': 5,
        'maxRoom': 6,
        'resultId1':1,
        'resultId2':2,
        'resultId3':3,
        'Neighborhood': 'Haprachim', 
          },
    {   
        'id': 11,
        'clientID': 10011,
        'nickname': 'Joseph  ',
        'userID': "1001", 
        'minPrice': 2000000,
        'maxPrice': 2200000,
        'minRoom': 4,
        'maxRoom': 4,
        'resultId1':1,
        'resultId2':2,
        'resultId3':3,
        'Neighborhood':'Haprachim', 
    },
    {   
        'id': 12,
        'clientID': 10012,
        'nickname': 'Benjamin ',
        'userID': "1002",
        'minPrice': 1920000,
        'maxPrice': 2050000,
        'minRoom': 5,
        'maxRoom': 5,
        'resultId1':1,
        'resultId2':2,
        'resultId3':3,
        'Neighborhood': 'Haprachim' , 
    },
    { 
        'id': 13,
        'clientID': 10001,
        'nickname': 'Reuben',
        'userID': "1001",
        'minPrice': 1600000,
        'maxPrice': 2100000,
        'minRoom': 3,
        'maxRoom': 3,
        'resultId1':1,
        'resultId1':2,
        'resultId1':3,
        'resultId1':1,
        'resultId2':2,
        'resultId3':3,
        'Neighborhood':'Hahoresh' ,
    },
    {   
        'id': 14,
        'clientID': 10002,
        'nickname': 'Simeon',
        'userID': "1002",
        'minPrice': 1850000,
        'maxPrice': 2200000,
        'minRoom': 4,
        'maxRoom': 4,
        'resultId1':1,
        'resultId2':2,
        'resultId3':3,
        'Neighborhood': 'Hahoresh', 
    },
    {   
        'id': 15,
        'clientID': 10003,
        'nickname': 'Levi',
        'userID': "1001",
        'minPrice': 1400000,
        'maxPrice': 2100000,
        'minRoom': 4,
        'maxRoom': 5,
        'resultId1':1,
        'resultId2':2,
        'resultId3':3,
        'Neighborhood': 'Hahoresh',
    },
    {   
        'id': 16,
        'clientID': 10004,
        'nickname': 'Judah',
        'userID': "1002",
        'minPrice': 1600000,
        'maxPrice': 1800000,
        'minRoom': 5,
        'maxRoom': 6,
        'resultId1':1,
        'resultId2':2,
        'resultId3':3,
        'Neighborhood':'Hahoresh' , 
    },
    { 
        'id': 17,
        'clientID': 10005,
        'nickname': 'Dan',
        'userID': "1001",
        'minPrice': 1750000,
        'maxPrice': 1950000,
        'minRoom': 6,
        'maxRoom': 6,
        'resultId1':1,
        'resultId2':2,
        'resultId3':3,
        'Neighborhood': 'Avnei-Chen', 
    },
    {   
        'id': 18,
        'clientID': 10006,
        'nickname': 'Naphtali',
        'userID': "1002",
        'minPrice': 1800000,
        'maxPrice': 2000000,
        'minRoom': 5,
        'maxRoom': 5,
        'resultId1':1,
        'resultId2':2,
        'resultId3':3,
        'Neighborhood': 'Avnei-Chen', 
    },
    {   
        'id': 19,
        'clientID': 10007,
        'nickname': 'Gad',
        'userID': "1001",
        'minPrice': 1200000,
        'maxPrice': 1400000,
        'minRoom': 4,
        'maxRoom': 4,
        'resultId1':1,
        'resultId2':2,
        'resultId3':3,
        'Neighborhood': 'Avnei-Chen',
    },
    { 
        'id': 20,
        'clientID': 10008,
        'nickname': 'Asher',
        'userID': "1002",
        'minPrice': 1100000,
        'maxPrice': 1200000,
        'minRoom': 4,
        'maxRoom': 5,
        'resultId1':1,
        'resultId2':2,
        'resultId3':3,
        'Neighborhood':'Avnei-Chen' ,
    },
    {   
        'id': 21,
        'clientID': 10009,
        'nickname': 'Issachar',
        'userID': "1001",
        'minPrice': 2400000,
        'maxPrice': 3000000,
        'minRoom': 4,
        'maxRoom': 5,
        'resultId1':1,
        'resultId2':2,
        'resultId3':3,
        'Neighborhood': 'Haprachim', 
    },
    {   
        'id': 22,
        'clientID': 10010,
        'nickname': 'Zebulun',
        'userID': "1002",
        'minPrice': 2350000,
        'maxPrice': 2800000,
        'minRoom': 4,
        'maxRoom': 4,
        'resultId1':1,
        'resultId2':2,
        'resultId3':3,
        'Neighborhood': 'Haprachim', 
          },
    {   
        'id': 23,
        'clientID': 10011,
        'nickname': 'Joseph  ',
        'userID': "1001", 
        'minPrice': 2100000,
        'maxPrice': 2300000,
        'minRoom': 5,
        'maxRoom': 5,
        'resultId1':1,
        'resultId2':2,
        'resultId3':3,
        'Neighborhood':'Haprachim', 
    },
    {   
        'id': 24,
        'clientID': 10012,
        'nickname': 'Benjamin ',
        'userID': "1002",
        'minPrice': 1820000,
        'maxPrice': 2050000,
        'minRoom': 4,
        'maxRoom': 5,
        'resultId1':1,
        'resultId2':2,
        'resultId3':3,
        'Neighborhood': 'Haprachim' , 
    }

  ] 

cities = ['New York', 'Los Angeles', 'Chicago']

@app.route("/auth/login", methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username in usersAuth and usersAuth[username]['password'] == password:
        return jsonify({"userID": usersAuth[username]['userID'], "nickname": usersAuth[username]['nickname']})
    else:
        return jsonify({"message": "Invalid username or password"}), 401



@app.route("/api/users", methods=['GET'])
def users():
    return jsonify({"users": userList})
    

# Route to get a user by index
@app.route("/api/users/<int:index>", methods=['GET'])
def get_user_by_index(index):
    try:
        user = userList[index]
        return jsonify({"user": user})
    except IndexError:
        return jsonify({"error": "User not found"}), 404
    
# Route to get a user by index
@app.route("/api/clientsList", methods=['GET'])
def get_client():
    return jsonify({"client": clientsList})

# Route to get users by userID
@app.route("/api/clientsList/<int:userID>", methods=['GET'])
def get_clients_by_userID(userID):
    user_clients = [client for client in clientsList if client['userID'] == str(userID)]
    if user_clients:
        return jsonify({"clients": user_clients})
    else:
        return jsonify({"error": "Clients not found for the given userID"}), 404



# @app.route("/api/clientdetails/<int:clientID>", methods=['GET'])
# def get_clientdetails_by_userID(clientID):
#     user_clients = [client for client in clientsSearch if client['clientID'] == clientID]
#     if user_clients:
#         return jsonify({"clientsSearch": user_clients})
#     else:
#         return jsonify({"error": "Clients not found for the given clientID"}), 404

def get_results_for_client(client, user_list):
    results = []
    for result_id in ['resultId1', 'resultId2', 'resultId3']:
        result = next((item for item in user_list if item['id'] == client[result_id]), None)
        if result:
            results.append(result)
    return results

@app.route("/api/clientdetails/<int:clientID>", methods=['GET'])
def get_clientdetails_by_userID(clientID):
    user_clients = [client for client in clientsSearch if client['clientID'] == clientID]
    if not user_clients:
        return jsonify({"error": "Clients not found for the given clientID"}), 404
    
    for client in user_clients:
        client['results'] = get_results_for_client(client, userList)

    return jsonify({"clientsSearch": user_clients})




@app.route("/api/neighborhood", methods=['GET'])
def neighborhood():
    return jsonify(
        {
            "neighborhood": [
                'אבני חן',
                'החורש',
                'הפרחים',
                'בצוותא',
                'המע"ר'
            ]
        } 
    )



# Route to get user or city by index
@app.route("/api/data", methods=['GET'])
def get_data_by_index():
    data_type = request.args.get('type')
    index = int(request.args.get('index', 0))  # Default to 0 if not provided

    if data_type == 'user':
        try:
            return jsonify({"user": userList[index]})
        except IndexError:
            return jsonify({"error": "User not found"}), 404
    elif data_type == 'city':
        try:
            return jsonify({"city": cities[index]})
        except IndexError:
            return jsonify({"error": "City not found"}), 404
    else:
        return jsonify({"error": "Invalid type"}), 400
    
if __name__ == "__main__":
    app.run(debug=True, port=8080)
