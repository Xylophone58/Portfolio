start_int = int(input("Starting interger: "))
end_int = int(input("Ending interger: "))
step_size = int(input("Step size: "))

steps = []

if((start_int and end_int > 0 and step_size < 0) or (start_int and end_int < 0 and step_size > 0)):
    print("Invalid step size.")
else:
    if(step_size > 0):
        while(start_int < end_int):
#            steps.append(start_int)
            print(start_int," ", end = '')
            start_int += step_size
    elif(step_size < 0):
        while(start_int > end_int):
            print(start_int," ", end = '')
            start_int += step_size