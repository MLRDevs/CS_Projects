# Alex Miller
# Age Calculator based on birthday and current date

from dateutil.relativedelta import relativedelta
from datetime import datetime
from time import strptime
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
import time

while True: # Main loop

    put_html("<p align=""left""><h4> AGE CALCULATOR</h4></p>") # put heading
    date = datetime.now().strftime("%m/%d/%Y") # get the current time
    DOB = input("", placeholder="your birthdate(mm/dd/yyyy)") # taking age from user
    try:
        val = strptime(DOB, "%m/%d/%Y") # check the formatting is right
    except:
        put_error("Alert! This is not the right format!") # if the format is not correct
        time.sleep(3)
        continue
    
    # get rid of the slashes
    in_date = DOB.split('/') 
    date = date.split('/')

    # convert to ints
    in_date = [int(i) for i in in_date]
    date = [int(i) for i in date]

    newdate = []

    # swap days with years
    in_date[0], in_date[2] = in_date[2], in_date[0]
    date[0], date[2] = date[2], date[0]


    if in_date <= date:
        now = datetime.strptime(DOB, "%m/%d/%Y")

        # display output
        popup("Your Age",
                [put_html("<h4>"f"{relativedelta(datetime.now(), now).years} Years</br> \
                {relativedelta(datetime.now(), now).months} Months</br>\
                {relativedelta(datetime.now(), now).days} Days""</h4>"), put_buttons(
                    ['Close'], onclick=lambda _: close_popup())], implicit_close = True)
    else: # if you put a year greater than the current year
        put_warning(
            f"No result found, this is {date[0]}, you can\'t be in {in_date[0]}."
        )
        time.sleep(3)

    clear()

    # calculate again
    choice = radio("Do you want to calculate again?", options=['Yes', 'No'], required=True)
    if choice.lower() == 'yes':
        continue
    else:
        clear()

        toast("Thanks a lot!")
        exit()