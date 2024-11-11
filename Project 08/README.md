# Weather App Guide using Tkinter and OpenWeatherMap API

This guide will help you create a weather application using Python's Tkinter library for the GUI and the OpenWeatherMap API to fetch weather data. Follow the steps below to build the application.

## Prerequisites

- Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- An API key from OpenWeatherMap. You can get it by signing up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).

## Steps

### 1. Import Libraries

First, import the necessary libraries:

```python
from tkinter import *
from tkinter import ttk
import requests
```

### 2. Define the `data_get` Function

This function fetches weather data for the selected city and updates the labels:

```python
def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=YOUR_API_KEY").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])
```
Replace `YOUR_API_KEY` with your actual API key from OpenWeatherMap.

### 3. Create the Main Window

Set up the main window:

```python
win = Tk()
win.title("Weather App")
win.config(bg="blue")
win.geometry("500x570")
```

### 4. Add Title Label

Add a label for the app's title:

```python
name_label = Label(win, text="Weather App", font=("Time New Roman", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=450)
```

### 5. Add City Selection Dropdown

Add a dropdown menu for selecting the city:

```python
city_name = StringVar()

list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"]

com = ttk.Combobox(win, values=list_name, font=("Time New Roman", 20, "bold"), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)
```

### 6. Add Weather Labels

Add labels to display the weather information:

```python
# Weather Label
w_label = Label(win, text="Weather Climate", font=("Time New Roman", 20))
w_label.place(x=25, y=260, height=50, width=210)

w_label1 = Label(win, text="", font=("Time New Roman", 20))
w_label1.place(x=250, y=260, height=50, width=210)

# Weather Description
wb_label = Label(win, text="Weather Description", font=("Time New Roman", 16))
wb_label.place(x=25, y=330, height=50, width=210)

wb_label1 = Label(win, text="", font=("Time New Roman", 17))
wb_label1.place(x=250, y=330, height=50, width=210)

# Temperature
temp_label = Label(win, text="Temperature", font=("Time New Roman", 20))
temp_label.place(x=25, y=400, height=50, width=210)

temp_label1 = Label(win, text="", font=("Time New Roman", 20))
temp_label1.place(x=250, y=400, height=50, width=210)

# Pressure
per_label = Label(win, text="Pressure", font=("Time New Roman", 20))
per_label.place(x=25, y=470, height=50, width=210)

per_label1 = Label(win, text="", font=("Time New Roman", 20))
per_label1.place(x=250, y=470, height=50, width=210)
```

### 7. Add the Done Button

Add a button to fetch the weather data:

```python
done_button = Button(win, text="Done", font=("sans-serif", 10, "bold"), command=data_get)
done_button.place(x=200, y=190, height=50, width=100)
```

### 8. Run the Application

Start the Tkinter main loop to run the application:

```python
win.mainloop()
```

## Complete Code

```python
from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=YOUR_API_KEY").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])

win = Tk()
win.title("Weather App")
win.config(bg="blue")
win.geometry("500x570")

name_label = Label(win, text="Weather App", font=("Time New Roman", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()

list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"]

com = ttk.Combobox(win, values=list_name, font=("Time New Roman", 20, "bold"), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

# Weather Label
w_label = Label(win, text="Weather Climate", font=("Time New Roman", 20))
w_label.place(x=25, y=260, height=50, width=210)

w_label1 = Label(win, text="", font=("Time New Roman", 20))
w_label1.place(x=250, y=260, height=50, width=210)

# Weather Description
wb_label = Label(win, text="Weather Description", font=("Time New Roman", 16))
wb_label.place(x=25, y=330, height=50, width=210)

wb_label1 = Label(win, text="", font=("Time New Roman", 17))
wb_label1.place(x=250, y=330, height=50, width=210)

# Temperature
temp_label = Label(win, text="Temperature", font=("Time New Roman", 20))
temp_label.place(x=25, y=400, height=50, width=210)

temp_label1 = Label(win, text="", font=("Time New Roman", 20))
temp_label1.place(x=250, y=400, height=50, width=210)

# Pressure
per_label = Label(win, text="Pressure", font=("Time New Roman", 20))
per_label.place(x=25, y=470, height=50, width=210)

per_label1 = Label(win, text="", font=("Time New Roman", 20))
per_label1.place(x=250, y=470, height=50, width=210)

done_button = Button(win, text="Done", font=("sans-serif", 10, "bold"), command=data_get)
done_button.place(x=200, y=190, height=50, width=100)

win.mainloop()
```

## Resources

- [Python](https://www.python.org/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [OpenWeatherMap API](https://openweathermap.org/api)

---
