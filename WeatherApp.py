from imports import *

def window():


     def send():
          # function that convert kelvin degrees (that what we get from the API) to celsius
          def fahr_to_cel(kelvin):
               celsius = kelvin - 273.15
               celsius = int(celsius)
               return celsius
          # set global var for using out of the scope
          global celsiuslabel
          global feelslabel
          global templabel
          global celsius_feel_like
          global aklimlabel
          global aklimstatus
          global localtimelabel
          global localtime
          global sunriselabel
          global sunrisetime
          global setriselabel
          global setrisetime
          global countrylabel
          
          # Try and except the get methods for the API request
          try:
               base_url = "http://api.openweathermap.org/data/2.5/weather?"
               key = 'a248ebd59999429b4fdfb9320e8feecb'
               city = entry.get()
               url = base_url + "appid=" + key + "&q=" + city
               response = requests.get(url).json()

               kelvin = response['main']['temp']
               feels_like = response['main']['feels_like']
               aklim = response['weather'][0]['description']
               
               local_time = response['dt']
               local_conv = datetime.datetime.fromtimestamp(local_time)
               
               sun_time = response['sys']['sunrise']
               date_conv = datetime.datetime.fromtimestamp(sun_time)

               set_time = response['sys']['sunset']
               set_conv = datetime.datetime.fromtimestamp(set_time)

               country = response['sys']['country']

               tempstatus = fahr_to_cel(kelvin)
               feels_like_temp = fahr_to_cel(feels_like)
               
               entry.delete(0, END)
               # Labels of the API for showing the result
               templabel = ttk.Label(root, text=(f'Temperature in {city}:'), background='black',foreground='white', font='15')
               feelslabel = ttk.Label(root, text=(f'Temperature in {city} feels like:'), background='black',foreground='white', font='15')
               celsiuslabel = Label(root,text=f'{tempstatus}°C', font='30', foreground='yellow', background='black')
               celsius_feel_like = Label(root, text=f'{feels_like_temp}°C', font='30', foreground='yellow', background='black')
               aklimstatus = ttk.Label(root, text=(f'Sky status in {city}:'), background='black',foreground='white', font='15')
               aklimlabel = Label(root,text=aklim, font='30', foreground='yellow', background='black')
               localtimelabel = ttk.Label(root, text=(f'Local Time in {city}:'), background='black',foreground='white', font='15')
               localtime = Label(root, text=local_conv, font='30', foreground='yellow', background='black')
               sunriselabel = Label(root, text=(f'Sunrise Time in {city}:'), background='black',foreground='white', font='15')
               sunrisetime = Label(root, text=date_conv, font='30', foreground='yellow', background='black')
               setriselabel = Label(root, text=(f'Sunset Time in {city}:'), background='black',foreground='white', font='15')
               setrisetime = Label(root, text=set_conv, font='30', foreground='yellow', background='black')
               countrylabel = Label(root, text=(country), background='black',foreground='white', font='15')

               templabel.place(x=0,y=15)
               celsiuslabel.place(x=250,y=15)
               feelslabel.place(x=0,y=45)
               celsius_feel_like.place(x=335,y=45)
               aklimlabel.place(x=245, y=75)
               aklimstatus.place(x=0, y=75)
               localtimelabel.place(x=0, y=105)
               localtime.place(x=245, y=105)
               sunriselabel.place(x=0, y=135)
               sunrisetime.place(x=245, y=135)
               setriselabel.place(x=0, y=165)
               setrisetime.place(x=245, y=165)
               countrylabel.place(x=400, y=0)
               
               mainlabel.destroy()
               mainlabel1.destroy()
          # catch the error key "KeyError" and response accordingly
               
          except KeyError:
               print('You Enter Wrong City Name, Please Try Again!')
               messagebox.showerror('Error','You Enter Wrong City Name, Please Try Again!')
               entry.delete(0, END)


     # Clear function that delete the labels
     def clear():
          global mainlabel1

          label_to_destroy = [celsiuslabel, feelslabel, templabel, celsius_feel_like, 
          aklimlabel, aklimstatus, localtime, localtimelabel, sunriselabel, 
          sunrisetime, setriselabel, setrisetime, countrylabel]
          
          for i in label_to_destroy:
               i.destroy()

          mainlabel1 = Label(root, text=f'''Hello {os.getlogin()}, 
Enter City Name And Click "Send" To Get 
The Weather Information of Your City!
Dont Forget To Clear The Screen By 
Clicking The "Clear" at the end of The Result!''', background='black', foreground='white', font=15)
          mainlabel1.place(x=50, y=30)

     def about():
          messagebox.showinfo('About', 'This app created by Maor Sasson')

     # Class buttons that create button and using the addbutton() function to add the button to the App window
     class Buttons():
          def __init__(self, name, comm):
               self.name = name
               self.comm = comm
               self.button = ttk.Button(root, text=self.name, command=self.comm)                 
          def addbutton(self, x, y, width):
               self.button.place(x=x, y=y, width=width)
     
     # Create the windows using the tkinter libary
     root = Tk()
     root.title('Weather Application')
     root.iconbitmap('WeatherApp - API\icon.ico')
     root.geometry('500x300')
     root.resizable(False, False)

     # Create canvas for background of the App
     imagepath = "WeatherApp - API\\bg2.jpg"
     img = Image.open(imagepath)
     photo = ImageTk.PhotoImage(img)
     canvas = tk.Canvas(root, bd=0, highlightthickness=0)
     canvas.place(x=0, y=0, width=5000, height=5000)
     canvas.create_image(250, 150, image=photo)
     messagebox.showinfo('Welcome!', f'Hello {os.getlogin()}, With This Application You Can Able To Know What The Weather at Every City In The World With Easy Action!')
     
     # Add buttons Using the class Buttons and the addbutton() func
     sendbutton = Buttons("Send", send)
     sendbutton.addbutton(0, 260, 50)

     clearbutton = Buttons("Clear", clear)
     clearbutton.addbutton(50, 260, 50)

     aboutebutton = Buttons("about", about)
     aboutebutton.addbutton(100, 260, 50)

     # Create and add Entry for the App
     entry = Entry(root, width=10)
     entrylabel = Label(root, text='Enter City Name:', background='black', foreground='White')
     entry.place(x=0, y=230)
     entrylabel.place(x=0, y=200)

     mainlabel = Label(root, text=f'''Hello {os.getlogin()}, 
Enter City Name And Click "Send" To Get 
The Weather Information of Your City!
Dont Forget To Clear The Screen By 
Clicking The "Clear" at the end of The Result!''', background='black', foreground='white', font=15)
     
     mainlabel.place(x=50, y=30)
     # the mainloop methods cause that the app windows not crash
     root.mainloop()

if __name__ == '__main__':
     window()



