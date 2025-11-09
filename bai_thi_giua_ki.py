from guizero import App, Text, PushButton
app=App(title='Đếm số bước chân', width=870, height=550,bg='lightblue')
text0=Text(app, text='',size=3)
text=Text(app, text='Mỗi bước chân\n là một bước tiến tới sức khỏe!', color="#FC6100", font='Courier new bold', size=30)
text0=Text(app, text='',size=3)
score=0
upscore=1
def click():
    global score
    score+=upscore
    text.value='Bước chân: '+str(score)
    if score==10000:
        text1.value='Chúc Mừng: Bạn đã hoàn thành mục tiêu 10.000 bước'
def click_muctieu():
    global score
    text1.value='Mục tiêu: 10.000 bước'
def click_reset():
    global score
    score-=score
    text.value='Bước chân: '+ str(score)
    text1.value=''
button1=PushButton(app, width=20, height=5, text='Mục tiêu', command=click_muctieu)
button1.bg="#FA4D1D"
button=PushButton(app, width=20, height=5, text='Thêm bước chân', command=click)
button.bg='lightgreen'
button2=PushButton(app, width=20, height=5, text='Đặt lại số bước chân', command=click_reset)
button2.bg='blue'
text0=Text(app, text='',size=3)
text=Text(app, text='Bước chân: '+ str(score), color="#FF391F", font='Courier new bold', size=35)
text1=Text(app,text='',size=23)
app.display()