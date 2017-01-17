"""
© Al-Banna-Techno 2017 All CopyRight Reversed
"""
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -%(levelname)s - %(message)s')
logging.disable(logging.INFO)
class AbtNumericalSystem():
    DECINUMS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    DECINUMS_str = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    class __NSTYPE:
        Binary = 2
        Ternary = 3
        Quaternary = 4
        Quinary = 5
        Senary = 6
        Octal = 8
        Decimal = 10
        Undecimal = 11
        Duodecimal = 12
        Tridecimal = 13
        Tetradecimal = 14
        Pentadecimal = 15
        Hexadecimal = 16

    NSTYPE = __NSTYPE()

    def __init__(self, num, base=NSTYPE.Decimal,alphastart="A"):
        self.num = str(num).upper()
        self.base = base
        self.alphastart=alphastart
        self.__check()
    def __repr__(self):
        return self
    def __check(self):
        """this function will check value of bases lower than or equal 10
            , other bases will be check at  __convert_to_deci

            if a>self.base:
                raise Exception("ERROR:INPUTS LARGER THAN BASE")
        """
        if self.base<2:
            raise Exception("BASE ERROR VALUE")
        ch=self.num
        if self.num[0]=="-":
            ch=self.num[1:]
        if self.base<=10:
            for a in ch:
                s=self.DECINUMS_str[:self.base]
                if a not in s:
                    raise Exception("ERROR NUM OUT OF BASE RANGE")
                    # for ex :res=NS.autoconvert("654612381",8,10)

    def __check_int_or_not(self, num):
        if int(num) != num:
            return False
        return True

    def __reverse_bin(self, num):
        if type(num) is list:
            return num[-1:-len(num) - 1:-1]
        s_num = str(num)
        return s_num[-1:-len(s_num) - 1:-1]

    def __convert_to_deci(self, num):
        logging.info("Convert To Deci " * 4)
        logging.debug("num-a %s" % num)
        num = self.__reverse_bin(num)
        logging.debug("num-b %s" % num)
        con_num = 0
        c = 0
        alpha = False
        if self.base > 9:
            alpha = True
        for a in num:
            logging.debug("a: %s" % a)
            logging.info(a in self.DECINUMS_str)
            # stOrd=ord(self.alphastart)
            if alpha and a not in self.DECINUMS_str:
                logging.debug("a-alpha : %s" % a)
                a = ord(a) - 64 + 9
                if a>self.base:
                    raise Exception("ERROR:INPUTS LARGER THAN BASE")
                logging.debug("a-alpha-ord : %s" % a)
            res = int(a) * (self.base ** c)
            logging.debug("base %s" % self.base)
            logging.debug("C : %s" % c)
            logging.debug("res : %s" % res)
            con_num += res
            logging.debug("con_num : %s" % con_num)
            c += 1
        return (con_num)
    #err
    def __convert_from_deci(self, num, base):
        logging.info("Convert From Deci " * 4)

        logging.debug("base %s" % base)
        tn = []
        logging.debug("num %s" % num)
        dn = int(num)
        if dn==0:
            return str(0)
        lres = dn
        logging.debug("lres-st %s" % lres)
        while lres:#end when lres =0
            modres = lres % base
            lres = lres // base
            logging.debug("lres %s" % lres)
            logging.debug("modres %s" % modres)
            if modres > 9:
                modres = chr(64 + (modres - 9))
            tn.append("%s" % modres)
            logging.debug("tn %s" % tn)
        return self.__reverse_bin(tn)
        # return tn
    def tostr(self,res,lower=False):
        fres = ""
        for a in res:
            fres += a
        if lower==10:
            return fres
        if not lower:# if we remove upper user will can mix upper and lower
            return fres.upper()
        else:
            return fres.lower()
    def convert(self, to=NSTYPE.Binary):
        num = self.num
        if self.base != self.NSTYPE.Decimal:
            if self.base == self.NSTYPE.Binary:
                pass
                # num = self.__reverse_bin(self.num)
                # logging.debug("reversed %s"%num)
            num = self.__convert_to_deci(num)
            # logging.debug("to deci %s"%num)
        if to == self.NSTYPE.Decimal:
            return str(num)
        else:
            return self.__convert_from_deci(num, to)
    @staticmethod
    def autoconvert(num1,base1,base2,lower=False):
        "we use this method instead of modify all function in this class"
        num = AbtNumericalSystem(str(num1), base1)
        return num.tostr(num.convert(base2),lower)
    @staticmethod
    def internalconvert(num1,base1,base2,lower=False):
        num = AbtNumericalSystem(str(num1), base1)
        res= num.tostr(num.convert(base2),lower)
        return AbtNumericalSystem(res, base2)

class AbtArithmeticNs():
    " src https://docs.python.org/3.4/library/operator.html"
    """
                            VI
        All Operations(+ - / // % * ** !) Results
        will take the same cop of the first element
        # default of cop is base of the element
        for example :-
            a=ArithmaticNs("500",10,16)
            b=ArithmaticNs("-123",10)
            v=b**2 # result base=b.cop=10
            print("After power "*5)
            # print(v.getNum())
            x=(a/v)+b # result base :
            n=a/v: a.cop=16
            n+b : b.cop=16
        so result will always take cop of the first element on strain "serial"
    """
    def __init__(self,num,base=10,conv_output_base=999999,fract="0"):
        self.num=num
        self.base=base
        "we will remove next condition if we make our class work with negative base"
        if conv_output_base<2:
            raise Exception("ERROR INVALID BASE VALUE %s"%conv_output_base)
        if conv_output_base==999999:
            self.cob=self.base
        else:
            self.cob = conv_output_base
        self.fract=fract
        self.testclass=AbtNumericalSystem(self.num, self.base) # to check on ineer value
    def getNum(self,base=999999,lower=False):
        if base!=999999:
            return AbtNumericalSystem.autoconvert(self.num, self.base, base, lower)
        return self.num
    def getBase(self):
        return self.base
    def getNumB(self):
        return self.num,self.base
    def getFract(self):
        return self.fract
    def setFract(self,val=0):
        self.fract=val
    def getCob(self):
        return self.cob
    def setCob(self,cob):
        self.cob=cob
    def getAll(self):
        return self.num,self.base,self.cob,self.fract
    def setNumB(self,num,base=999999):
        ""
        "check"
        self.num=num
        if base!=999999:
            self.base=base

    def set_output_convert_base(self,b):
        self.cob=b
    def __check_negative(self,val):
        rs = [val, False]
        if str(val)[0]=="-":
            rs=[str(val)[1:],True]
        return rs

    def __for_all_conv(self,val,base):
        rs1 = self.__check_negative(val)
        r = AbtNumericalSystem.autoconvert(rs1[0], base, 10)
        if rs1[1] == True:
            r = "-" + r
        return r
    def __neg__(self):
        return AbtArithmeticNs("-%s" % self.num, self.base, self.cob)

    def __add__(self, other):
        r1=self.__for_all_conv(self.num,self.base)
        if type(other) == type(0) or type(other) == type(0.1):
            r2 = other
        else:
            r2 = self.__for_all_conv(other.num, other.base)
        r3=int(r1)+int(r2)
        r4=str(r3)
        if r4[0]=="-":
            r5=AbtNumericalSystem.internalconvert(r4[1:], 10, self.cob)
            return AbtArithmeticNs("-%s" % r5.num, r5.base, self.cob)
        r5=AbtNumericalSystem.internalconvert(r4, 10, self.cob)
        return AbtArithmeticNs(r5.num, r5.base, self.cob)

    def __truediv__(self, other):
        "we know that there are error with fractal"
        r1=self.__for_all_conv(self.num,self.base)
        if type(other) == type(0) or type(other) == type(0.1):
            r2 = other
        else:
            r2 = self.__for_all_conv(other.num, other.base)
        r3=int(r1)/int(r2)
        r6=int(r3)
        r4=str(r6)
        if r4[0]=="-":
            r5=AbtNumericalSystem.internalconvert(r4[1:], 10, self.cob)
            if r6!=r3:
                return AbtArithmeticNs("-%s" % r5.num, r5.base, self.cob, str(r3 - r6))
            return AbtArithmeticNs("-%s" % r5.num, r5.base, self.cob)
        r5=AbtNumericalSystem.internalconvert(r4, 10, self.cob)
        if r6 != r3:
            return AbtArithmeticNs(r5.num, r5.base, self.cob, str(r3 - r6))
        return AbtArithmeticNs(r5.num, r5.base, self.cob)

    def __mul__(self, other):
        r1=self.__for_all_conv(self.num,self.base)
        if type(other) == type(0) or type(other) == type(0.1):
            r2 = other
        else:
            r2 = self.__for_all_conv(other.num, other.base)
        r3=int(r1)*int(r2)
        r4=str(r3)
        if r4[0]=="-":
            r5=AbtNumericalSystem.internalconvert(r4[1:], 10, self.cob)
            return AbtArithmeticNs("-%s" % r5.num, r5.base, self.cob)
        r5=AbtNumericalSystem.internalconvert(r4, 10, self.cob)
        return AbtArithmeticNs(r5.num, r5.base, self.cob)
    def __floordiv__(self, other):
        "we know that there are error with fractal"
        r1=self.__for_all_conv(self.num,self.base)
        if type(other) == type(0) or type(other) == type(0.1):
            r2 = other
        else:
            r2 = self.__for_all_conv(other.num, other.base)
        r3=int(r1)//int(r2)
        r6=int(r3)
        r4=str(r6)
        if r4[0]=="-":
            r5=AbtNumericalSystem.internalconvert(r4[1:], 10, self.cob)
            if r6!=r3:
                return AbtArithmeticNs("-%s" % r5.num, r5.base, self.cob, str(r3 - r6))
            return AbtArithmeticNs("-%s" % r5.num, r5.base, self.cob)
        r5=AbtNumericalSystem.internalconvert(r4, 10, self.cob)
        if r6 != r3:
            return AbtArithmeticNs(r5.num, r5.base, self.cob, str(r3 - r6))
        return AbtArithmeticNs(r5.num, r5.base, self.cob)
    def __sub__(self, other):
        r1=self.__for_all_conv(self.num,self.base)
        if type(other) == type(0) or type(other) == type(0.1):
            r2 = other
        else:
            r2 = self.__for_all_conv(other.num, other.base)
        r3=int(r1)-int(r2)
        r4=str(r3)
        if r4[0]=="-":
            r5=AbtNumericalSystem.internalconvert(r4[1:], 10, self.cob)
            return AbtArithmeticNs("-%s" % r5.num, r5.base, self.cob)
        r5=AbtNumericalSystem.internalconvert(r4, 10, self.cob)
        return AbtArithmeticNs(r5.num, r5.base, self.cob)

    def __mod__(self, other):
        r1=self.__for_all_conv(self.num,self.base)
        if type(other) == type(0) or type(other) == type(0.1):
            r2=other
        else:
            r2=self.__for_all_conv(other.num,other.base)
        r3=int(r1)%int(r2)
        r4=str(r3)
        if r4[0]=="-":
            r5=AbtNumericalSystem.internalconvert(r4[1:], 10, self.cob)
            return AbtArithmeticNs("-%s" % r5.num, r5.base, self.cob)
        r5=AbtNumericalSystem.internalconvert(r4, 10, self.cob)
        return AbtArithmeticNs(r5.num, r5.base, self.cob)
    def __pow__(self, other, modulo=None):
        r1=self.__for_all_conv(self.num,self.base)
        if type(other) == type(0) or type(other) == type(0.1):
            r2=other
        else:
            r2=self.__for_all_conv(other.num,other.base)
        r3=int(r1)**int(r2)
        r4=str(r3)
        if r4[0]=="-":
            r5=AbtNumericalSystem.internalconvert(r4[1:], 10, self.cob)
            return AbtArithmeticNs("-%s" % r5.num, r5.base, self.cob)
        r5=AbtNumericalSystem.internalconvert(r4, 10, self.cob)
        return AbtArithmeticNs(r5.num, r5.base, self.cob)

    def __str__(self):
        return str(self.num)

    "Additional "
    def __getitem__(self):
        return self.num




