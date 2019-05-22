from my_controller.factory.MyLottoClasses import *


class LottoFactory:

    __fix_numbers:list

    def __init__(self):
        pass


    def makeFullLotto(self,lottotype:str,fix_nums:list,my_lotto_line:int) -> []:

        self.__fix_numbers=fix_nums.copy()

        result=list()

        for i in range(0,my_lotto_line):

            if lottotype==C.Strings.six_lotto_type():
                result.append(SixLottoCoupon(self.__fix_numbers))

            if lottotype==C.Strings.seven_lotto_type():
                result.append(self.__fix_numbers)

        return result


