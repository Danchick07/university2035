from tkinter import *# import tkinterwindow = Tk()window.geometry('800x600')canvas = Canvas(window, width=800, height=600, bg='white') #Холст создалиcanvas.pack() #Поставили холст на мальберт# canvas.create_rectangle(100,100,350,350,fill='black', outline='')# canvas.create_rectangle(120, 120, 140, 140,fill='red', outline='')# canvas.create_rectangle(150, 150, 190, 190,fill='blue', outline='')# canvas.create_rectangle(200, 200, 260, 260,fill='green', outline='')## canvas.create_polygon(10, 50, 50, 10, 90, 50, fill='yellow', outline='')canvas.create_polygon(10, 260, 60, 200, 110, 260, fill='green', outline='black')canvas.create_rectangle(20, 260, 100, 360, fill='red', outline='black')window.mainloop()# import requests## url = 'https://swapi.dev/api/' # Сайт со звёздными войнами.## response = requests.get(url).json()## # print(response['people'])## people_api = response['people'] # Ссылка на БД с персонажами## # Вывод информации о 5 персонажах# # 'https://swapi.dev/api/people/1'# def check_people(url):#     for i in range(1, 6):#         response = requests.get(url + str(i)).json()#         print(response['name'], response['height'])#### # print(people_api)# # print(people_api['results'])# # print(people_api['results'][0])# # print(people_api['results'][0]['name'])