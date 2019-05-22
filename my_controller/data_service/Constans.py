class C:
    class Integers:
        @classmethod
        def six_lotto_max_value(cls):
            return 45

        @classmethod
        def seven_lotto_max_value(cls):
            return 35

        @classmethod
        def six_lottery_value(cls):
            return 6

        @classmethod
        def seven_lottery_value(cls):
            return 7

        @classmethod
        def min_fix_number(cls) :
            return 1

        @classmethod
        def max_fix_number(cls):
            return 4

    class Strings:
        @classmethod
        def six_lotto_type(cls) -> str:
            return '6/45'

        @classmethod
        def seven_lotto_type(cls):
            return '7/35'
