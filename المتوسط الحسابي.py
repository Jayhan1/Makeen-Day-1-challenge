continue_execution = True
while continue_execution:
    num_values = 0
    sum_values = 0
    
    while (num_values <= 0):
        num_values = int(input("أدخل عدد الأرقام المراد حساب متوسطها "))
        if (num_values <= 0):
            print("عدد الأرقام يجب أن يكون أكبر من الصفر. حاول مرة أخرى")
    
    for i in range(num_values):
        value = int(input(f"أدخل رقم {i + 1}: "))
        sum_values += value
    
    average = sum_values / num_values
    print(f"المتوسط الحسابي للأرقام المدخلة هو: {average}")
    
    user_input = input("هل تريد اكمال البرنامج؟ 'نعم' أو 'لا'.")
    continue_execution = (user_input.lower() == 'نعم')
