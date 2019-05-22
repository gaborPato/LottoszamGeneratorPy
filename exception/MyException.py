from my_controller.factory.MyLottoClasses import *


class NoCorrectCouponType(Exception):
    message = f'*ERROR*right answer: {C.Strings.six_lotto_type()} or {C.Strings.seven_lotto_type()}'


class NoCorrectFixNumberValue(Exception):
    message = f'*ERROR*Fixed Samples Comma Separated ({C.Integers.min_fix_number()} - {C.Integers.max_fix_number()} Pieces)!!'


class CouponNumberLimitError(Exception):
    message = '*ERROR*There is no such number on the coupon'


class TooLessLinesError(Exception):
    message = '*ERROR*there must be at least 1 line'


class MultipleNumberError(Exception):
    message = '*ERROR*you replied!'


class CustomValueError(ValueError):
    message = '*ERROR*you did not write number'
