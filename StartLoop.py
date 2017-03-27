"""
© Al-Banna-Techno 2017 All Rights Reserved⁯
"""
from Abt_ns import AbtArithmeticNs,AbtNumericalSystem
from colorama import Fore, Back, Style
import os
from colorama import init
import re
import sys
class Cooloring():
    def __init__(self):
        self.bcolors = [
            Back.LIGHTCYAN_EX, Back.CYAN,
            Back.LIGHTYELLOW_EX, Back.YELLOW,
            Back.BLACK, Back.LIGHTBLACK_EX,
            Back.LIGHTBLUE_EX, Back.BLUE,
            Back.LIGHTGREEN_EX, Back.GREEN,
            Back.LIGHTWHITE_EX, Back.WHITE,
            Back.LIGHTRED_EX, Back.RED,
            Back.LIGHTMAGENTA_EX, Back.MAGENTA,
            Back.LIGHTYELLOW_EX, Back.YELLOW,
            Back.RESET
        ]
        self.fcolors = [
            Fore.LIGHTCYAN_EX, Fore.CYAN,
            Fore.LIGHTYELLOW_EX, Fore.YELLOW,
            Fore.BLACK, Fore.LIGHTBLACK_EX,
            Fore.LIGHTBLUE_EX, Fore.BLUE,
            Fore.LIGHTGREEN_EX, Fore.GREEN,
            Fore.LIGHTWHITE_EX, Fore.WHITE,
            Fore.LIGHTRED_EX, Fore.RED,
            Fore.LIGHTMAGENTA_EX, Fore.MAGENTA,
            Fore.LIGHTYELLOW_EX, Fore.YELLOW,
            Fore.RESET
        ]
        self.last = len(self.fcolors) - 1
class works():
    def __init__(self):
        self.toexit=False
        self.glo=globals()
        self.loc=locals()
        self.colors = Cooloring()
        
        pass
    def loop(self):
        try:
           print(self.colors.fcolors[13] + self.colors.bcolors[5] + "Start Al Banna Techno Numerical System Converter" + self.colors.fcolors[self.colors.last] + self.colors.bcolors[
               self.colors.last])
           while True:
               print(self.colors.fcolors[12] + "AbtNSC>>>" + self.colors.fcolors[14] + "", end="")
               track = True
               v = ""
               try:
                   while track:
                       v += input()
                       if ";" in v or "#" == v[0] or "^" == v[0] or "@" == v[0]:
                           track = False
               except EOFError:
                   break
               # v=input()
               v = v.replace(";", "")
               if v.lower() == "^help":
                   print(self.colors.fcolors[11] + """
                          var declare as name=$(value,base,con_base)
                              by default con_base =base
                              con_base used to select which base will number returned with at
                              math-expressions like + - * / //
                          with / operation it's probably that value not be integer
                          so the rest of value will put in var called fract
                          varName.getFract() to get the rest if is be

                          you can set or get options ad values with next functions
                          def getBase(self):
                              return self.base
                          def getNumB(self):
                              return self.num,self.base
                          def getFract(self):
                              return self.fract
                          def setFract(self,val=0):
                              self.fract=val
                          def getCob(self):
                                "get convert base : con_base"
                              return self.cob
                          def setCob(self,cob):
                              self.cob=cob
                          def getAll(self):
                              return self.num,self.base,self.cob,self.fract

#                          def set_output_convert_base(self,b):
#                              self.cob=b

                          def setNumB(self,num,base=999999):
                              "check"
                              self.num=num
                              if base!=999999:
                                  self.base=base


                          var.getNum(base): To get Var Number, by default base=the main base

                          We Also Can use :
                              $$(num,It's Base,ConvertTo(Base))
                              for example
                              >>>@($$(234fde,16,10)) :-
                              2314206

                          ^clean :
                              to clear screen
                          ^end :
                              to end program
                          ^admin:
                              to show the Programmer Name
                          #command
                          to execute command of your command line
                              for example
                              #ping -t google.com
                              #dir
                              #tree
                              #cls

                              #mkdir name
                              #clear
                              #netstat
                              ........................

                          Warn :--------:
                              you needn't to use semicolon ;
                              with "#"==v[0] or "^"==v[0] or "@"==v[0]:
                              when v is your text
                          but if you will use multi line program you must
                          write ; at the end line
                          """ + self.colors.fcolors[self.colors.last])
                   continue
               if v == "^end":
                   print("" + self.colors.fcolors[self.colors.last], end="")
                   self.toexit=True
                   """
                   we can't use any of next methods because exceptions handle
                   every thing so we can't exit
                   so we will use outer condition
                   """
                   # exit(0)
                   # os.system("exit")
                   # os.close(0)
                   # exit(-1)
                   break
               if v=="^admin":
                   print(self.colors.fcolors[6]+self.colors.bcolors[9]+"""Al Banna Techno"""+self.colors.fcolors[self.colors.last]+
                         self.colors.bcolors[self.colors.last]
                         )
                   continue
               if v == "^clean":
                   if "win" in str(sys.platform).lower():
                       os.system("cls")
                   else:
                       os.system("clear")
                   continue
               if v[0] == "#":
                   try:
                       os.system(v[1:])
                   except KeyboardInterrupt:
                       print(self.colors.fcolors[12] + "\nTO : end the main program write ^end command" + self.colors.fcolors[14] + "")
               print("" + self.colors.fcolors[8], end="")
               v = v.replace("$$(", "AbtNumericalSystem.autoconvert(")
               # v=v.replace(" ","").replace("$(","ArithmaticNs(")
               v = v.replace("$(", "AbtArithmeticNs(")
               fre = re.compile(u'AbtArithmeticNs\((\w+),')
               s = fre.findall(v)

               fre2 = re.compile(u'AbtNumericalSystem.autoconvert\((\w+),')
               s2 = fre2.findall(v)
               """
               y=$(10,10,10)
               ['10']
               y=AbtArithmeticNs("10",10,10)
               """
               for a in s2:
                   v = v.replace('AbtNumericalSystem.autoconvert(%s,' % a, 'AbtNumericalSystem.autoconvert("%s",' % a)
               for a in s:
                   v = v.replace('AbtArithmeticNs(%s,' % a, 'AbtArithmeticNs("%s",' % a)
               # print(s)
               # print(v)
               if "@(" in v[0:2]:
                   try:
                       eval("print(%s" % (v[2:]), self.glo, self.loc)
                   except Exception as e:
                       print(self.colors.fcolors[12] + "Syntax Error %s"%e + self.colors.fcolors[self.colors.last])
               else:
                   try:
                       # print(v)
                       exec(v, self.glo, self.loc)
                   except Exception as e:
                       print(self.colors.fcolors[12] + "Syntax Error %s"%e + self.colors.fcolors[self.colors.last])
               print("" + self.colors.fcolors[self.colors.last], end="")
        except KeyboardInterrupt:
           pass

c=works()
"Next Loop To Prevent Closing by Ctrl+C or x or any thing else ^end"
def main():
    while True:
        if not c.toexit:
            try:
                c.loop()
            except:
                continue
        else:
            exit(0)
if __name__=="__main__":
    main()
