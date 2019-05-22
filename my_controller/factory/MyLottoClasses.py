from abc import ABC
from random import randint

from my_controller.data_service.Constans import C


class Lotto(ABC):
    _lottery_number: int
    _max_number_of_coupon: int

    def __init__(self, fixnumbers: []):
        self.__number_line = self.__add_numbers_of_line(fixnumbers)

    def __add_numbers_of_line(self, fix_numbers: []):
        result = list(fix_numbers)

        i = len(fix_numbers)
        while i < self._lottery_number:
            rnd = randint(1, self._max_number_of_coupon)
            if rnd not in result:
                result.append(rnd)
                i += 1

        result.sort()
        return result

    def get_lotto_line(self):
        return self.__number_line


class SixLottoCoupon(Lotto):
    _lottery_number = C.Integers.six_lottery_value()
    _max_number_of_coupon = C.Integers.six_lotto_max_value()

    def __init__(self, fixnumbers: []):
        super().__init__(fixnumbers)


class SevenLottoCoupon(Lotto):
    _lottery_number = C.Integers.seven_lottery_value()
    _max_number_of_coupon = C.Integers.seven_lotto_max_value()

    def __init__(self, fixnumbers: []):
        super().__init__(fixnumbers)
