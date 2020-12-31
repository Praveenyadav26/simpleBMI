

#              -------------Information about BMI Function---------------                #

def info(bmi):
    bmi = float(bmi)
    try:
        if 0 < bmi < 18.5:
            return "You Are Under Weight"
        elif 18.5 <= bmi <= 24:
            return "You Are Normal"
        elif 24 < bmi <= 29.9:
            return "You Are Over Weight"
        else:
            return "BMI is out of range"
    except:
        pass


#                     ------------Calculation of BMI Function-------------                         #
# noinspection PyBroadException
def BMI(height, weight):
    if height == "" or weight == "":
        return "Give two Value"
    else:
        try:
            high = (float(height) / 100)
            f_bmi = (float(weight) / (high * high))
            bmi = float("%.2f" % f_bmi)
            return bmi
        except:
            pass
