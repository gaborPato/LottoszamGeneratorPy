from exception.MyException import *

from my_controller.factory.MyLottoClasses import *


class CheckDataIntegrity(ABC):

    __result_list:list

    @classmethod
    def chk_lotto_type(cls, ltype):
        if (ltype == C.Strings.six_lotto_type()
                or ltype == C.Strings.seven_lotto_type()):

            return

        raise NoCorrectCouponType

    @classmethod
    def chk_fix_numbers(cls, input_fix_numbers: str, lotto_type) -> list:

        fix_number_list = input_fix_numbers.split(',')
        if len(fix_number_list) not in range(C.Integers.min_fix_number(), C.Integers.max_fix_number() + 1) or \
                fix_number_list[0] == '':
            raise NoCorrectFixNumberValue
        cls.__convert_str_to_intarray(fix_number_list,lotto_type)
        return cls.__result_list

    @classmethod
    def __convert_str_to_intarray(cls, fix_numbers,lotto_type):
        result_fix_numbers = []
        try:
            for num_str in fix_numbers:
                result_fix_numbers.append(int(num_str))
            cls.__check_fix_numbers_intarray(result_fix_numbers,lotto_type)

        except ValueError:
            raise CustomValueError

    @classmethod
    def __check_fix_numbers_intarray(cls, fix_numbers: list,lotto_type):
        """

        :type fix_numbers: list
        """
        if lotto_type == C.Strings.six_lotto_type():
            nl = C.Integers.six_lotto_max_value()
        else:
            nl = C.Integers.seven_lotto_max_value()

        for i in fix_numbers:
            if fix_numbers.count(i) > 1:
                raise MultipleNumberError
            if i > nl or i < 1:
                raise CouponNumberLimitError

        cls.__result_list=fix_numbers.copy()
    @classmethod
    def chk_lotto_line_value(cls, lines):
        try:
            l = int(lines)
            if l < 1:
                raise TooLessLinesError
            return l
        except ValueError:
            raise CustomValueError
