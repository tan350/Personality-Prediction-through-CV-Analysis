import os
import pandas as pd
import PyPDF2
import en_core_web_sm
nlp = en_core_web_sm.load()
import nltk
nltk.download()
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import tkinter.font as font
from functools import partial
from pyresparser import ResumeParser
from sklearn import datasets, linear_model 
import spacy



class train_model:
    
    def train(self):
        custom_nlp = spacy.load('en_core_web_sm')
        data =pd.read_csv('training_dataset.csv')
        array = data.values

        for i in range(len(array)):
            if array[i][0]=="Male":
                array[i][0]=1
            else:
                array[i][0]=0


        df=pd.DataFrame(array)

        maindf =df[[0,1,2,3,4,5,6]]
        mainarray=maindf.values

        temp=df[7]
        train_y =temp.values
        
        self.mul_lr = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg',max_iter =1000)
        self.mul_lr.fit(mainarray, train_y)
        
    def test(self, test_data):
        try:
            test_predict=list()
            for i in test_data:
                test_predict.append(int(i))
            y_pred = self.mul_lr.predict([test_predict])
            return y_pred
        except:
            print("All Factors For Finding Personality Not Entered!")


def check_type(data):
    if type(data)==str or type(data)==str:
        return str(data).title()
    if type(data)==list or type(data)==tuple:
        str_list=""
        for i,item in enumerate(data):
            str_list+=item+", "
        return str_list
    else:   return str(data)

def prediction_result(top, aplcnt_name, cv_path, personality_values):
    "after applying a job"
    top.withdraw()
    applicant_data={"Candidate Name":aplcnt_name.get(),  "CV Location": cv_path}
    

    
    age = personality_values[1]
    
    print("\n############# Candidate Entered Data #############\n")
    print(applicant_data, personality_values)
    
    personality = model.test(personality_values)
    print("\n############# Predicted Personality #############\n")
    print(personality)
    # # cv_path = os.path.abspath(__file__)
    # cv_path= 'C:\\Users\\tasharma\\Downloads\\Aithon Project\\resume.pdf'
    # # data = ResumeParser(cv_path).get_extracted_data()
    # data = ResumeParser(cv_path).get_extracted_data()

    resume_directory = 'C:\\Users\\tasharma\\Downloads\\Aithon Project'
    resume_filename = 'resume.pdf'
    pdf_path = 'C:\\Users\\tasharma\\Downloads\\Aithon Project\\resume.pdf'
    data = ResumeParser(pdf_path).get_extracted_data()


    
    try:
        del data['name']
        if len(data['mobile_number'])<10:
            del data['mobile_number']
    except:
        pass
    
    print("\n############# Resume Parsed Data #############\n")

    for key in data.keys():
        if data[key] is not None:
            print('{} : {}'.format(key,data[key]))
    
    result=Tk()
    result.geometry('700x550')
    result.overrideredirect(False)
    result.geometry("{0}x{1}+0+0".format(result.winfo_screenwidth(), result.winfo_screenheight()))
    result.configure(background='White')
    result.title("Predicted Personality")
    result.iconbitmap(r"C:\Users\tasharma\Downloads\Aithon Project\Predicting-personality-using-Resume-main/icon3.ico")
    
    #Title
    titleFont = font.Font(family='Arial', size=40, weight='bold')
    Label(result, text="PREDICTED PERSONALITY or CHARACTER", fg='red', bg='white', font=("Arial bload",20), pady=10, anchor=CENTER).pack(fill=BOTH)
    
    Label(result, text = str('{} : {}'.format("Name:", aplcnt_name.get())).title(), fg='black', bg='white', anchor='w').pack(fill=BOTH)
    Label(result, text = str('{} : {}'.format("Age:", age)), fg='black', bg='white', anchor='w').pack(fill=BOTH)
    for key in data.keys():
        if data[key] is not None:
            Label(result, text = str('{} : {}'.format(check_type(key.title()),check_type(data[key]))), fg='black', bg='white', anchor='w', width=60).pack(fill=BOTH)
    Label(result, text = str("perdicted personality: "+personality).title(), fg='black', bg='white', anchor='w').pack(fill=BOTH)
    
    
    terms_mean = """
    Following is the description of various personalities detected use in this system:

1. Openness: People who like to learn new things and enjoy new experiences usually score high in openness. It sometimes called "Intellect" or "Imagination," this measures your level of creativity, and your desire for knowledge and new experiences.

2. Conscientiousness: People that have a high degree of conscientiousness are reliable and prompt. If you score highly in conscientiousness, you'll
    likely be organized and thorough, and know how to make plans and follow them through. If you score low, you'll likely be lax and disorganized.

3. Extraversion: Extraversion traits include being; energetic, talkative, and assertive (sometime seen as outspoken by Introverts). Extraverts get their energy and drive from others, while introverts are self-driven get their drive from within themselves.

4. Agreeableness: These individuals are warm, friendly, compassionate and cooperative and traits include being kind, affectionate, and sympathetic. In contrast, people with lower levels may be more distant.

5. Neuroticism: Neuroticism relates to degree of negative emotions. People that score high on often experience emotional instability and negative emotions. Characteristics typically include being moody and tense.    
"""
    
    Label(result, text = terms_mean, fg='#0872B2',bg='white', anchor='w', justify=LEFT).pack(fill=BOTH)

    quitBtn = Button(result, text="  EXIT  ", bg='#10DD0C', command =lambda:  result.destroy(),width=20).pack()

    result.mainloop()



    

def perdict_person():
      
    root.withdraw()
    
    top = Toplevel()
    top.geometry('650x480')
    top.configure(bg='#ACC5F2')
    top.title("Upload Resume")
    top.iconbitmap(r"C:\Users\tasharma\Downloads\Aithon Project\Predicting-personality-using-Resume-main/icon2.ico")
    
    #Title
    titleFont = font.Font(family='Helvetica', size=20, weight='bold')
    lab=Label(top, text="ENTER YOUR DETAILS", fg='red', bg='#ACC5F2', font=('Arial bold',25), pady=10).pack(pady=20)

    #Job_Form
    job_list=('Select Job', '101-Developer at TTC', '102-Chef at Taj', '103-Professor at MIT')
    job = StringVar(top)
    job.set(job_list[0])

    l1=Label(top, text="Candidate's Name:", font=('Arial bold',12) , bg='#ACC5F2').place(x=60, y=130)
    l2=Label(top, text="Age:",font=('Arial bold',12) , bg='#ACC5F2').place(x=60, y=160)
    l3=Label(top, text="Gender:", font=('Arial bold',12) ,bg='#ACC5F2').place(x=60, y=190)
    l4=Label(top, text="Upload Resume", font=('Arial bold',12) , bg='#ACC5F2').place(x=60, y=220)
    l5=Label(top, text="How much do you like to experience new things:",font=('Arial bold',12) , bg='#ACC5F2').place(x=60, y=250)
    l6=Label(top, text="How Often do you feel Negativity:", font=('Arial bold',12) , bg='#ACC5F2').place(x=60, y=280)
    l7=Label(top, text="How organized and disciplined are you:",font=('Arial bold',12) , bg='#ACC5F2').place(x=60, y=310)
    l8=Label(top, text="How much good a team-player you are:",font=('Arial bold',12) , bg='#ACC5F2').place(x=60, y=340)
    l9=Label(top, text="Your level of sociability:", font=('Arial bold',12) ,bg='#ACC5F2').place(x=60, y=370)
    
    sName=Entry(top)
    sName.place(x=450, y=130, width=160)
    age=Entry(top)
    age.place(x=450, y=160, width=160)
    gender = IntVar()
    R1 = Radiobutton(top, text="Male", variable=gender, value=1, padx=7)
    R1.place(x=450, y=190)
    R2 = Radiobutton(top, text="Female", variable=gender, value=0, padx=3)
    R2.place(x=540, y=190)
    cv=Button(top, text="Select File", command=lambda:  OpenFile(cv))
    cv.place(x=450, y=220, width=160)
    openness=Entry(top)
    openness.insert(0,'1-10')
    openness.place(x=450, y=250, width=160)
    neuroticism=Entry(top)
    neuroticism.insert(0,'1-10')
    neuroticism.place(x=450, y=280, width=160)
    conscientiousness=Entry(top)
    conscientiousness.insert(0,'1-10')
    conscientiousness.place(x=450, y=310, width=160)
    agreeableness=Entry(top)
    agreeableness.insert(0,'1-10')
    agreeableness.place(x=450, y=340, width=160)
    extraversion=Entry(top)
    extraversion.insert(0,'1-10')
    extraversion.place(x=450, y=370, width=160)

    submitBtn=Button(top, padx=2, pady=0, text="Submit", bd=0, fg='white', bg='#08C419', font=(12))
    submitBtn.config(command=lambda: prediction_result(top,sName,loc,(gender.get(),age.get(),openness.get(),neuroticism.get(),conscientiousness.get(),agreeableness.get(),extraversion.get())))
    submitBtn.place(x=260, y=420,width=150)
    

    top.mainloop()

def OpenFile(b4):
    global loc;
    name = filedialog.askopenfilename(initialdir=r"C:\Users\tasharma\Downloads",
                            filetypes =(("PDF","*.pdf*"),('All files', '*')),
                           title = "Choose a file."
                           )
    try:
        filename=os.path.basename(name)
        loc=name
    except:
        filename=name
        loc=name
    b4.config(text=filename)
    return



if __name__ == "__main__":
    model = train_model()
    model.train()

    root = Tk()
    root.geometry('560x420')
    root.title("Home page")
    root.iconbitmap(r"C:\Users\tasharma\Downloads\Aithon Project\Predicting-personality-using-Resume-main/icon.ico")
    titleFont = font.Font(family='Helvetica', size=25, weight='bold')
    homeBtnFont = font.Font(size=12, weight='bold')
    lab=Label(root, text="WELCOME TO MY PERSONALITY \nPREDICTION SYSTEM", fg='red', font=("Arial bold",25), pady=30).pack()
   
    # description of application
    my_frame = LabelFrame(root, text="About Us:", fg="white",bg="#228E9F", padx=5, pady=5)
    my_frame.pack(pady=20)
    my_title = Label(my_frame, text="This system focuses on predicting the personality of the person using various \ninformation like age, gender etc. It also extracts necessary information from your \nresume. This project can be used in many areas that require selection of good\n candiates from a pool of applicants to save time and decrease workload.", font=("Arial", 11), bg="#92ECFA")
    my_title.pack()
    b2=Button(root, padx=4, pady=4, text="  Get Started !  ", bg='#10DD0C', fg='white', bd=1, font=homeBtnFont, command=perdict_person).pack()
    own=Label(root,text='-Made by Team : Victory',font=('Arial',12)).pack(pady=20)
    root.mainloop()