import requests,json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

api_key = "7f65701f025236c354d7754c5a4e0b71"
def credits():
    cred=Toplevel()
    cred.geometry('300x170')
    cred.title('programmer')

    Label(cred,text='Created By:KYLE PHILLIPS').grid(row=2,column=2)
    Label(cred,text='LETS GOO!!!').grid(row=3,column=2)
def proceed():
    city=cit.get()
    if city=='':
        return messagebox.showerror('Error','Enter City Name')
    elif api_key=='':
        return messagebox.showerror('Error','Enter your api key')

    else:
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        cityname = city
        complete_url = base_url + "appid=" + api_key + "&q=" + cityname
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":

            y = x["main"]
            currenttemp = y["temp"]
            currentpressure = y["pressure"]
            currenthumidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            Label(window,text='Temperature: '+str(round(currenttemp-272.15))+' degree celsius').place(x=2,y=90)
            Label(window,text='Atmospheric Pressure: '+str(currentpressure)+' hPa').place(x=2,y=120)
            Label(window,text='Humidity: '+str(currenthumidiy)).place(x=2,y=150)
            Label(window,text='Description: '+str(weather_description)).place(x=2,y=180)
            window.configure(background="yellow")
        else:
            return messagebox.showerror('Error','No City Found')


window=Tk()
window.geometry('400x400')
window.title('Weather')
window.configure(background="powderblue")
window.configure(background="blue")

cit=StringVar()
Label(window,text='Weather',font='Helvetica 12 bold').grid(row=1,column=3)
Button(window,text='Credits',command=credits).grid(row=1,column=4)
Label(window,text='Enter City:').grid(row=2,column=1)
Entry(window,width=15,textvariable=cit).grid(row=2,column=2)
Button(window,text='Proceed',command=proceed).grid(row=3,column=3)


window.mainloop()
