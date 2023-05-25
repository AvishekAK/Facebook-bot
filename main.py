from tkinter import *
from tkinter import ttk 
import uuid #allows users to create a unique identifier
import json #allows user to create read and write json file
from tkinter import filedialog
from PIL import Image, ImageTk

global my_data_list
global currentRowIndex

my_data_list = []

primary = Tk();
primary.geometry('1500x406')
primary.title("Manager Window")

def make_new_record():
    blankTuple = ('','','','','','','','','','','','','','')
    open_popup('add',blankTuple,primary)

btnNewRecord = Button(primary,text='Add New', bg = "#90EE90",
                      padx=2,pady=3,command=lambda:make_new_record())
btnNewRecord.grid(row=0,column=0,sticky='w')

trv = ttk.Treeview(primary,columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15),
                   show='headings',height='16')
trv.grid(row=1,column=0,rowspan=16,columnspan=5)

trv.heading(1,text="Action",anchor='w')
trv.heading(2,text="ID",anchor='center')
trv.heading(3,text="SKU_ID",anchor='center')
trv.heading(4,text="Title",anchor='center')
trv.heading(5,text="Price",anchor='center')
trv.heading(6,text="Category",anchor='center')
trv.heading(7,text="Condition",anchor='center')
trv.heading(8,text="Description",anchor='center')
trv.heading(9,text="Tags",anchor='center')
trv.heading(10,text="Location",anchor='center')
trv.heading(11,text="Photos",anchor='center')
trv.heading(12,text="Groups",anchor='center')
trv.heading(13,text="Actual_Price",anchor='center')
trv.heading(14,text="Delivery_Fee",anchor='center')
trv.heading(15,text="Seller",anchor='center')

trv.column("#1",anchor='w',width=75,stretch=False)
trv.column("#2",anchor='w',width=200,stretch=True)
trv.column("#3",anchor='w',width=75,stretch=False)
trv.column("#4",anchor='w',width=75,stretch=False)
trv.column("#5",anchor='w',width=100,stretch=False)
trv.column("#6",anchor='w',width=150,stretch=True)
trv.column("#7",anchor='w',width=100,stretch=True)
trv.column("#8",anchor='w',width=100,stretch=False)
trv.column("#9",anchor='w',width=100,stretch=False)
trv.column("#10",anchor='w',width=100,stretch=False)
trv.column("#11",anchor='w',width=75,stretch=False)
trv.column("#12",anchor='w',width=75,stretch=False)
trv.column("#13",anchor='w',width=75,stretch=False)
trv.column("#14",anchor='w',width=75,stretch=False)
trv.column("#15",anchor='w',width=75,stretch=False)

def load_json_from_file():
    global my_data_list
    with open("C:\\Users\\user\\Desktop\\New json reader\\products2.json","r") as file_handler:
        my_data_list = json.load(file_handler)
    file_handler.close
    print('file has been read and closed')

def remove_all_data_from_trv():
    for item in trv.get_children():
        trv.delete(item)

def load_trv_with_json():
    global my_data_list

    remove_all_data_from_trv()

    rowIndex = 1 

    for key in my_data_list:
        guid_value = key['id']
        skuid_value = key['skuid_value']
        title_value = key['title_value']
        price_value = key['price_value']
        category_value = key['category_value']
        condition_value = key['condition_value']
        description_value = key['description_value']
        tags_value = key['tags_value']
        location_value = key['location_value']
        photos_value = key['photos_value']
        groups_value = key['groups_value']
        actprice_value = key['actprice_value']
        delfee_value = key['delfee_value']
        seller_value = key['seller_value']

        trv.insert('',index='end',iid=rowIndex,text='',
                   values=('edit',guid_value,skuid_value,title_value,price_value,category_value,condition_value,
                           description_value,tags_value,location_value,photos_value,groups_value,actprice_value,
                           delfee_value,seller_value))
        rowIndex=rowIndex+1

def MousebuttonUpCallBack(event):
    global trv
    currentRowIndex = trv.selection()[0]
    lastTuple = (trv.item(currentRowIndex,'values'))
    open_popup('edit',lastTuple,primary)

def open_popup(_mode,_tuple,primary):
    global myname
    child = Toplevel(primary);
    child.geometry('1000x800');
    child.title('Child Window')
    child.grab_set(); #alow it to receive events 
                    #and prevent users from interaacting with the main window
    child.configure(bg='steel blue');  
    load_form = True;
    input_frame = LabelFrame(child, text='Enter New Record',
                             bg='steel blue',
                             font=('Caslon',14))
    input_frame.grid(row=0,rowspan=6,column=0)

    l1 = Label(input_frame, text='ID',width=25,height=2,anchor='w',
               relief='ridge',font=('Caslon',14))
    l2 = Label(input_frame, text='SKU_ID',width=25,height=2,anchor='w',
               relief='ridge',font=('Caslon',14))
    l3 = Label(input_frame, text='Title',width=25,height=2,anchor='w',
               relief='ridge',font=('Caslon',14))
    l4 = Label(input_frame, text='Price',width=25,height=2,anchor='w',
               relief='ridge',font=('Caslon',14))
    l5 = Label(input_frame, text='Category',width=25,height=2,anchor='w',
               relief='ridge',font=('Caslon',14))
    l6 = Label(input_frame, text='Condition',width=25,height=2,anchor='w',
               relief='ridge',font=('Caslon',14))
    l7 = Label(input_frame, text='Description',width=25,height=2,anchor='w',
               relief='ridge',font=('Caslon',14))
    l8 = Label(input_frame, text='Tags',width=25,height=2,anchor='w',
               relief='ridge',font=('Caslon',14))
    l9 = Label(input_frame, text='Location',width=25,height=2,anchor='w',
               relief='ridge',font=('Caslon',14))
    l10 = Label(input_frame, text='Photos',width=25,height=2,anchor='w',
               relief='ridge',font=('Caslon',14))
    l11 = Label(input_frame, text='Groups',width=25,height=2,anchor='w',
               relief='ridge',font=('Caslon',14))
    l12 = Label(input_frame, text='Actual_Price',width=25,height=2,anchor='w',
               relief='ridge',font=('Caslon',14))
    l13 = Label(input_frame, text='Delivery_Fee',width=25,height=2,anchor='w',
               relief='ridge',font=('Caslon',14))
    l14 = Label(input_frame, text='Seller',width=25,height=2,anchor='w',
               relief='ridge',font=('Caslon',14))
    l1.grid(column=0,row=0,padx=1,pady=0);
    l2.grid(column=0,row=1,padx=1,pady=0);
    l3.grid(column=0,row=2,padx=1,pady=0);
    l4.grid(column=0,row=3,padx=1,pady=0);
    l5.grid(column=0,row=4,padx=1,pady=0);
    l6.grid(column=0,row=5,padx=1,pady=0);
    l7.grid(column=0,row=6,padx=1,pady=0);
    l8.grid(column=0,row=7,padx=1,pady=0);
    l9.grid(column=0,row=8,padx=1,pady=0);
    l10.grid(column=0,row=9,padx=1,pady=0);
    l11.grid(column=0,row=10,padx=1,pady=0);
    l12.grid(column=0,row=11,padx=1,pady=0);
    l13.grid(column=0,row=12,padx=1,pady=0);
    l14.grid(column=0,row=13,padx=1,pady=0);

   # def select_file():
   #     path= filedialog.askopenfilename(title="Select an Image", filetype=(('image    files','*.jpg'),('all files','*.*')))
   #     img= Image.open(path)
   #     return path


    id_value = StringVar()
    id_value.set(uuid.uuid4())

    crm_id = Label(input_frame, anchor='w', height=1, relief='ridge',textvariable=id_value,
                   font=('Caslon',14))
    crm_id.grid(row=0, column=1,padx=20)
    sku_en = Entry(input_frame,width=30,borderwidth=2,fg='black',font=('Caslon',14))
    sku_en.grid(row=1,column=1)
    title_en = Entry(input_frame,width=30,borderwidth=2,fg='black',font=('Caslon',14))
    title_en.grid(row=2,column=1)
    price_en = Entry(input_frame,width=30,borderwidth=2,fg='black',font=('Caslon',14))
    price_en.grid(row=3,column=1)
    category_en = Entry(input_frame,width=30,borderwidth=2,fg='black',font=('Caslon',14))
    category_en.grid(row=4,column=1)
    condition_en = Entry(input_frame,width=30,borderwidth=2,fg='black',font=('Caslon',14))
    condition_en.grid(row=5,column=1)
    description_en = Entry(input_frame,width=30,borderwidth=2,fg='black',font=('Caslon',14))
    description_en.grid(row=6,column=1)
    tags_en = Entry(input_frame,width=30,borderwidth=2,fg='black',font=('Caslon',14))
    tags_en.grid(row=7,column=1)
    location_en = Entry(input_frame,width=30,borderwidth=2,fg='black',font=('Caslon',14))
    location_en.grid(row=8,column=1)
    photos_en = Entry(input_frame,width=20,borderwidth=2,fg='black',font=('Caslon',14))
    photos_en.grid(row=9,column=1)
    upload_button = Button(input_frame,text="Upload",width=10)
    upload_button.grid(row=9,column=2)
    groups_en = Entry(input_frame,width=30,borderwidth=2,fg='black',font=('Caslon',14))
    groups_en.grid(row=10,column=1)
    actprice_en = Entry(input_frame,width=30,borderwidth=2,fg='black',font=('Caslon',14))
    actprice_en.grid(row=11,column=1)
    delfee_en = Entry(input_frame,width=30,borderwidth=2,fg='black',font=('Caslon',14))
    delfee_en.grid(row=12,column=1)
    seller_en = Entry(input_frame,width=30,borderwidth=2,fg='black',font=('Caslon',14))
    seller_en.grid(row=13,column=1)


    btnAdd = Button(input_frame,text='Save',padx=5,pady=10,command=lambda:determineAction())
    btnAdd.grid(row=14,column=0)

    btnDelete = Button(input_frame,text='Delete',padx=5,pady=10,command=lambda:delete_record())
    btnDelete.grid(row=14,column=3)

    btnCancel = Button(input_frame,text='Cancel',padx=5,pady=10,command=lambda:child_cancel())
    btnCancel.grid(row=14,column=4)

    load_form = False;

    def delete_record():
        guid_value = id_value.get()
        skuid_value = sku_en.get()
        title_value = title_en.get()
        price_value = price_en.get()
        category_value = category_en.get()
        condition_value = condition_en.get()
        description_value = description_en.get()
        tags_value = tags_en.get()
        location_value = location_en.get()
        photos_value = photos_en.get()
        groups_value = groups_en.get()
        actprice_value = actprice_en.get()
        delfee_value = delfee_en.get()
        seller_value = seller_en.get()
        process_request('_DELETE_',guid_value,skuid_value,title_value,price_value,category_value,condition_value,description_value,tags_value,
                        location_value,photos_value,groups_value,actprice_value,delfee_value,seller_value)
        reload_main_form()
        child.grab_release();
        child.destroy()
        child.update()

    def child_cancel():
            child.grab_release();
            child.destroy()
            child.update()

    def reload_main_form():
        load_trv_with_json()

    def change_background_color(new_color):
        sku_en.config(bg=new_color)
        title_en.config(bg=new_color)
        price_en.config(bg=new_color)
        category_en.config(bg=new_color)
        condition_en.config(bg=new_color)
        description_en.config(bg=new_color)
        tags_en.config(bg=new_color)
        location_en.config(bg=new_color)
        photos_en.config(bg=new_color)
        groups_en.config(bg=new_color)
        actprice_en.config(bg=new_color)
        delfee_en.config(bg=new_color)
        seller_en.config(bg=new_color)
    
    def add_entry():
        guid_value = id_value.get()
        skuid_value = sku_en.get()
        title_value = title_en.get()
        price_value = price_en.get()
        category_value = category_en.get()
        condition_value = condition_en.get()
        description_value = description_en.get()
        tags_value = tags_en.get()
        location_value = location_en.get()
        photos_value = photos_en.get()
        groups_value = groups_en.get()
        actprice_value = actprice_en.get()
        delfee_value = delfee_en.get()
        seller_value = seller_en.get()

        if len(title_value)==0:
            change_background_color('#FF82AE')
            return
        
        process_request('_INSERT_',guid_value,skuid_value,title_value,price_value,category_value,condition_value,description_value,tags_value,
                        location_value,photos_value,groups_value,actprice_value,delfee_value,seller_value)
        
    def update_entry():
        guid_value = id_value.get()
        skuid_value = sku_en.get()
        title_value = title_en.get()
        price_value = price_en.get()
        category_value = category_en.get()
        condition_value = condition_en.get()
        description_value = description_en.get()
        tags_value = tags_en.get()
        location_value = location_en.get()
        photos_value = photos_en.get()
        groups_value = groups_en.get()
        actprice_value = actprice_en.get()
        delfee_value = delfee_en.get()
        seller_value = seller_en.get()
        if len(title_value)==0:
            change_background_color('#FF82AE')
            return
        
        process_request('_UPDATE_',guid_value,skuid_value,title_value,price_value,category_value,condition_value,description_value,tags_value,
                        location_value,photos_value,groups_value,actprice_value,delfee_value,seller_value)
    
    def load_edit_field_with_row_data(_tuple):
        if len(_tuple)==0:
            return;
    
        id_value.set(_tuple[1]);
        sku_en.delete(0,END)
        sku_en.insert(0,_tuple[2])
        title_en.delete(0,END)
        title_en.insert(0,_tuple[3])
        price_en.delete(0,END)
        price_en.insert(0,_tuple[4])
        category_en.delete(0,END)
        category_en.insert(0,_tuple[5])
        condition_en.delete(0,END)
        condition_en.insert(0,_tuple[6])
        description_en.delete(0,END)
        description_en.insert(0,_tuple[7])
        tags_en.delete(0,END)
        tags_en.insert(0,_tuple[8])
        location_en.delete(0,END)
        location_en.insert(0,_tuple[9])
        photos_en.delete(0,END)
        photos_en.insert(0,_tuple[10])
        groups_en.delete(0,END)
        groups_en.insert(0,_tuple[11])
        actprice_en.delete(0,END)
        actprice_en.insert(0,_tuple[12])
        delfee_en.delete(0,END)
        delfee_en.insert(0,_tuple[13])
        seller_en.delete(0,END)
        seller_en.insert(0,_tuple[14])

    if _mode== 'edit':
        load_edit_field_with_row_data(_tuple)
    
    def process_request(command_type,guid_value,skuid_value,title_value,price_value,category_value,condition_value,description_value,tags_value,
                        location_value,photos_value,groups_value,actprice_value,delfee_value,seller_value):
        global my_data_list
        global dirty
        dirty = True

        if command_type == '_UPDATE_':
            row = find_row_in_my_data_list(guid_value)
            if row >= 0:
                dict = {"id":guid_value,"skuid_value":skuid_value,"title_value":title_value,"price_value":price_value,"category_value":category_value,
                        "condition_value":condition_value,"description_value":description_value,"tags_value":tags_value,"location_value":location_value,
                        "photos_value":photos_value,"groups_value":groups_value,"actprice_value":actprice_value,"delfee_value":delfee_value,"seller_value":seller_value}
                my_data_list[row]=dict
        
        elif command_type == "_INSERT_":
            dict = {"id":guid_value,"skuid_value":skuid_value,"title_value":title_value,"price_value":price_value,"category_value":category_value,
                        "condition_value":condition_value,"description_value":description_value,"tags_value":tags_value,"location_value":location_value,
                        "photos_value":photos_value,"groups_value":groups_value,"actprice_value":actprice_value,"delfee_value":delfee_value,"seller_value":seller_value}
            my_data_list.append(dict)
        
        elif command_type == "_DELETE":
            row = find_row_in_my_data_list(guid_value)
            if row >= 0:
                del my_data_list[row];
        
        save_json_to_file();
        clear_all_fields();
    
    def find_row_in_my_data_list(guid_value):
        global my_data_list
        row = 0
        found = False

        for rec in my_data_list:
            if rec['id'] == guid_value:
                found = True
                break
            row =row+1
        
        if(found==True):
            return(row)
        
        return(-1)
    def determineAction():
        if load_form == False:
            if _mode == "edit":
                update_entry();
            else:
                add_entry();
        
        reload_main_form()
        child.grab_release();
        child.destroy()
        child.update()

    def save_json_to_file():
        global my_data_list
        with open("C:\\Users\\user\\Desktop\\New json reader\\products2.json",'w') as file_handler:
            json.dump(my_data_list, file_handler,indent=4)
        file_handler.close
        print("file has been written to and closed")
    
    def load_json_from_file():
        global my_data_list
        with open("C:\\Users\\user\\Desktop\\New json reader\\products2.json",'r') as file_handler:
            my_data_list = json.load(file_handler)
        file_handler.close
        print('file has been read and closed')
    
    def clear_all_fields():
        sku_en.delete(0,END)
        title_en.delete(0,END)
        price_en.delete(0,END)
        category_en.delete(0,END)
        condition_en.delete(0,END)
        description_en.delete(0,END)
        tags_en.delete(0,END)
        location_en.delete(0,END)
        photos_en.delete(0,END)
        groups_en.delete(0,END)
        actprice_en.delete(0,END)
        delfee_en.delete(0,END)
        seller_en.delete(0,END)
        crm_id.configure(text="")
        sku_en.focus_set()
        id_value.set(uuid.uuid4())
        change_background_color('#FFFFFF')

trv.bind("<ButtonRelease>",MousebuttonUpCallBack)
load_json_from_file()
load_trv_with_json()
primary.mainloop()








        





        
