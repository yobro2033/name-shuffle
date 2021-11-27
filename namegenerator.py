import os

import random

import json

vowels = ["a", "e", "i", "o", "u"]

def jigName(name, limit):
    theList = []
    for mode in [1, 2]:
        parts = name.split(" ")
        if mode == 1:
            part = parts[0]
            mode = "fName"
        else:
            part = parts[1]
            mode = "lName"
        for index in range(0, len(part)):
            char = part[index]
            if char != "-" and char.lower() in vowels:
                count = 0
                jiggedPart = ""
                for eachChar in part:
                    if count == index:
                        jiggedPart += char
                    jiggedPart += eachChar
                    count += 1
                if mode == "fName":
                    finalJigged = f"{jiggedPart.capitalize()} {parts[1].capitalize()}"
                else:
                    finalJigged = f"{parts[0].capitalize()} {jiggedPart.capitalize()}"
                theList.append(finalJigged)
    theList = random.sample(theList, len(theList))
    finalList = []
    for x in theList:
        if len(finalList) == limit:
            break
        finalList.append(x)
    return finalList

os.system("cls")

names = ["Thi-Kieu-Trang Nguyen", "Ha-Phuong-Anh Vuong", "Kieu-Thi-Trang Nguyen", "Phuong-Ha-Anh Vuong", "Thi-Trang-Kieu Nguyen", "Ha-Anh-Phuong Vuong", "Trang-Thi-Kieu Nguyen", "Anh-Ha-Phuong Vuong", "Kieu-Trang-Thi Nguyen", "Phuong-Anh-Ha Vuong", "Trang-Kieu-Thi Nguyen", "Anh-Phuong-Ha Vuong", "Thi-Kieu-Nguyen Trang", "Ha-Phuong-Vuong Anh", "Kieu-Thi-Nguyen Trang", "Phuong-Ha-Vuong Anh", "Thi-Trang-Nguyen Kieu", "Ha-Anh-Vuong Phuong", "Trang-Thi-Nguyen Kieu", "Anh-Ha-Vuong Phuong", "Kieu-Trang-Nguyen Thi", "Phuong-Anh-Vuong Ha", "Trang-Kieu-Nguyen Thi", "Anh-Phuong-Vuong Ha", "Thi-Nguyen-Kieu Trang", "Ha-Vuong-Phuong Anh", "Kieu-Nguyen-Thi Trang", "Phuong-Vuong-Ha Anh", "Thi-Nguyen-Trang Kieu", "Ha-Vuong-Anh Phuong", "Trang-Nguyen-Thi Kieu", "Anh-Vuong-Ha Phuong", "Kieu-Nguyen-Trang Thi", "Phuong-Vuong-Anh Ha", "Trang-Nguyen-Kieu Thi", "Anh-Vuong-Phuong Ha", "Nguyen-Thi-Kieu Trang", "Vuong-Ha-Phuong Anh", "Nguyen-Kieu-Thi Trang", "Vuong-Phuong-Ha Anh", "Nguyen-Thi-Trang Kieu", "Vuong-Ha-Anh Phuong", "Nguyen-Trang-Thi Kieu", "Vuong-Anh-Ha Phuong", "Nguyen-Kieu-Trang Thi", "Vuong-Phuong-Anh Ha", "Nguyen-Trang-Kieu Thi", "Vuong-Anh-Phuong Ha", "Kieu-Trang Nguyen", "Phuong-Anh Vuong", "Thi-Trang Nguyen", "Ha-Anh Vuong", "Trang-Kieu Nguyen", "Anh-Phuong Vuong", "Thi-Kieu Nguyen", "Ha-Phuong Vuong", "Trang-Thi Nguyen", "Anh-Ha Vuong", "Kieu-Thi Nguyen", "Phuong-Ha Vuong", "Trang-Nguyen Thi", "Anh-Vuong Ha", "Trang-Nguyen Kieu", "Anh-Vuong Phuong", "Kieu-Nguyen Thi", "Phuong-Vuong Ha", "Kieu-Nguyen Trang", "Phuong-Vuong Anh", "Thi-Nguyen Kieu", "Ha-Vuong Phuong", "Thi-Nguyen Trang", "Ha-Vuong Anh", "Nguyen-Trang Thi", "Vuong-Anh Ha", "Nguyen-Trang Kieu", "Vuong-Anh Phuong", "Nguyen-Kieu Thi", "Vuong-Phuong Ha", "Nguyen-Kieu Trang", "Vuong-Phuong Anh", "Nguyen-Thi Kieu", "Vuong-Ha Phuong", "Nguyen-Thi Trang", "Vuong-Ha Anh", "Thi Nguyen", "Ha Vuong", "Kieu Nguyen", "Phuong Vuong", "Trang Nguyen", "Anh Vuong", "Nguyen Thi", "Vuong Ha", "Nguyen Kieu", "Vuong Phuong", "Nguyen Trang", "Vuong Anh", "Dieu-Minh Bui", "Ky-Duyen Cao", "Vu-Hoang Dang", "Thai-Hoang Dang", "Anh-Tuan Hoang", "Ryan-tej kamdar", "Louis-Anthony Kennedy", "Leonardo-Nima Khamnei", "Duy-Khanh Le", "Tu-Trong Luu", "Ngoc-Uyen Ly", "Phuong-Trang Mai", "Nadeem-Ahmed Mukri", "Thao-Ngan Ngo", "Hoang-Dung Nguyen", "Simon-Rio nzewi", "Minh-Ngoc Pham", "Cem-Sultan Ratip", "Daniel-George Schofield", "Rudi-Joseph Thompson", "Huong-Giang Tran", "Kha-Phuc Vuong", "Thanh-Nam Vuong", "Jonathan-Wakigathi Wanyanga", "Rafe-hugh Williams", "Dannera-Benitta Wynter", "Minh-Dieu Bui", "Duyen-Ky Cao", "Hoang-Vu Dang", "Hoang-Thai Dang", "Tuan-Anh Hoang", "tej-Ryan kamdar", "Anthony-Louis Kennedy", "Nima-Leonardo Khamnei", "Khanh-Duy Le", "Trong-Tu Luu", "Uyen-Ngoc Ly", "Trang-Phuong Mai", "Ahmed-Nadeem Mukri", "Ngan-Thao Ngo", "Dung-Hoang Nguyen", "Rio-Simon nzewi", "Ngoc-Minh Pham", "Sultan-Cem Ratip", "George-Daniel Schofield", "Joseph-Rudi Thompson", "Giang-Huong Tran", "Phuc-Kha Vuong", "Nam-Thanh Vuong", "Wakigathi-Jonathan Wanyanga", "hugh-Rafe Williams", "Benitta-Dannera Wynter", "Dieu-Bui Minh", "Ky-Cao Duyen", "Vu-Dang Hoang", "Thai-Dang Hoang", "Anh-Hoang Tuan", "Ryan-kamdar tej", "Louis-Kennedy Anthony", "Leonardo-Khamnei Nima", "Duy-Le Khanh", "Tu-Luu Trong", "Ngoc-Ly Uyen", "Phuong-Mai Trang", "Nadeem-Mukri Ahmed", "Thao-Ngo Ngan", "Hoang-Nguyen Dung", "Simon-nzewi Rio", "Minh-Pham Ngoc", "Cem-Ratip Sultan", "Daniel-Schofield George", "Rudi-Thompson Joseph", "Huong-Tran Giang", "Kha-Vuong Phuc", "Thanh-Vuong Nam", "Jonathan-Wanyanga Wakigathi", "Rafe-Williams hugh", "Dannera-Wynter Benitta", "Minh-Bui Dieu", "Duyen-Cao Ky", "Hoang-Dang Vu", "Hoang-Dang Thai", "Tuan-Hoang Anh", "tej-kamdar Ryan", "Anthony-Kennedy Louis", "Nima-Khamnei Leonardo", "Khanh-Le Duy", "Trong-Luu Tu", "Uyen-Ly Ngoc", "Trang-Mai Phuong", "Ahmed-Mukri Nadeem", "Ngan-Ngo Thao", "Dung-Nguyen Hoang", "Rio-nzewi Simon", "Ngoc-Pham Minh", "Sultan-Ratip Cem", "George-Schofield Daniel", "Joseph-Thompson Rudi", "Giang-Tran Huong", "Phuc-Vuong Kha", "Nam-Vuong Thanh", "Wakigathi-Wanyanga Jonathan", "hugh-Williams Rafe", "Benitta-Wynter Dannera", "Bui-Dieu Minh", "Cao-Ky Duyen", "Dang-Vu Hoang", "Dang-Thai Hoang", "Hoang-Anh Tuan", "kamdar-Ryan tej", "Kennedy-Louis Anthony", "Khamnei-Leonardo Nima", "Le-Duy Khanh", "Luu-Tu Trong", "Ly-Ngoc Uyen", "Mai-Phuong Trang", "Mukri-Nadeem Ahmed", "Ngo-Thao Ngan", "Nguyen-Hoang Dung", "nzewi-Simon Rio", "Pham-Minh Ngoc", "Ratip-Cem Sultan", "Schofield-Daniel George", "Thompson-Rudi Joseph", "Tran-Huong Giang", "Vuong-Kha Phuc", "Vuong-Thanh Nam", "Wanyanga-Jonathan Wakigathi", "Williams-Rafe hugh", "Wynter-Dannera Benitta", "Bui-Minh Dieu", "Cao-Duyen Ky", "Dang-Hoang Vu", "Dang-Hoang Thai", "Hoang-Tuan Anh", "kamdar-tej Ryan", "Kennedy-Anthony Louis", "Khamnei-Nima Leonardo", "Le-Khanh Duy", "Luu-Trong Tu", "Ly-Uyen Ngoc", "Mai-Trang Phuong", "Mukri-Ahmed Nadeem", "Ngo-Ngan Thao", "Nguyen-Dung Hoang", "nzewi-Rio Simon", "Pham-Ngoc Minh", "Ratip-Sultan Cem", "Schofield-George Daniel", "Thompson-Joseph Rudi", "Tran-Giang Huong", "Vuong-Phuc Kha", "Vuong-Nam Thanh", "Wanyanga-Wakigathi Jonathan", "Williams-hugh Rafe", "Wynter-Benitta Dannera", "Minh Bui", "Duyen Cao", "Hoang Dang", "Tuan Hoang", "tej kamdar", "Anthony Kennedy", "Nima Khamnei", "Khanh Le", "Trong Luu", "Uyen Ly", "Trang Mai", "Ahmed Mukri", "Ngan Ngo", "Dung Nguyen", "Rio nzewi", "Ngoc Pham", "Sultan Ratip", "George Schofield", "Joseph Thompson", "Giang Tran", "Phuc Vuong", "Nam Vuong", "Wakigathi Wanyanga", "hugh Williams", "Benitta Wynter", "Bui Minh", "Cao Duyen", "Dang Hoang", "Hoang Tuan", "kamdar tej", "Kennedy Anthony", "Khamnei Nima", "Le Khanh", "Luu Trong", "Ly Uyen", "Mai Trang", "Mukri Ahmed", "Ngo Ngan", "Nguyen Dung", "nzewi Rio", "Pham Ngoc", "Ratip Sultan", "Schofield George", "Thompson Joseph", "Tran Giang", "Vuong Phuc", "Vuong Nam", "Wanyanga Wakigathi", "Williams hugh", "Wynter Benitta", "Dieu Bui", "Ky Cao", "Vu Dang", "Thai Dang", "Anh Hoang", "Ryan kamdar", "Louis Kennedy", "Leonardo Khamnei", "Duy Le", "Tu Luu", "Ngoc Ly", "Phuong Mai", "Nadeem Mukri", "Thao Ngo", "Hoang Nguyen", "Simon nzewi", "Minh Pham", "Cem Ratip", "Daniel Schofield", "Rudi Thompson", "Huong Tran", "Kha Vuong", "Thanh Vuong", "Jonathan Wanyanga", "Rafe Williams", "Dannera Wynter", "Bui Dieu", "Cao Ky", "Dang Vu", "Dang Thai", "Hoang Anh", "kamdar Ryan", "Kennedy Louis", "Khamnei Leonardo", "Le Duy", "Luu Tu", "Ly Ngoc", "Mai Phuong", "Mukri Nadeem", "Ngo Thao", "Nguyen Hoang", "nzewi Simon", "Pham Minh", "Ratip Cem", "Schofield Daniel", "Thompson Rudi", "Tran Huong", "Vuong Kha", "Vuong Thanh", "Wanyanga Jonathan", "Williams Rafe", "Wynter Dannera"]
lists = []

for x in names:
    aList = jigName(x, 10000)
    finalList = []
    for eachName in aList:
        finalList.append(eachName)
    lists.append(finalList)

nameList = []

for each in lists:
    for name in each:
        nameList.append(name
            )

with open('offspring_data.txt', 'w') as outfile:
    json.dump(nameList, outfile)
print(nameList)

input()