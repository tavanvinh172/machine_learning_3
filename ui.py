from tkinter import ttk
from tkinter import *
from results import printResult 
from tkinter import messagebox
from data_encoder import getData1

def draw_ui(form, y_test, neuralN, regres, X_test):
    lable_infor = Label(form, text = "Nhập thông tin:", font=("Arial Bold", 10), fg="red")
    lable_infor.grid(row = 1, column = 1, padx = 30, pady = 10)

    lable_age = Label(form, text = " Tuổi:")
    lable_age.grid(row = 2, column = 1, padx = 30, pady = 10)
    textbox_age = Entry(form)
    textbox_age.grid(row = 2, column = 2)

    lable_default = Label(form, text = "Có thẻ tín dụng?")
    lable_default.grid(row = 2, column = 3, padx = 30, pady = 10)
    defaultChosen = ttk.Combobox(form, width = 20)
    defaultChosen['values'] = ('yes', 
                            'no',
                            'unknown'
                            )
    defaultChosen.grid(row = 2, column = 4)
    defaultChosen.current()

    lable_housing = Label(form, text = "Có nợ tiền nhà?")
    lable_housing.grid(row = 3, column = 3, padx = 30, pady = 10)
    housingChosen = ttk.Combobox(form, width = 20)
    housingChosen['values'] = ('yes', 
                            'no',
                            'unknown'
                            )
    housingChosen.grid(row = 3, column = 4)
    housingChosen.current()

    lable_contact = Label(form, text = "Phương thức liên lạc?")
    lable_contact.grid(row = 4, column = 3, padx = 30, pady = 10)
    contactChosen = ttk.Combobox(form, width = 20)
    contactChosen['values'] = ('cellular', 
                            'telephone',
                            'unknown'
                            )
    contactChosen.grid(row = 4, column = 4)
    contactChosen.current()

    lable_job = Label(form, text = "Công việc hiện tại:")
    lable_job.grid(row = 3, column = 1, pady = 10)
    jobChosen = ttk.Combobox(form, width = 20)
    jobChosen['values'] = ('blue-collar', 
                            'entrepreneur',
                            'retired',
                            'admin.',
                            'services',
                            'technician',
                            'self-employed',
                            'management',
                            'student',
                            'unemployed',
                            'housemaid',
                            'unknown'
                            )
    jobChosen.grid(row = 3, column = 2)
    jobChosen.current()

    lable_marital = Label(form, text = "Tình trạng hôn nhân:")
    lable_marital.grid(row = 4, column = 1,pady = 10)
    maritalChosen = ttk.Combobox(form, width = 20)
    maritalChosen['values'] = ('married', 
                            'divorced',
                            'single',
                            'unknown'
                            )
    maritalChosen.grid(row = 4, column = 2)
    maritalChosen.current()

    lable_education = Label(form, text = "Trình độ học vấn:")
    lable_education.grid(row = 5, column = 1, pady = 10)
    educationChosen = ttk.Combobox(form, width = 20)
    educationChosen['values'] = ('basic.9y', 
                            'university.degree',
                            'basic.4y',
                            'professional.course',
                            'high.school',
                            'basic.6y',
                            'unknown'
                            )
    educationChosen.grid(row = 5, column = 2)
    educationChosen.current()

    lable_loan = Label(form, text = "Khoản nợ cá nhân:")
    lable_loan.grid(row = 6, column = 1, pady = 10 )
    loanChosen = ttk.Combobox(form, width = 20)
    loanChosen['values'] = ('yes', 
                            'no',
                            'unknown'
                            )
    loanChosen.grid(row = 6, column = 2)
    loanChosen.current()
    # textbox_loan = Entry(form)
    # textbox_loan.grid(row = 6, column = 2)

    lbl1 = Label(form)
    lbl1.grid(column=1, row=8, pady = 5)
    predict_score, precision_score, recall_score, f1_score = printResult(y_test, regres.predict(X_test))
    lbl1.configure(text="Tỉ lệ dự đoán đúng của LOGISTIC REGRESSION: "+'\n'
                            + "Ty le du doan dung: %.2f" % predict_score + "\n"
                            +"Precision: %.2f" % precision_score + "\n"
                            +"Recall: %.2f" % recall_score + "\n"
                            + "F1-score: %.2f" % f1_score)
        
    lbl2 = Label(form)
    lbl2.grid(column=2, row=8)
    predict_score, precision_score, recall_score, f1_score = printResult(y_test, neuralN.predict(X_test))
    lbl2.configure(text="Tỉ lệ dự đoán đúng của NEURAL NETWORK: "+'\n'
                            + "Ty le du doan dung: %.2f" % predict_score + "\n"
                            +"Precision: %.2f" % precision_score + "\n"
                            +"Recall: %.2f" % recall_score + "\n"
                            + "F1-score: %.2f" % f1_score)
    lb_Result = Label(form, text="Kết quả dự đoán: ")
    lb_Result.grid(column=1, row=9, pady = 5)

    def predictLogisticRegression():
        age = textbox_age.get().strip()
        job = jobChosen.get().strip()
        marital = maritalChosen.get().strip()
        education = educationChosen.get().strip()
        default = defaultChosen.get().strip()
        housing = housingChosen.get().strip()
        loan = loanChosen.get().strip()
        contact = contactChosen.get().strip()
        if((age == '') or (job == '') or (education == '') or (loan == '') or (marital == '')):
            messagebox.showinfo("Thông báo", "Bạn cần nhập đầy đủ thông tin!")
        else:
            X_train = getData1(age, job, marital, education, default, housing, loan, contact)
            y_kqua = regres.predict(X_train)
            lb_logisRe.configure(text= y_kqua)
    btn_logisRe = Button(form, text = 'LOGISTIC REGRESSION', command = predictLogisticRegression)
    btn_logisRe.grid(row = 10, column = 1, pady = 10)
    lb_logisRe = Label(form, text="...")
    lb_logisRe.grid(column=2, row=10)


    def predictNeuralNetwork():
        age = textbox_age.get().strip()
        job = jobChosen.get().strip()
        marital = maritalChosen.get().strip()
        education = educationChosen.get().strip()
        default = defaultChosen.get().strip()
        housing = housingChosen.get().strip()
        loan = loanChosen.get().strip()
        contact = contactChosen.get().strip()
        if((age == '') or (job == '') or (marital == '') or (education == '') or (loan == '') or (default == '') or (housing == '') or (contact == '')):
            messagebox.showinfo("Thông báo", "Bạn cần nhập đầy đủ thông tin!")
        else:
            X_train = getData1(age, job, marital, education, default, housing, loan, contact)
            y_kqua = neuralN.predict(X_train)
            lb_neural.configure(text= y_kqua)
        
    btn_neural = Button(form, text = 'NEURAL NETWORK', command = predictNeuralNetwork)
    btn_neural.grid(row = 11, column = 1)
    lb_neural = Label(form, text="...")
    lb_neural.grid(column = 2, row = 11)