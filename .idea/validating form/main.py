
from tkinter import *
from tkinter import messagebox
from module import *
from tkinter import ttk


def check_validator(option):

    match option:

        case "national":
            return national_validator(national.get())

        case "phone":
            return phone_validator(phone.get())

        case "card":
            return card_validator(card.get())

        case "plate":
            return plate_validator(plate_number.get())

        case "bill":
            return bill_validator(
                bill_id.get(),
                payment_id.get()
            )


def show_value(value):

    if value is None:
        return "ندارد"

    if value is True:
        return "بله"

    if value is False:
        return "خیر"

    if isinstance(value, list):
        return "، ".join(value)

    return str(value)


def submit_click():

    result = ""


    # کد ملی
    try:

        national_result = check_validator("national")

        result += "========== کد ملی ==========\n"
        result += f"کد منطقه: {show_value(national_result.get('code'))}\n"
        result += f"شهر: {show_value(national_result.get('city'))}\n"
        result += f"استان: {show_value(national_result.get('province'))}\n\n"

    except ValueError as e:

        result += "========== کد ملی ==========\n"
        result += f"خطا: {e}\n\n"


    # شماره موبایل
    try:

        phone_result = check_validator("phone")

        result += "========== شماره موبایل ==========\n"
        result += f"اپراتور: {show_value(phone_result.get('operator'))}\n"
        result += f"نوع سیم کارت: {show_value(phone_result.get('type'))}\n\n"

    except ValueError as e:

        result += "========== شماره موبایل ==========\n"
        result += f"خطا: {e}\n\n"


    # کارت بانکی
    try:

        card_result = check_validator("card")

        result += "========== کارت بانکی ==========\n"
        result += f"نام بانک: {show_value(card_result.get('persian_name'))}\n"
        result += f"پیش شماره کارت: {show_value(card_result.get('card_prefix'))}\n"
        result += f"کد شبا: {show_value(card_result.get('sheba_code'))}\n\n"

    except ValueError as e:

        result += "========== کارت بانکی ==========\n"
        result += f"خطا: {e}\n\n"


    # پلاک
    try:

        plate_result = check_validator("plate")

        result += "========== پلاک ==========\n"
        result += f"دسته بندی: {show_value(plate_result.get('category'))}\n"
        result += f"استان: {show_value(plate_result.get('province'))}\n"
        result += f" پلاک: {show_value(plate_result.get('template'))}\n"
        result += f"نوع وسیله: {show_value(plate_result.get('type'))}\n\n"

    except ValueError as e:

        result += "========== پلاک ==========\n"
        result += f"خطا: {e}\n\n"


    # قبض
    try:

        bill_result = check_validator("bill")

        result += "========== قبض ==========\n"
        result += f"مبلغ: {show_value(bill_result.get('amount'))}\n"
        result += f"شناسه قبض: {show_value(bill_result.get('bill_id'))}\n"
        result += f"شناسه پرداخت: {show_value(bill_result.get('payment_id'))}\n"
        result += f"نوع قبض: {show_value(bill_result.get('type'))}\n"
        result += f"بارکد: {show_value(bill_result.get('barcode'))}\n"
        result += f"شناسه قبض معتبر: {show_value(bill_result.get('is_valid_bill_id'))}\n"
        result += f"شناسه پرداخت معتبر: {show_value(bill_result.get('is_valid_payment_id'))}\n"
        result += f"قبض معتبر: {show_value(bill_result.get('is_valid'))}\n\n"

    except ValueError as e:

        result += "========== قبض ==========\n"
        result += f"خطا: {e}\n\n"


    messagebox.showinfo(
        title="نتیجه بررسی",
        message=result
    )


window = Tk()

window.title("بررسی اطلاعات")
window.geometry("380x370")
window.configure(background="lightsteelblue")


# کد ملی

Label(
    window,
    text="کد ملی:",
    bg="lightsteelblue",
    fg="black"
).place(x=315, y=20)

national = StringVar()

Entry(
    window,
    textvariable=national
).place(x=30, y=20, width=200)


# شماره موبایل

Label(
    window,
    text="شماره موبایل:",
    bg="lightsteelblue",
    fg="black"
).place(x=315, y=65)

phone = StringVar()

Entry(
    window,
    textvariable=phone
).place(x=30, y=65, width=200)


# شماره کارت

Label(
    window,
    text="شماره کارت:",
    bg="lightsteelblue",
    fg="black"
).place(x=315, y=110)

card = StringVar()

Entry(
    window,
    textvariable=card
).place(x=30, y=110, width=200)


# پلاک

Label(
    window,
    text="شماره پلاک:",
    bg="lightsteelblue",
    fg="black"
).place(x=315, y=155)

plate_number = StringVar()

Entry(
    window,
    textvariable=plate_number
).place(x=30, y=155, width=200)


# شناسه قبض

Label(
    window,
    text="شناسه قبض:",
    bg="lightsteelblue",
    fg="black"
).place(x=315, y=200)

bill_id = StringVar()

Entry(
    window,
    textvariable=bill_id
).place(x=30, y=200, width=200)


# شناسه پرداخت

Label(
    window,
    text="شناسه پرداخت:",
    bg="lightsteelblue",
    fg="black"
).place(x=315, y=245)

payment_id = StringVar()

Entry(
    window,
    textvariable=payment_id
).place(x=30, y=245, width=200)


# دکمه

Button(
    window,
    text="بررسی همه اطلاعات",
    bg="white",
    command=submit_click
).place(
    x=125,
    y=300,
    width=130,
    height=35
)


window.mainloop()

