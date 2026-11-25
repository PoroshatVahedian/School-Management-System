############ app school management ###########
import csv
import jdatetime
import re
import national_id_validation
import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
from random import randint

first_use = Tk()
first_use.title('setting up')
first_use.geometry('900x700')
first_use.resizable(False, False)
first_use.configure(background='#c9af98')


class Human:
    fields = ['mathematics', 'science', 'humanities']
    age_in_years = 0
    txt_validation = False
    national_id_validation = False
    birth_date_validation_ = False
    phone_number_validation = False

    def __init__(self, national_id, name, last_name, gender, birth_date, address, phone_number, father_name, state, city, _type):
        self.national_id = national_id
        self.name = name
        self.last_name = last_name
        self.gender = gender
        self.birth_date = birth_date
        self.address = address
        self.phone_number = phone_number
        self.father_name = father_name
        self.state = state
        self.city = city
        self._type = _type

    @staticmethod
    def birth_date_validation(a_birth_date):
        birth_pattern = r'^\d{4}\/\d{2}\/\d{2}$'
        if re.findall(birth_pattern, a_birth_date):
            birth_year = re.findall(r'^\d{4}', a_birth_date)
            if 1340 < int(birth_year[0]) < 1390:
                birth_day_month = re.findall(r'\d{2}', a_birth_date)
                if (1 <= int(birth_day_month[2]) <= 6 or int(birth_day_month[2])==12) and 1 <= int(birth_day_month[3]) <= 31:
                    parsed_date = a_birth_date.split('/')
                    target_date = jdatetime.date(int(parsed_date[0]) , int(parsed_date[1]) , int(parsed_date[2]))
                    now_date = jdatetime.datetime.now().date()
                    deference = now_date-target_date
                    age_in_days = deference.days
                    Human.age_in_years = age_in_days / 365

                elif 7 <= int(birth_day_month[2]) <= 11 and 1 <= int(birth_day_month[3]) <= 30:
                    parsed_date = a_birth_date.split('/')
                    target_date = jdatetime.date(int(parsed_date[0]) , int(parsed_date[1]) , int(parsed_date[2]))
                    now_date = jdatetime.datetime.now().date()
                    deference = now_date-target_date
                    age_in_days = deference.days
                    Human.age_in_years = age_in_days / 365

                else:
                    print('!!Birth day or birth month is invalid!!')
            else:
                print('!!Birth year is invalid!!')
        else:
            print('!!Birth date is invalid!!')
        
    @staticmethod
    def names_validation_func(name, last_name, father_name):
        if len(name) >= 3 and len(last_name) >= 3 and re.findall(r'^[A-Za-z]+$' ,name) and re.findall(r'^[A-Za-z]+$', last_name) and re.findall(r'^[A-Za-z]+$', father_name):
            Human.txt_validation = True
            return Human.txt_validation
        else:
            Human.txt_validation = False
            print('!!Name or lastname entered is not valid!!')
            return Human.txt_validation
        
    @staticmethod
    def national_id_validation_func(a_national_id):
        national_id_check = national_id_validation.national_id_validation_function(a_national_id)
        if national_id_check == False:
            Human.national_id_validation = False
            print('!!The entered National ID is not valid!!')
            return Human.national_id_validation
        else:
            Human.national_id_validation = True
            return Human.national_id_validation

    @staticmethod
    def phone_number_validation_func(a_phone_number):
        if re.findall(r'^09\d{9}$|^\+989\d{9}$', a_phone_number):
            Human.phone_number_validation = True
            return Human.phone_number_validation
        else:
            Human.phone_number_validation =  False
            print('!!Phone number entered is not valid!!')
            return Human.phone_number_validation
        
new_school = None

def primitive_register_def():
    global new_school
    school_data = [school_name, school_capacity, school_annual_tuition, school_type, school_reg_num,
    school_phone, school_area, school_city, school_state, school_established_year]
    school_name_validation = False
    capacity_validation = False
    annual_tuition_validation = False
    for i in school_data:
        if i.get() == '':
            i.insert(0, '!!Required!!')
    else:
        if re.findall(r'^[A-Za-z]+$' , school_name.get()):
            school_name_validation == True
        else:
            school_name.insert(0, '!!Invalid school name!!')
        if 20 <= int(school_capacity.get()) <= 1000:
            capacity_validation == True
        else:
            school_capacity.insert(0, '!!Invalid capacity!!')
        if 100 <= int(school_annual_tuition.get()) <= 100000000:
            annual_tuition_validation == True
        else:
            school_annual_tuition.insert(0, '!!Invalid annual tuition!!')
        school_reg_num_validation = False
        if re.findall(r'^\d{10}$', school_reg_num.get()):
            school_reg_num_validation == True
        else:
            school_reg_num.insert(0, '!!Invalid registertion code!!')
        school_phone_validation = False
        if re.findall(f'^{phone_codes[school_state.get()]}\d{8}$', school_phone.get()):
            school_phone_validation == True
        else:
            school_phone.insert(0, '!!Invalid phone number!!')
        school_area_validation = False
        if 3 <= int(school_area.get()) <= 22:
            school_area_validation == True
        else:
            school_area.insert(0, '!!Invalid Area!!')
        school_established_year_validation = False
        current_date = jdatetime.datetime.now()
        current_year = current_date.year
        if 1350 <= int(school_established_year.get()) <= current_year:
            school_established_year_validation == True
        else:
            school_established_year.insert(0, '!!Invalid Area!!')

        if school_name_validation == True and capacity_validation == True and annual_tuition_validation == True and school_reg_num_validation == True and school_phone_validation == True and school_area_validation == True and school_established_year == True:

            new_manager = Manager.register(national_id = manager_national_id.get(), name = manager_fname.get(), last_name = manager_lname.get(), birth_date = f'{manager_birth_year.get()}/{manager_birth_month.get()}/{manager_birth_day.get()}', 
            address = manager_address.get(), phone_number = manager_phone_number.get(), father_name = manager_father_name.get(), state = manager_state.get(), city = manager_city.get(), _type = 'manager', work_experience = manager_work_experience.get(), education = manager_education.get())

            new_manager = Manager.register(national_id = manager_national_id.get(), name = manager_fname.get(), last_name = manager_lname.get(), gender = gender_var.get(), birth_date = f'{manager_birth_year.get()}/{manager_birth_month.get()}/{manager_birth_day.get()}', address = manager_address.get(),
                                            phone_number = manager_phone_number.get(), father_name = manager_father_name.get(), state = manager_state.get(), city = manager_city.get(), _type = 'manager', work_experience = manager_work_experience.get(), education = manager_education.get())
            new_school = School(school_name.get(), school_type.get(), int(school_established_year.get()), school_area.get(), int(school_capacity.get()), int(school_annual_tuition.get()), school_reg_num.get(),
            school_phone.get(), school_state.get(), school_city.get(), new_manager)
            new_school.register_school()
            first_use.destroy()


        else:
            messagebox.showerror('something went wrong', 'Some of the information entered is invalid!')


class School:
    student_number = 0
    teacher_number = 0
    moderators_number = 0
    school_name_ = ''
    def __init__(self, name, type, registration_code, established_year, capacity, annual_tuition, phone_number, state, city, area, manager):
        self.name = name
        self.type = type
        self.registration_code = registration_code
        self.student_num = 0
        self.established_year = established_year
        self.capacity = capacity
        self.annual_tuition = annual_tuition
        self.phone_number = phone_number
        self.state = state
        self.city = city
        self.area = area
        self.manager = manager
        self.students = []
        self.moderators = []
        self.teachers = []
        self.classes = []
        School.school_name_ = name


    def register_school(self):
        all_dirs = os.listdir()
        if self.name not in all_dirs:
            school_folder = os.mkdir(self.name)
        with open(f'{self.name}/school date.csv', 'w') as file:
            file_content = csv.writer(file)
            file_content.writerow([self.registration_code, self.name, self.type, self.student_num, self.established_year,
            self.capacity, self.annual_tuition, self.phone_number, self.state, self.city, self.area])
            
class Manager(Human):
    s_birth_date_res = False
    def __init__(self, national_id, name, last_name, gender, birth_date, address, phone_number, father_name, state, city, _type, work_experience, education):
        super().__init__(national_id, name, last_name, gender, birth_date, address, phone_number, father_name, state, city, 'manager')
        self.work_experience = work_experience
        self.education = education

    @classmethod    
    def register(cls, **kwargs):
        txt_validation_res = super().names_validation_func(kwargs['name'], kwargs['last_name'], kwargs['father_name'])
        national_id_validation_res = super().national_id_validation_func(kwargs['national_id'])
        super().birth_date_validation(kwargs['birth_date'])
        if kwargs['_type'] == 'student':
            if kwargs['grade'] =='10th' and (super().age_in_years < 15 or super().age_in_years >= 17):
                cls.s_birth_date_res = False
                print("!!Student\'s age is not valid!!")
            elif kwargs['grade'] =='11th' and (super().age_in_years < 16 or super().age_in_years >= 18):
                cls.s_birth_date_res = False
                print("!!Student\'s age is not valid!!")
            elif kwargs['grade'] =='12th' and (super().age_in_years < 17 or super().age_in_years >= 19):
                cls.s_birth_date_res = False
                print("!!Student\'s age is not valid!!")
            else:
                cls.s_birth_date_res = True
        elif kwargs['_type'] == 'manager' or kwargs['_type'] == 'teacher':
            if 18 < Human.age_in_years < 60:
                cls.s_birth_date_res = True
        else:
            print('err')
        phone_number_validation_res = super().phone_number_validation_func(kwargs['phone_number'])


        if txt_validation_res == True and national_id_validation_res == True and cls.s_birth_date_res == True and phone_number_validation_res == True:
            if kwargs['_type'] == 'student':
                with open('database.csv', 'r') as file:
                    check_line = file.readline()
                    if check_line == '' or check_line == '\n':
                        with open('database.csv', 'a') as file:
                                file_content.writerow(list(kwargs.values()))
                                School.student_number += 1
                                new_school.students.append(Student(**kwargs))
                        return new_school.students
                    else:
                        with open('database.csv', 'r') as file:
                            file_prs = csv.reader((file))
                            for check in file_prs:
                                if kwargs['national_id'] == check[0]:
                                    print('This student is already registered!')
                                    break
                            else:
                                with open('database.csv', 'a') as file:
                                    file_content =csv.writer(file)
                                    file_content.writerow(list(kwargs.values()))
                                    School.student_number += 1
                                    new_school.students.append(Student(**kwargs))
                                    print(new_school.students)
                return new_school.students
            elif kwargs['_type'] == 'teacher':
                with open('teachers_database.csv', 'r') as file:
                    check_line = file.readline()
                    if check_line == '' or check_line == '\n':
                        with open('teachers_database.csv', 'a') as file:
                                file_content =csv.writer(file)
                                file_content.writerow(list(kwargs.values()))
                                School.teacher_number += 1
                                School.teachers.append(Teacher(**kwargs))
                        return School.teachers
                    else:
                        with open('teachers_database.csv', 'r') as file:
                            file_prs = csv.reader((file))
                            for check in file_prs:
                                if kwargs['national_id'] == check[0]:
                                    print('This teacher is already registered!')
                                    break
                                else:
                                    with open('teachers_database.csv', 'a') as file:
                                        file_content =csv.writer(file)
                                        file_content.writerow(list(kwargs.values()))
                                        School.teacher_number += 1
                                        School.teachers.append(Teacher(**kwargs))
                        return School.teachers
                    
            # elif kwargs['_type'] == 'moderator':
            #     with open('moderators_database.csv', 'r') as file:
            #         check_line = file.readline()
            #         if check_line == '' or check_line == '\n':
            #             with open('moderators_database.csv', 'a') as file:
            #                     file_content =csv.writer(file)
            #                     file_content.writerow(list(kwargs.values()))
            #                     School.moderators_number += 1
            #                     School.moderators.append(Moderator(**kwargs))
            #             return School.moderators
            #         else:
            #             with open('moderators_database.csv', 'r') as file:
            #                 file_prs = csv.reader((file))
            #                 for check in file_prs:
            #                     if kwargs['national_id'] == check[0]:
            #                         print('This teacher is already exist!')
            #                         break
        #                     else:
        #                         with open('moderators_database.csv', 'a') as file:
        #                             file_content =csv.writer(file)
        #                             file_content.writerow(list(kwargs.values()))
        #                             School.moderators_number += 1
        #                             School.moderators.append(Teacher(**kwargs))
            #   
                # return School.moderators                             

            elif kwargs['_type'] == 'manager':
                with open(f'{school_name.get()}/manager.csv', 'r') as file:
                    check_line = file.readline()
                    if check_line == '' or check_line == '\n':
                        with open(f'{school_name.get()}/manager.csv', 'a') as file:
                            file_content = csv.writer(file)
                            file_content.writerow(list(kwargs.values()))
                            new_manager = Manager(**kwargs)
                        return new_manager
                    else:
                        with open(f'{school_name.get()}/manager.csv', 'r') as file:
                            file_prs = csv.reader((file))
                            for check in file_prs:
                                if kwargs['national_id'] == check[0]:
                                    print('This manager is already exist!')
                                    break
                            else:
                                with open(f'{school_name.get()}/manager.csv', 'a') as file:
                                    file_content = csv.writer(file)
                                    file_content.writerow(list(kwargs.values()))
                                    new_manager = Manager(**kwargs)
                                return new_manager             
        else:
            print("!!Some incorrect information has been entered!!")

    @staticmethod
    def inquiry(national_id, parameter):
        with open('database.csv', 'r') as file:
            file_reader = csv.reader(file)
            for line in file_reader:
                if line == None:
                    return '!!No students are registered!!'
                elif line[0]==national_id:
                    return line[Student.rounds[parameter]]
            else:
                return '!!There are no students with this national code!!'


    @staticmethod
    def get_person(**kwargs):
        search_resault = []
        if search_type.get() == 'students':
            with open('database.csv', 'r') as file:
                file_reader = csv.reader(file)
                parameter_count = 0
                person_check = False

                for i in file_reader:
                    if i == []:
                        return '!!There are no students with this profile!!'
                    else:
                        for j in kwargs.keys():
                            if kwargs[j] == i[Student.rounds[j]]:
                                person_check = True
                                parameter_count += 1
                                search_resault.append(f'{parameter_count}-{i[1]} {i[2]} with national code: {i[0]}')
                            else:
                                if person_check == False:
                                    break
                        else:
                            continue
        return search_resault
    # def 
    # @staticmethod
    # def receive_tuition(a_national_id):
    #     with open('database.csv', 'r') as file:
    #         file_prs = csv.reader(file)

# students = []

# def add_person(person_type):
#     if person_type == 'student':
#         students.append(Student())

phone_codes = {
    'East Azerbaijan': '041',
    'West Azerbaijan': '044',
    'Ardabil': '045',
    'Isfahan': '031',
    'Alborz': '026',
    'Ilam': '084',
    'Bushehr': '077',
    'Tehran': '021',
    'Chaharmahal and Bakhtiari': '038',
    'South Khorasan': '056',
    'Razavi Khorasan': '051',
    'North Khorasan': '058',
    'Khuzestan': '061',
    'Zanjan': '024',
    'Semnan': '023',
    'Sistan and Baluchestan': '054',
    'Fars': '071',
    'Qazvin': '028',
    'Qom': '025',
    'Kurdistan': '087',
    'Kerman': '034',
    'Kermanshah': '083',
    'Kohgiluyeh and Boyer-Ahmad': '074',
    'Golestan': '017',
    'Gilan': '013',
    'Lorestan': '066',
    'Mazandaran': '011',
    'Markazi': '086',
    'Hormozgan': '076',
    'Hamadan': '081',
    'Yazd': '035',
}




manager_canvas = Canvas(width=900, height=700, bg='#c9af98')
manager_canvas.place(x=-2, y=-2)
manager_canvas.create_text(445, 30, text='Create Your school management app!', fill='#3a4660',font=('Arial Rounded MT Bold', 28))
female_manager_img = PhotoImage(file = 'images\icons8-manager-94.png')
male_manager_img = PhotoImage(file = 'images\icons8-manager-94 (1).png')

manager_canvas.create_text(460, 80, text='School Manager', fill='#845007',font=('Arial Rounded MT Bold', 22))
manager_canvas.create_line(346, 100, 575, 100, fill='#845007', width=3)

gender_var = StringVar()
gender_var.set('female')
female_manager = Radiobutton(first_use, image= female_manager_img, variable = gender_var, value='female', bg='#c9af98', activebackground='#c9af98')
female_manager.place(x=50, y=110)
male_manager = Radiobutton(first_use, image= male_manager_img, variable = gender_var, value='male', bg='#c9af98', activebackground='#c9af98')
male_manager.place(x=180, y=110)

manager_canvas.create_text(395, 145, text='First Name:', fill='#845007',font=('Arial Rounded MT Bold', 14))
manager_fname = ttk.Entry(first_use, width=18)
manager_fname.place(x=450, y=135)

manager_canvas.create_text(700, 145, text='Last Name:', fill='#845007',font=('Arial Rounded MT Bold', 14))
manager_lname = ttk.Entry(first_use, width=18)
manager_lname.place(x=755, y=135)

manager_canvas.create_text(395, 190, text='National ID:', fill='#845007',font=('Arial Rounded MT Bold', 14))
manager_national_id = ttk.Entry(first_use, width=18)
manager_national_id.place(x=450, y=180)

manager_canvas.create_text(670, 190, text='Education:', fill='#845007',font=('Arial Rounded MT Bold', 14))
manager_education = ttk.Entry(first_use, width=23)
manager_education.place(x=725, y=180)

manager_canvas.create_text(680, 355, text='Work Experience:', fill='#845007',font=('Arial Rounded MT Bold', 13))
manager_work_experience = ttk.Entry(first_use, width=18)
manager_work_experience.place(x=760, y=345)

manager_canvas.create_text(192, 260, text='Birth Date', fill='#845007',font=('Arial Rounded MT Bold', 14))
manager_canvas.create_line(33, 270, 360, 270 , fill='#845007', width=2)
manager_canvas.create_text(55, 295, text='Year:', fill='#845007',font=('Arial Rounded MT Bold', 14))
manager_birth_year=ttk.Entry(width=8)
manager_birth_year.place(x=80,y=284)
manager_canvas.create_text(150, 293, text='/', fill='#845007',font=('Arial Rounded MT Bold', 19))
manager_birth_month=Spinbox(manager_canvas,values=['Farvardin','Ordibehesht','Khordad','Tir','Mordad','Shahrivar','Mehr','Aban','Azar','Dey','Bahman','Esfand'],width=10,bg='#eee4de',fg='#3a4660')
manager_birth_month.place(x=165,y=286)
manager_canvas.create_text(253, 293, text='/', fill='#845007',font=('Arial Rounded MT Bold', 19))
manager_canvas.create_text(285, 293, text='Day:', fill='#845007',font=('Arial Rounded MT Bold', 14))
manager_birth_day=ttk.Entry(width=8)
manager_birth_day.place(x=305, y=285)

manager_canvas.create_text(460, 265, text='Address:', fill='#845007',font=('Arial Rounded MT Bold', 14))
manager_address = ttk.Entry(width=60)
manager_address.place(x=510, y=255)

manager_canvas.create_text(85, 350, text='Father Name:', fill='#845007',font=('Arial Rounded MT Bold', 14))
manager_father_name = ttk.Entry(width=16)
manager_father_name.place(x=148, y=340)

manager_canvas.create_text(365, 350, text='Phone number:', fill='#845007',font=('Arial Rounded MT Bold', 14))
manager_phone_number = ttk.Entry(width=17)
manager_phone_number.place(x=440, y=340)

provinces = ['East Azerbaijan', 'West Azerbaijan', 'Ardabil', 'Isfahan', 'Alborz', 'Ilam', 'Bushehr', 'Tehran', 'Chaharmahal and Bakhtiari', 'South Khorasan', 'Razavi Khorasan', 'North Khorasan', 'Khuzestan', 'Zanjan', 'Semnan', 'Sistan and Baluchestan', 'Fars', 'Qazvin', 'Qom', 'Kurdistan', 'Kerman', 'Kermanshah', 'Kohgiluyeh and Boyer-Ahmad', 'Golestan', 'Gilan', 'Lorestan', 'Mazandaran', 'Markazi', 'Hormozgan', 'Hamadan', 'Yazd']

manager_canvas.create_text(460, 310, text='Email:', fill='#845007',font=('Arial Rounded MT Bold', 14))
manager_email = ttk.Entry(width=34)
manager_email.place(x=500, y=300)

manager_canvas.create_text(50, 395, text='State:', fill='#845007',font=('Arial Rounded MT Bold', 14))
manager_state = ttk.Combobox(manager_canvas, values= provinces, width=29, font=('Arial Rounded MT Bold', 8))
manager_state.set('Tehran')
manager_state.place(x=85, y=387)

def m_update_city_combobox(event):
    selected_state = iran[manager_state.get()]
    manager_city = ttk.Combobox(manager_canvas, values=selected_state, width=29, font=('Arial Rounded MT Bold', 8))
    manager_city.set(selected_state[0])
    manager_city.place(x=465, y=387)

manager_canvas.create_text(440, 395, text='City:', fill='#845007',font=('Arial Rounded MT Bold', 14))
manager_city = ttk.Combobox(manager_canvas, values= 'Choose-your-state-first!', width=29, font=('Arial Rounded MT Bold', 8))
manager_city.set('Tehran')
manager_city.place(x=465, y=387)
manager_state.bind("<<ComboboxSelected>>", m_update_city_combobox)

iran = {
    'East Azerbaijan': ['Tabriz', 'Maragheh', 'Mianeh', 'Shabestar'],
    'West Azerbaijan': ['Urmia', 'Khoy', 'Mahabad', 'Sardasht'],
    'Ardabil': ['Ardabil', 'Meshgin Shahr', 'Parsabad'],
    'Isfahan': ['Isfahan', 'Kashan', 'Najafabad', 'Shahreza'],
    'Alborz': ['Karaj', 'Eshtehard', 'Fardis', 'Nazarabad', 'Taleghan'],
    'Ilam': ['Ilam', 'Dehloran', 'Shirvan and Chardavol', 'Abdanan'],
    'Bushehr': ['Bushehr', 'Bandar Ganaveh', 'Dayyer', 'Borazjan'],
    'Tehran': ['Tehran', 'Karaj', 'Shahriar', 'Varamin'],
    'Chaharmahal and Bakhtiari': ['Shahrekord', 'Borujen', 'Farsan', 'Lordegan'],
    'South Khorasan': ['Birjand', 'Qaenat', 'Darmiyan', 'Nehbandan'],
    'Razavi Khorasan': ['Mashhad', 'Sabzevar', 'Neyshabur', 'Torbat-e Heydarieh'],
    'North Khorasan': ['Bojnourd', 'Shirvan', 'Jajarm', 'Faruj'],
    'Khuzestan': ['Ahvaz', 'Abadan', 'Khorramshahr', 'Dezful'],
    'Zanjan': ['Zanjan', 'Abhar', 'Khodabande', 'Tarom'],
    'Semnan': ['Semnan', 'Shahroud', 'Damghan', 'Garmsar'],
    'Sistan and Baluchestan': ['Zahedan', 'Chabahar', 'Zabol', 'Iran Shahr'],
    'Fars': ['Shiraz', 'Marvdasht', 'Neyriz', 'Kazerun'],
    'Qazvin': ['Qazvin', 'Takestan', 'Abyek', 'Alborz'],
    'Qom': ['Qom', 'Kahak', 'Kahrizak', 'Salafchegan', 'Dastjerd'],
    'Kurdistan': ['Sanandaj', 'Marivan', 'Bijar', 'Saqqez'],
    'Kerman': ['Kerman', 'Bam', 'Jiroft', 'Rafsanjan'],
    'Kermanshah': ['Kermanshah', 'Islamabad-e Gharb', 'Paveh', 'Javanrud'],
    'Kohgiluyeh and Boyer-Ahmad': ['Yasuj', 'Dehdasht', 'Gachsaran', 'Dogonbadan'],
    'Golestan': ['Gorgan', 'Aliabad-e Katul', 'Kordkuy', 'Gomishan'],
    'Gilan': ['Rasht', 'Lahijan', 'Langarud', 'Soomesara'],
    'Lorestan': ['Khorramabad', 'Aligudarz', 'Borujerd', 'Dorood'],
    'Mazandaran': ['Amol', 'Babol', 'Babolsar', 'Firoozkuh', 'Ghaemshahr'],
    'Markazi': ['Arak', 'Saveh', 'Mahallat', 'Khomein', 'Ashtian', 'Tafresh'],
    'Hormozgan': ['Bandar Abbas', 'Qeshm', 'Kish Island', 'Minab', 'Jask','Hormuz'],
    'Hamadan': ['Hamadan', 'Malayer', 'Nahavand', 'Gol Tappeh', 'Tuyserkan'],
    'Yazd': ['Yazd', 'Ardakan', 'Meybod', 'Taft' ,'Bafq', 'Abarkuh', 'Khatam'],
    }

manager_canvas.create_text(460, 440, text='School ', fill='#e5521b',font=('Arial Rounded MT Bold', 22))
manager_canvas.create_line(346, 460, 575, 460, fill='#e5521b', width=3)

manager_canvas.create_text(80, 490, text='School Name:', fill='#e5521b',font=('Arial Rounded MT Bold', 14))
school_name = ttk.Entry(width=18)
school_name.place(x=150, y=480)

manager_canvas.create_text(365, 490, text='Capacity:', fill='#e5521b',font=('Arial Rounded MT Bold', 14))
school_capacity = ttk.Entry(width=18,)
school_capacity.place(x=415, y=480)

manager_canvas.create_text(650, 490, text='Annual Tuition:', fill='#e5521b',font=('Arial Rounded MT Bold', 14))
school_annual_tuition = ttk.Entry(width=18)
school_annual_tuition.place(x=725, y=480)

manager_canvas.create_text(205, 520, text='Type', fill='#e5521b',font=('Arial Rounded MT Bold', 14))
manager_canvas.create_line(35, 538, 405, 538, fill='#e5521b', width=2)
school_type = StringVar()
school_type.set('public')
public_sch = Radiobutton(first_use, text='Public School' ,variable = school_type, value='public', bg='#c9af98', activebackground='#c9af98',font=('Arial Rounded MT Bold', 10), fg='#e5521b')
public_sch.place(x=30, y=545)
ind_sch = Radiobutton(first_use, text='Independent' ,variable = school_type, value='ind', bg='#c9af98', activebackground='#c9af98',font=('Arial Rounded MT Bold', 10), fg='#e5521b')
ind_sch.place(x=150, y=545)
magnet_sch = Radiobutton(first_use, text='Magnet School' ,variable = school_type, value='Magnet', bg='#c9af98', activebackground='#c9af98',font=('Arial Rounded MT Bold', 10), fg='#e5521b')
magnet_sch.place(x=275, y=545)
gifted_sch = Radiobutton(first_use, text='Gifted School' ,variable = school_type, value='gifted', bg='#c9af98', activebackground='#c9af98',font=('Arial Rounded MT Bold', 10), fg='#e5521b')
gifted_sch.place(x=30, y=565)
charter_sch = Radiobutton(first_use, text='Charter School' ,variable = school_type, value='charter', bg='#c9af98', activebackground='#c9af98',font=('Arial Rounded MT Bold', 10), fg='#e5521b')
charter_sch.place(x=150, y=565)
international_sch = Radiobutton(first_use, text='International' ,variable = school_type, value='international', bg='#c9af98', activebackground='#c9af98',font=('Arial Rounded MT Bold', 10), fg='#e5521b')
international_sch.place(x=275, y=565)

manager_canvas.create_text(660, 535, text='Registration Number:', fill='#e5521b',font=('Arial Rounded MT Bold', 12))
school_reg_num = ttk.Entry(width=18)
school_reg_num.place(x=750, y=525)

manager_canvas.create_text(635, 570, text='School Phone Number:', fill='#e5521b',font=('Arial Rounded MT Bold', 12))
school_phone = ttk.Entry(width=18)
school_phone.place(x=740, y=560)

manager_canvas.create_text(50, 610, text='State:', fill='#e5521b',font=('Arial Rounded MT Bold', 12))
school_state = ttk.Combobox(manager_canvas, values= provinces, width=25, font=('Arial Rounded MT Bold', 8))
school_state.set('Tehran')
school_state.place(x=80, y=602)

def s_update_city_combobox(event):
    selected_state = iran[school_state.get()]
    manager_city = ttk.Combobox(manager_canvas, values=selected_state, width=25, font=('Arial Rounded MT Bold', 8))
    manager_city.set(selected_state[0])
    manager_city.place(x=358, y=602)

manager_canvas.create_text(336, 610, text='City:', fill='#e5521b',font=('Arial Rounded MT Bold', 14))
school_city = ttk.Combobox(manager_canvas, values= 'Choose-your-state-first!', width=25, font=('Arial Rounded MT Bold', 8))
school_city.set('Tehran')
school_city.place(x=358, y=602)
school_state.bind("<<ComboboxSelected>>", s_update_city_combobox)

manager_canvas.create_text(50, 645, text='Area:', fill='#e5521b',font=('Arial Rounded MT Bold', 12))
school_area = ttk.Entry(width=8)
school_area.place(x=72, y=635)

manager_canvas.create_text(385, 645, text='Established Year:', fill='#e5521b',font=('Arial Rounded MT Bold', 12))
school_established_year = ttk.Entry(width=18)
school_established_year.place(x=460, y=635)

primitive_register = Button(manager_canvas, text='Register', bg='#2d891b', fg='white', width=22, height=3 ,font=('Arial Rounded MT Bold', 11), activebackground='#2d891b', bd=0, command= lambda:primitive_register_def())
primitive_register.place(x=625, y=595)

first_use.mainloop()

win = Tk()
win.title('School Management')
win.geometry('1360x680')
win.resizable(False, False)

class Student(Human):
    rounds = {'national_id': 0, 'name': 1, 'last_name': 2,
        'birth_date': 3, 'address': 4, 'phone_number': 5, 'father_name': 6,
        'state': 7, 'city': 8, 'grade': 9, 'this_year_marks': 10,
        'previos_marks': 11, 'field': 12, '_type': 13}
    
    def __init__(self, national_id, name, last_name, gender, birth_date, address, phone_number, father_name, state, city, _type, grade, this_year_marks, previos_marks, field):
        super().__init__(national_id, name, last_name, gender,  birth_date, address, phone_number, father_name, state, city, 'student')
        self.grade = grade
        self.this_year_marks = this_year_marks
        self.previos_marks = previos_marks
        self.field = field

class Teacher(Human):
    def __init__(self, national_id, name, last_name, gender, birth_date, address, phone_number, father_name, state, city, work_experience, teaching_courses):
        super().__init__(national_id, name, last_name, gender, birth_date, address, phone_number, father_name, state, city,'teacher')
        self.work_experience = work_experience
        self.teaching_courses = teaching_courses

    def grading(self, national_id, point, field, status):
        tst = open(f'{field}_{self.teaching_courses}','r')
        try:
            file = open(f'{field}_{self.teaching_courses}','a')
            file_append = csv.writer(file)
            file_append.writerow([national_id, point, f'status:{status}'])
            file.close()
        except FileNotFoundError:
            return 'err'
        
    
        

# class Moaven(Human):
#     def __init__(self, national_id, name, last_name, birth_date, address, phone_number, father_name, state, city, special_disease, work_experience):
#         super().__init__(national_id, name, last_name, birth_date, address, phone_number, father_name, state, city, special_disease)
#         self.work_experience = work_experience

############################################################### main page ##################################################################

def show_page(page_num):
    pages.select(page_num)

pages = ttk.Notebook(win, width=1360, height=680)
pages.place(x=0, y=0)

style = ttk.Style()
style.configure('Custom.TNotebook', background='#E0EFEA')

main_page = Frame(pages, width= 250, height=250, background='#E0EFEA')
main_page.pack()
pages.add(main_page, text="Catalog")
school_page = Frame(pages, bg= '#dbe4cf')
pages.add(school_page, text="School")
manager_page = Frame(pages, bg= '#e4edc1')
pages.add(manager_page, text="Manager")
search_person_img = PhotoImage(file='images\search-oersons.png')
manager_page_search_btn = Button(manager_page, image=search_person_img, bd= 0, bg= '#e4edc1', activebackground= '#e4edc1', command= lambda: show_page(3))
manager_page_search_btn.place(x= 420, y= 25)
student_reg_img = PhotoImage(file='images\student_register.png')
student_registration_btn = Button(manager_page, image=student_reg_img, bd= 0, bg= '#e4edc1', activebackground= '#e4edc1', command= lambda: show_page(4))
student_registration_btn.place(x= 730, y= 25)
create_cls_img = PhotoImage(file=r'images\create-cls.png')
create_cls_btn = Button(manager_page, image= create_cls_img, bd= 0, bg= '#e4edc1', activebackground= '#e4edc1', command= lambda: show_page(5))
create_cls_btn.place(x= 420, y= 250)
recruitment_img = PhotoImage(file=r'images\estekhdam.png')
recruitment_btn = Button(manager_page, image= recruitment_img, bd= 0, bg= '#e4edc1', activebackground= '#e4edc1')
recruitment_btn.place(x= 730, y= 250)
salary_payment_img = PhotoImage(file='images\salary-payment.png')
salary_payment_btn = Button(manager_page, image= salary_payment_img, bd= 0, bg= '#e4edc1', activebackground= '#e4edc1')
salary_payment_btn.place(x= 420, y= 470)
receive_tuition_img = PhotoImage(file='images\pay_t.png')
receive_tuition_btn = Button(manager_page, image= receive_tuition_img, bd= 0, bg= '#e4edc1', activebackground= '#e4edc1')
receive_tuition_btn.place(x= 730, y= 470)

search_page = Frame(pages, width= 250, height=250, background='#e4edc1')
search_page.pack()
pages.add(search_page, text="Search")
funcs_frame = Frame(search_page, bg='#e4edc1', width=1200, height=650)
funcs_frame.place(x=220, y=5)

parameters_search_entry_list = []
values_search_entry_list = []

def add_search_box():
    global create_search_box
    if len(parameters_search_entry_list) <= 8 and len(values_search_entry_list) <= 7:
        new_parameter_entry = ttk.Entry(left_search_boxes_frame, width=14, font=('Arial Rounded MT Bold', 12))
        new_parameter_entry.pack(pady=5)
        parameters_search_entry_list.append(new_parameter_entry)
        new_value_entry = ttk.Entry(right_search_boxes_frame, width=14, font=('Arial Rounded MT Bold', 12))
        new_value_entry.pack(pady=5)
        values_search_entry_list.append(new_value_entry)

def search_items():
    final_parameters = []
    final_values = []
    for parameter in parameters_search_entry_list:
        final_parameters.append(parameter.get())
    for value in values_search_entry_list:
        final_values.append(value.get())

    search_resault = new_school.manager.get_person(**dict(zip(final_parameters, final_values)))
    for res in search_resault:
        show_search_res.insert(END, res)

Label(funcs_frame, text = 'Search in:', font=('Arial Rounded MT Bold', 22), bg= '#e4edc1', fg='#362E23').place(x= 20, y=10)
search_type = StringVar()
search_in_students = Radiobutton(funcs_frame, text= 'Students', variable = search_type, value='students', bg='#e4edc1', activebackground='#e4edc1', fg='#3A3C26', font=('Arial Rounded MT Bold', 15))
search_in_students.place(x=60, y=55)
search_in_teachers = Radiobutton(funcs_frame, text= 'Teachers', variable = search_type, value='teachers', bg='#e4edc1', activebackground='#e4edc1', fg='#3A3C26', font=('Arial Rounded MT Bold', 15))
search_in_teachers.place(x=220, y=55)
search_in_moderators = Radiobutton(funcs_frame, text= 'Moderators', variable = search_type, value='moderators', bg='#e4edc1', activebackground='#e4edc1', fg='#3A3C26', font=('Arial Rounded MT Bold', 15))
search_in_moderators.place(x=380, y=55)
search_type.set('students')

left_search_boxes_frame = Frame(funcs_frame, bg= '#e4edc1', width=150, height=450)
left_search_boxes_frame.place(x=60, y=185)
right_search_boxes_frame = Frame(funcs_frame, bg= '#e4edc1', width=150, height=450)
right_search_boxes_frame.place(x=255, y=185)

Label(funcs_frame, text = 'Search by:', font=('Arial Rounded MT Bold', 22), bg= '#e4edc1', fg='#362E23').place(x= 20, y=100)
Label(funcs_frame, text = 'Parameters', font=('Arial Rounded MT Bold', 16), bg= '#e4edc1', fg='#362E23').place(x= 68, y=148)
a_parameter_entry = ttk.Entry(left_search_boxes_frame, width=14, font=('Arial Rounded MT Bold', 12))
parameters_search_entry_list.append(a_parameter_entry)
a_parameter_entry.pack(pady=5)

Label(funcs_frame, text = 'Values', font=('Arial Rounded MT Bold', 16), bg= '#e4edc1', fg='#362E23').place(x= 285, y=148)
a_value_entry = ttk.Entry(right_search_boxes_frame, width=14, font=('Arial Rounded MT Bold', 12))
values_search_entry_list.append(a_value_entry)
a_value_entry.pack(pady=5)
add_search_box_img = PhotoImage(file=r'images\icons8-add-40.png')
create_search_box = Button(funcs_frame, image= add_search_box_img, bg='#e4edc1', bd=0, activebackground='#e4edc1', command= add_search_box)
create_search_box.place(x=208, y=143)
Label(funcs_frame, text='Search results', bg='#e4edc1', font=('Arial Rounded MT Bold', 14), fg='#185d21').place(x=530, y=128)
search_items_btn = Button(funcs_frame, text= 'Search', font=('Arial Rounded MT Bold', 18), bg='#185d21', fg='white', bd=0, activebackground='#e4edc1', command= lambda:search_items())
search_items_btn.place(x=150, y=550)
show_search_frame = Frame(funcs_frame, width=1600, height=500, bg= '#e4edc1')
show_search_frame.place(x=420, y=160)
show_search_res = Listbox(show_search_frame, width=40, height=25, bg='#faf29d', fg='#185d21', font=('Arial Rounded MT Bold', 11))
show_search_res.pack(side= LEFT)
scroll = Scrollbar(show_search_frame)
scroll.pack(side=LEFT, fill='y', ipadx=2)
show_search_res.config(yscrollcommand=scroll.set)
scroll.config(command=show_search_res.yview)

register_page = Frame(pages, width= 250, height=250, background='#e4edc1')
register_page.pack()
pages.add(register_page, text="Register")
funcs_frame_reg = Frame(register_page, bg='#e4edc1', width=1200, height=650)
funcs_frame_reg.place(x=140, y=5)
Label(funcs_frame_reg, text = 'Student Registration', font=('Arial Rounded MT Bold', 24), bg= '#e4edc1', fg='#362E23').place(x=380, y=5)
Label(funcs_frame_reg, text='First Name:',fg='#185d21', bg='#e4edc1',font=('Arial Rounded MT Bold', 14)).place(x=0, y=168)
student_fname = ttk.Entry(funcs_frame_reg, width=18)
student_fname.place(x=110, y=175)
Label(funcs_frame_reg, text='Last Name:',fg='#185d21', bg='#e4edc1',font=('Arial Rounded MT Bold', 14)).place(x=265, y=168)
student_lname = ttk.Entry(funcs_frame_reg, width=18,)
student_lname.place(x=380, y=175)
Label(funcs_frame_reg, text='National ID:',fg='#185d21', bg='#e4edc1',font=('Arial Rounded MT Bold', 14)).place(x=530, y=168)
student_nID = ttk.Entry(funcs_frame_reg, width=18)
student_nID.place(x=645, y=175)
Label(funcs_frame_reg, text='Father Name:',fg='#185d21', bg='#e4edc1',font=('Arial Rounded MT Bold', 14)).place(x=805, y=168)
student_father_name = ttk.Entry(funcs_frame_reg, width=18)
student_father_name.place(x=940, y=175)
Label(funcs_frame_reg, text='Birth Date',fg='#185d21', bg='#e4edc1',font=('Arial Rounded MT Bold', 20)).place(x=140, y=220)
Label(funcs_frame_reg, text='Year:',fg='#185d21', bg='#e4edc1',font=('Arial Rounded MT Bold', 14)).place(x=0, y=264)
student_birth_year = ttk.Entry(funcs_frame_reg, width=8)
student_birth_year.place(x=60, y=270)
Label(funcs_frame_reg, text='/',fg='#185d21', bg='#e4edc1',font=('Arial Rounded MT Bold', 16)).place(x=120, y=264)
Label(funcs_frame_reg, text='Month:',fg='#185d21', bg='#e4edc1',font=('Arial Rounded MT Bold', 14)).place(x=135, y=264)
student_birth_month=Spinbox(funcs_frame_reg,values=['Farvardin','Ordibehesht','Khordad','Tir','Mordad','Shahrivar','Mehr','Aban','Azar','Dey','Bahman','Esfand'],width=10,fg='#3a4660')
student_birth_month.place(x=205,y=270)
Label(funcs_frame_reg, text='/',fg='#185d21', bg='#e4edc1',font=('Arial Rounded MT Bold', 16)).place(x=290, y=264)
Label(funcs_frame_reg, text='Day:',fg='#185d21', bg='#e4edc1',font=('Arial Rounded MT Bold', 14)).place(x=305, y=264)
student_birth_day=ttk.Entry(funcs_frame_reg, width=8)
student_birth_day.place(x=355, y=270)
student_gender_var = StringVar()
student_gender_var.set('female')
Label(funcs_frame_reg, text='Gender:',fg='#185d21', bg='#e4edc1',font=('Arial Rounded MT Bold', 16)).place(x=460, y=260)
female_student = Radiobutton(funcs_frame_reg, text= 'female', variable = student_gender_var, value='female', bg='#e4edc1', activebackground='#e4edc1', fg= '#185d21', font=('Arial Rounded MT Bold', 14))
female_student.place(x=570, y=260)
male_student = Radiobutton(funcs_frame_reg, text= 'male', variable = student_gender_var, value='male', bg='#e4edc1', activebackground='#e4edc1', fg= '#185d21', font=('Arial Rounded MT Bold', 14))
male_student.place(x=660, y=260)
Label(funcs_frame_reg, text= 'Field:', bg='#e4edc1', fg= '#185d21', font=('Arial Rounded MT Bold', 14)).place(x=0, y=400)
student_field = ttk.Entry(funcs_frame_reg, width=12)
student_field.place(x=60, y=404)
student_grade_var = StringVar()
Label(funcs_frame_reg, text= 'Grade:', bg='#e4edc1', fg= '#185d21', font=('Arial Rounded MT Bold', 14)).place(x=800, y=264)
tenth_grade = Radiobutton(funcs_frame_reg, text= '10th', variable = student_grade_var, value='10th', bg='#e4edc1', activebackground='#e4edc1', fg= '#185d21', font=('Arial Rounded MT Bold', 14))
tenth_grade.place(x=875, y=264)
eleventh_grade= Radiobutton(funcs_frame_reg, text= '11th', variable = student_grade_var, value='11th', bg='#e4edc1', activebackground='#e4edc1', fg= '#185d21', font=('Arial Rounded MT Bold', 14))
eleventh_grade.place(x=950, y=264)
twelfth_grade= Radiobutton(funcs_frame_reg, text= '12th', variable = student_grade_var, value='12th', bg='#e4edc1', activebackground='#e4edc1', fg= '#185d21', font=('Arial Rounded MT Bold', 14))
twelfth_grade.place(x=1025, y=264)
Label(funcs_frame_reg, text= 'Phone Number:', bg='#e4edc1', fg= '#185d21', font=('Arial Rounded MT Bold', 14)).place(x=0, y=334)
student_phone = ttk.Entry(funcs_frame_reg, width=18)
student_phone.place(x=150, y=340)
Label(funcs_frame_reg, text= 'Address:', bg='#e4edc1', fg= '#185d21', font=('Arial Rounded MT Bold', 14)).place(x=920, y=334)
student_address = ttk.Entry(funcs_frame_reg, width=18)
student_address.place(x=1010, y=340)

Label(funcs_frame_reg, text= 'State:', bg='#e4edc1', fg= '#185d21', font=('Arial Rounded MT Bold', 14)).place(x=290, y=334)
student_state = ttk.Combobox(funcs_frame_reg, values= provinces, width=29, font=('Arial Rounded MT Bold', 8))
student_state.set('Tehran')
student_state.place(x=355, y=340)

def s_update_city_combobox(event):
    selected_state = iran[student_state.get()]
    student_city = ttk.Combobox(funcs_frame_reg, values=selected_state, width=29, font=('Arial Rounded MT Bold', 8))
    student_city.set(selected_state[0])
    student_city.place(x=660, y=340)

Label(funcs_frame_reg, text= 'City:', bg='#e4edc1', fg= '#185d21', font=('Arial Rounded MT Bold', 14)).place(x=610, y=334)
student_city = ttk.Combobox(funcs_frame_reg, values= 'Choose-your-state-first!', width=29, font=('Arial Rounded MT Bold', 8))
student_city.set('Tehran')
student_city.place(x=660, y=340)
student_state.bind("<<ComboboxSelected>>", s_update_city_combobox)

# final_sturdent_register_btn = Button(funcs_frame_reg, text='Register', bg='#2d891b', fg='white', width=22, height=3 ,font=('Arial Rounded MT Bold', 11), activebackground='#2d891b', bd=0, command= lambda:new_school.manager.register(national_id = student_nID.get(), name = student_fname.get(), 
#     last_name = student_lname.get(), gender = student_gender_var.get(), birth_date = f'{student_birth_year.get()}/{student_birth_month.get()}/{student_birth_day.get()}', address = student_address.get(), phone_number = student_phone.get(), father_name = student_father_name.get(), state = student_state.get(),
#     city = student_city.get(), grade = student_grade_var.get(), field = student_field.get(), _type = 'student'))
final_sturdent_register_btn = Button(funcs_frame_reg, text='Register', bg='#2d891b', fg='white', width=22, height=3 ,font=('Arial Rounded MT Bold', 11), activebackground='#2d891b', bd=0, command= lambda:new_school.manager.register(national_id = '0152401475', name = 'Ava', last_name = 'Mahmoudi', gender = 'female', birth_date = f'1385/09/06', address = 'Chitgar', phone_number = '09122417869', father_name = 'Ahmad', state = 'Tehran', city = 'Tehran', grade = '10th', field = 'humanities', _type = 'student', this_year_marks = "[16, 19, 8.25, 15, 20, 19]", previos_marks = "[17.75, 18.5, 20, 20, 19]"))
final_sturdent_register_btn.place(x=438, y=460)

create_class_page = Frame(pages, width= 250, height=250, background='#e4edc1')
create_class_page.pack()
pages.add(create_class_page, text="Classes Management")
funcs_frame_cls = Frame(create_class_page, bg='#e4edc1', width=1200, height=650)
funcs_frame_cls.place(x=80, y=5)

exam_construction = Frame(pages, width= 250, height=250, background='#e4edc1')
exam_construction.pack()
pages.add(exam_construction, text="Exam Construction")
funcs_frame_exam = Frame(exam_construction, bg='#e4edc1', width=1200, height=650)
funcs_frame_exam.place(x=80, y=5)


moderator_page = Frame(pages, bg= '#f5ee9e')
pages.add(moderator_page, text="Moderator")
teacher_page = Frame(pages, bg= '#DBC7C9')
pages.add(teacher_page, text="Teacher")
student_page = Frame(pages, bg= '#ffd0fe')
pages.add(student_page, text="Student")

Label(main_page, text='School Management', bg='#E0EFEA', font=('Arial Rounded MT Bold', 28), fg='#445F3B').place(x=485, y=14)

school_img = PhotoImage(file=r'images\school-icon.png')
school_icon = Button(main_page, image= school_img, bg = '#E0EFEA', bd= 0, activebackground= '#E0EFEA', command= lambda: show_page(1))
school_icon.place(x=560, y=230)

manager_img = PhotoImage(file= r'images\manager-icon.png')
manager_icon = Button(main_page, image= manager_img, bg = '#E0EFEA', bd= 0, activebackground= '#E0EFEA', command= lambda: show_page(2))
manager_icon.place(x=748, y=97)

moderator_img = PhotoImage(file= r'images\moderator-icon.png')
moderator_icon = Button(main_page, image= moderator_img, bg = '#E0EFEA', bd= 0, activebackground= '#E0EFEA', command= lambda: show_page(5))
moderator_icon.place(x=750, y=435)

teacher_img = PhotoImage(file= r'images\teachersymbol.png')
teacher_icon = Button(main_page, image= teacher_img, bg = '#E0EFEA', bd= 0, activebackground= '#E0EFEA', command= lambda: show_page(6))
teacher_icon.place(x=421, y=427)

student_img = PhotoImage(file= r'images\studentlogin.png')
student_icon = Button(main_page, image= student_img, bg = '#E0EFEA', bd= 0, activebackground= '#E0EFEA', command= lambda: show_page(7))
student_icon.place(x=426, y=97)




win.mainloop()