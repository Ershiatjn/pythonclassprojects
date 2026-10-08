from persian_tools import national_id
from persian_tools import phone_number
from persian_tools.bank import card_number
from persian_tools import plate
from persian_tools import bill
from persian_tools import digits


def convert_number(value):
    return digits.convert_to_en(value)


# ---------------- کد ملی ----------------

def national_validator(national):
    national = convert_number(national)

    if national == "":
        raise ValueError("کد ملی را وارد کنید")

    if not national_id.validate(national):
        raise ValueError("کد ملی صحیح نیست")

    result = national_id.find_place(national)

    if result is None:
        raise ValueError("اطلاعات کد ملی پیدا نشد")

    return result


# ---------------- موبایل ----------------

def phone_validator(phone):
    phone = convert_number(phone)

    if phone == "":
        raise ValueError("شماره موبایل را وارد کنید")

    if not phone_number.validate(phone):
        raise ValueError("شماره موبایل صحیح نیست")

    phone = phone_number.normalize(phone)

    result = phone_number.operator_data(phone)

    if result is None:
        raise ValueError("اطلاعات شماره موبایل پیدا نشد")

    return result


# ---------------- کارت بانکی ----------------

def card_validator(card):
    card = convert_number(card)

    card = card.replace("-", "")
    card = card.replace(" ", "")

    if card == "":
        raise ValueError("شماره کارت را وارد کنید")

    if not card_number.validate(card):
        raise ValueError("شماره کارت صحیح نیست")

    result = card_number.bank_data(card)

    if result is None:
        raise ValueError("اطلاعات بانک پیدا نشد")

    return result


# ---------------- پلاک ----------------

def plate_validator(plate_number):
    plate_number = convert_number(plate_number)

    plate_number = plate_number.replace(" ", "")
    plate_number = plate_number.replace("-", "")
    plate_number = plate_number.replace("ایران", "")

    if plate_number == "":
        raise ValueError("شماره پلاک را وارد کنید")

    if not plate.is_valid(plate_number):
        raise ValueError("پلاک صحیح نیست")

    result = plate.get_info(plate_number)

    if result is None:
        raise ValueError("اطلاعات پلاک پیدا نشد")

    return result


# ---------------- قبض ----------------

def bill_validator(bill_id, payment_id):
    bill_id = convert_number(bill_id)
    payment_id = convert_number(payment_id)

    bill_id = bill_id.replace(" ", "")
    payment_id = payment_id.replace(" ", "")

    if bill_id == "":
        raise ValueError("شناسه قبض را وارد کنید")

    if payment_id == "":
        raise ValueError("شناسه پرداخت را وارد کنید")

    if not bill_id.isdigit():
        raise ValueError("شناسه قبض باید عدد باشد")

    if not payment_id.isdigit():
        raise ValueError("شناسه پرداخت باید عدد باشد")

    result = bill.get_detail(
        bill_id=int(bill_id),
        payment_id=int(payment_id)
    )

    if result is None:
        raise ValueError("اطلاعات قبض پیدا نشد")

    if not result["is_valid_bill_id"]:
        raise ValueError("شناسه قبض صحیح نیست")

    if not result["is_valid_payment_id"]:
        raise ValueError("شناسه پرداخت صحیح نیست")

    return result