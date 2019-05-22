
from exception.MyException import *

from my_controller.data_service.CheckDataIntegrity import CheckDataIntegrity as cdi
from my_controller.factory.LottoFactory import LottoFactory


def lotto_type_prompt() -> str:
    while True:
        lotto_type = input(f'lotto type({C.Strings.six_lotto_type()} or {C.Strings.seven_lotto_type()}) ->')
        try:
            cdi.chk_lotto_type(lotto_type)
            return lotto_type
        except NoCorrectCouponType as error:
            print(error.message)



def fix_numbers_prompt(lotto_type):
    while True:
        input_fix_numbers = input(
            f'Fixed Samples Comma Separated ({C.Integers.min_fix_number()} - {C.Integers.max_fix_number()} Pieces):')

        try:
            result=cdi.chk_fix_numbers(input_fix_numbers, lotto_type)
            return result

        except NoCorrectFixNumberValue as err:
            print(err.message)
        except CustomValueError as err:
            print(err.message)
        except CouponNumberLimitError as err:
            print(err.message)
        except MultipleNumberError as err:
            print(err.message)



def lotto_lines_value_prompt():
    while True:
        lines = input('number of rows :')
        try:

            lines = cdi.chk_lotto_line_value(lines)

            return lines
        except CustomValueError as err:
            print(err.message)
        except TooLessLinesError as err:
            print(err.message)


def run():
    lotto_coupon_factory=LottoFactory()
    lotto_type=lotto_type_prompt()

    fix_numbers=fix_numbers_prompt(lotto_type)

    my_full_lotto_coupon = lotto_coupon_factory.makeFullLotto(lotto_type,fix_numbers,lotto_lines_value_prompt())

    for lotto in my_full_lotto_coupon:
        print(lotto.get_lotto_line())
