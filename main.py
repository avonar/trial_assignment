from tkinter import *  #NOSONAR
from app.calculation import PriceCalculator


# Main class
class Application:
    # Constructor
    def __init__(self, master):
        price = StringVar()
        sku_count = StringVar()
        state_code = StringVar()
        cvt_to = StringVar()

        def calculate_full_price():
            price_val = int(price.get())
            state_code_val = state_code.get()
            sku_count_val = int(sku_count.get())
            price_with_discount, total_price = PriceCalculator(state_code_val, price_val, sku_count_val).calculate()
            print(price_with_discount, total_price)
            if not price_with_discount and not total_price:
                cvt_to.set('Wrond data.')
                return
            if price_with_discount < price_val * sku_count_val or total_price < price_val * sku_count_val:
                cvt_to.set(
                    f'Something going wrong. price_with_discount: {price_with_discount}, total_price:{total_price}')
                return
            cvt_to.set(f'price_with_discount: {price_with_discount}, total_price:{total_price}')

        f_top = Frame(master)
        f_bot = Frame(master)
        f_bot2 = Frame(master)
        f_top.pack()
        f_bot.pack()
        f_bot2.pack()

        # Label to display instructions
        one_price = Label(f_top, text='Enter price', font='freesansbold')
        one_price.pack(side=TOP)

        one_sku_count = Label(f_bot, text='Enter sku count', font='freesansbold')
        one_sku_count.pack(side=TOP)

        one_state_code = Label(f_bot2, text='Enter state code', font='freesansbold')
        one_state_code.pack(side=TOP)

        two_price = Entry(f_top, textvariable=price, relief='sunken', justify=LEFT, width=30, font=14)
        two_price.pack()

        two_sku_count = Entry(f_bot, textvariable=sku_count, relief='sunken', justify=LEFT, width=30, font=14)
        two_sku_count.pack()

        two_state_code = Entry(f_bot2, textvariable=state_code, relief='sunken', justify=LEFT, width=30, font=14)
        two_state_code.pack()

        # Button to Calculate Full Wave Length in Meters
        btn_one = Button(master,
                         bg='Blue',
                         text='CALCULATE',
                         font='freesansbold',
                         fg='Blue',
                         command=calculate_full_price)
        btn_one.pack(fill=X)

        # Label to display the results of the calculation
        lbl_result = Label(master, textvariable=cvt_to, relief='flat', bg='Grey', font='freesansbold', fg='Blue')
        lbl_result.pack(fill=BOTH, expand=1)

        # The exit Button
        btn_exit = Button(master, text='Exit')
        btn_exit.pack(side=BOTTOM, fill=X)


root = Tk()
app = Application(root)
root.title('Antenna Wavelength Calculator')
root.minsize(450, 450)

root.mainloop()
