from tkinter import *
import requests
import json
 
headers = {
        "Access-Token":"",
        "Client-Secret":"",
        "Content-Type":"application/json",
        "Accept":"application/json",
        }
main_url = 'https://api.fortnox.se/3/'

#Repopulates the list so all values are up to date 
def populate_list():
    parts_list.delete(0,END)
    callAPI()

#Clears all the fields
def clear_text():
     price_entry.delete(0, END)
     end_point_entry.delete(0, END)


def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item)
    except IndexError:
        pass

#Calls the api and renders out 
def callAPIPrice():
    global url
    url = main_url + end_point_entry.get()
    resp = requests.get(url, headers=headers).json()
    print(json.dumps(resp, indent=4))
    for item in [resp['Price']['Price']]:
       parts_list.insert(END, item)
 

def callAPI():
        url = main_url + end_point_entry.get()
        resp = requests.get(url, headers=headers).json()
        print(json.dumps(resp, indent=4))
        for item in [resp]:
            parts_list.insert(END, item)

#Updates price on a article
def updatePrice():
    data = json.dumps ({
    "Price": {
        "Price": price_entry.get()
    }
})
    #print(data)
    putURL = url
    requests.put(putURL, data=data, headers=headers).json()
    #print(resp)
    populate_list()

#Create window
app = Tk()
 
#Price
price_text = StringVar()
price_label = Label(app, text='Pris', font=('bold', 14), pady=20, padx=40)
price_label.grid(row=0, column=0, sticky=W)
price_entry = Entry(app, textvariable = price_text, border=0, font=(14))
price_entry.grid(row=0, column= 1)
 
#EndPoint
 
end_point = StringVar()
end_point_label = Label(app, text='Endpoint', font=('bold', 14), pady=20)
end_point_label.grid(row=1, column=0)
end_point_entry = Entry(app, border=0, font=(14))
end_point_entry.grid(row=1, column=1)
    
#Parts lists
parts_list = Listbox(app, height=10, width=90, border=0)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, padx=20 )
parts_list.bind('<<ListboxSelect>>', select_item)
 
#Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3, rowspan=6,sticky=N+S)

scrollbar2 = Scrollbar(app, orient=HORIZONTAL)
scrollbar2.grid(row=9, column=0, columnspan=3, sticky=E+W, padx=20)
#set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set, xscrollcommand=scrollbar2.set)
scrollbar.configure(command=parts_list.yview)
scrollbar2.configure(command=parts_list.xview)

 
#Buttons
add_btn = Button(app, text='Hämta Pris', width=12, command=callAPIPrice, background = '#6f9e6f', foreground='white', border=0, activebackground='#c0eac0', font=('bold'))
add_btn.grid(row=2, column=0,pady=20 ,padx=20)

add_btn = Button(app, text='Hämta', width=12, command=callAPI, background = '#c22626', foreground='white', border=0, activebackground='#c0eac0', font=('bold'))
add_btn.grid(row=2, column=3,padx=20)
 
update_btn = Button(app, text='Uppdatera', width=12, command=updatePrice, background='#FFC300', foreground='white', border=0, font=('bold'), activebackground='#c0eac0')
update_btn.grid(row=2, column=2,padx=20)
 
clear_btn = Button(app, text='Rensa input', width=12, command=clear_text, background='#d0dd00', foreground='white', border=0, font=('bold'),activebackground='#c0eac0')
clear_btn.grid(row=2, column=1,padx=20)


app.title('Fortnox Manager')
app.configure(background ='#eaf1ea')
app.geometry('800x400')
 
#start program
app.mainloop()