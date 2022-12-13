def cough_dec(func):
    def func_wrapper():
        print("*cough*")
        func()
        print("*cough*")

    return func_wrapper


@cough_dec
def question():
    print("can i get a discount?")


@cough_dec
def answer():
    print('just 20pc mate!, and you are coughing way too much!!!')

question()
answer()