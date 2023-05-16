def get_num_questions():
    return int(input("أدخل عدد الأسئلة: "))
continue_execution = True
while continue_execution:
    num_questions = 0
    while (num_questions <= 0):
        num_questions = get_num_questions() 
        if (num_questions <= 0):
            print("عدد الأسئلة يجب أن يكون أكبر من الصفر. يرجى المحاولة مرة أخرى.")
    num1 = int(input("أدخل العدد الأول: "))
    num2 = int(input("أدخل العدد الثاني: "))
    result = num1 + num2
    print("الناتج: ", result)
    
    user_input = input("هل تريد مواصلة تنفيذ البرنامج؟ 'نعم' أو 'لا'.")
    continue_execution = (user_input.lower() == 'نعم')
