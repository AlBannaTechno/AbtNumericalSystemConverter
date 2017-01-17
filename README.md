
# AlBannaTechno Numerical System Converter v 1.0.0
Numerical System Converter with any base &amp; support Command Line Interface

This Program Provide a Class To Make Full Convert From Any Base To Any Base
The Range Of Base Is Supported By chr(n) function in python
But we Make The Range From A-Z=a-z
Because this project designed to provide numerical system converter only
But We Can Use It To Convert String as We Will Explain
We Will Work To Make String Converter Work Better But Until Now 
String Converter Will Make A-Z=a-z range for Hex Decimal Converting Purpose


## Getting Started

* This Project Can Directly Use from Command Line `StartLoop.py` File
* Also Can Use as a part of your project `Abt_ns.py` File
* Or You Can Download Pre-Built Version of This Project 
 * [win32](https://www.dropbox.com/s/qbl8rt1wdvy1w6m/AbtNSC_win32_1.0.0.zip?dl=0)

### Prerequisites
* Python 3.4
* colorama lib

### Using
To Use Command Line Interface
```
python StartLoop.py
```
It's Will Show
```
Start Al Banna Techno Numerical System Converter
AbtNSC>>>
```
We Can Define Variable Like:
```
anyName=$(numOrString,Base,BaseToUseWithOperations->default=Base);
a=$(f123ecd,16);
b=$(025471040,8);
```
To Print
```
@(a*b)
516D91B1D23A0
```
While
```
@(b*a)
50555443307221640
```
Because When we use arithmetic operations The Result Will Produce With the First Object Base 
```
AbtNSC>>>a=$(fedc2343,16);
AbtNSC>>>b=$(00100010010111010,2);
AbtNSC>>>c=a*b*87;
AbtNSC>>>@(c);
1740952DFD4122
```
We Should Know That The Result Is a Class 
so we can use GetNum(base) function with c variable
```
AbtNSC>>>@(c.getNum(2));
10111010000001001010100101101111111010100000100100010
```
If We But The Third Parameter ConBase
any operation will take the first object base(Always) ,additionally here it's will use the ConBase
Example:ConBase=2
```
AbtNSC>>>a=$(fffeec324,16,2);
AbtNSC>>>@(a*54)
110101111111111100010111010010100110011000
```
Using Automatic Converter $$(numOrStr,from,to)
```
AbtNSC>>>a=$$(ffeceddeedccc,16,8);
AbtNSC>>>@(a)
177754733573556314
```
Warn $$ Will Produce String Not Class So
```
AbtNSC>>>@(a.getNum(2))
Syntax Error
```
## Some Details
* The Base Must Be >=The maximum Base in the String
```
AbtNSC>>>@($$(1584548,8,2))
Syntax Error
```
Because 8 not in octal (0->7)
* To Execute the Statements We need to put Semicolon; ate the end of the last line
And Because We Use Python We Must Take into account Spaces
And We Can Execute Any python statement
For Example
```
a=$(1234,10,2);
b=$(3523fe,16,10);
for c in range (10):
  print(a*10)
```

###Be Warn with Next Bugs
* we can't use multiline after 'for' statement because we have some problems with get \n from command line
So 
```
for c in range (10):
  a+=b # will work 
  print(a*10) # will not Work
```
Because it's will interpret as `for a in range(10):     f+=ff   print(f)`

* When we Use Non-English Characters with CMD It's Will not Work
but Work Correctly with Linux(dis)
So we if We Need To Do This on windows we need to third-party application
or we can use it via pycharm or any third-party-apps support utf-8/16 encoding
```
AbtNSC>>>a=$(البنا,2000);
AbtNSC>>>@(a)
البنا
AbtNSC>>>@(a.getNum())
البنا
AbtNSC>>>@(a.getNum(100))
2BW^AZK
AbtNSC>>>@(a.getNum(2))
1010110011100100010111111101000100000111110010000100000
AbtNSC>>>
AbtNSC>>>@($$(1010110011100100010111111101000100000111110010000100000,2,2000))
البنا
```
But We Warn If We Use Small Base It's Will Make an Error:
```
AbtNSC>>>a=$(البنا,300,10);
AbtNSC>>>@(a.getNum(2))
Syntax Error ERROR: INPUTS LARGER THAN BASE
```
* We Must Use Ns Class Before Primitive Data Type
```
AbtNSC>>>a=$(123,15,10);
AbtNSC>>>@(a*2)
516
AbtNSC>>>@(2*a)
Syntax Error unsupported operand type(s) for *: 'int' and 'AbtArithmeticNs'
```
We Will Work On Those Bugs

### Additional
* Use
  * `^end` To:End The Program
  * `^clean`:To:Clean Screen
  * `^admin` To:Show Admin Name
  * `^help` To:Get Help
  * `#command` To: execute operation system commands
      like
      
        ```
        AbtNSC>>>#ls
        AbtNumericalSystemConverter  Abt_ns.py  Generate_pyc.py  StartLoop.py  __pycache__  build_pyc
        ```
        
* Also You Use Native 
  * AbtNumericalSystem
  * AbtArithmeticNs
Classes
If you want to Integrates them into your project

## Versioning
We use [SemVer](http://semver.org/) for versioning 

## Authors

* **Osama Al Banna** - *Initial work* - [AlBannaTechno](https://github.com/AlBannaTechno)

## License

This project is licensed under the Appache2.0 License - see the [LICENSE.md](LICENSE.md) file for details



