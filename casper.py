import argparse
from os import system, name
import os
import sys
def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')

print ("")
A = """

                                         .,,cccd$$$$$$$$$$$ccc,
                                     ,cc$$$$$$$$$$$$$$$$$$$$$$$$$cc,
                                   ,d$$$$$$$$$$$$$$$$"J$$$$$$$$$$$$$$c,
                                 d$$$$$$$$$$$$$$$$$$,$" ,,`?$$$$$$$$$$$$L
                               ,$$$$$$$$$$$$$$$$$$$$$',J$$$$$$$$$$$$$$$$$b
                              ,$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i `$h
                              $$$$$$$$$$$$$$$$$$$$$$$$$P'  "$$$$$$$$$$$h $$
                             ;$$$$$$$$$$$$$$$$$$$$$$$$F,$$$h,?$$$$$$$$$$h$F
                             `$$$$$$$$$$$$$$$$$$$$$$$F:??$$$:)$$$$P",. $$F
                              ?$$$$$$$$$$$$$$$$$$$$$$(   `$$ J$$F"d$$F,$F
                               ?$$$$$$$$$$$$$$$$$$$$$h,  :P'J$$F  ,$F,$"
                                ?$$$$$$$$$$$$$$$$$$$$$$$ccd$$`$h, ",d$
                                 "$$$$$$$$$$$$$$$$$$$$$$$$",cdc $$$$"
                        ,uu,      `?$$$$$$$$$$$$$$$$$$$$$$$$$$$c$$$$h
                    .,d$$$$$$$cc,   `$$$$$$$$$$$$$$$$??$$$$$$$$$$$$$$$,
                  ,d$$$$$$$$$$$$$$$bcccc,,??$$$$$$ccf `"??$$$$??$$$$$$$
                 d$$$$$$$$$$$$$$$$$$$$$$$$$h`?$$$$$$h`:...  d$$$$$$$$P
                d$$$$$$$$$$$$$$$$$$$$$$$$$$$$`$$$$$$$hc,,cd$$$$$$$$P"
            =$$?$$$$$$$$P' ?$$$$$$$$$$$$$$$$$;$$$$$$$$$???????",,
               =$$$$$$F       `"?????$$$$$$$$$$$$$$$$$$$$$$$$$$$$$bc
               d$$F"?$$k ,ccc$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i
        .     ,ccc$$c`""u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P",$$$$$$$$$$$$h
     ,d$$$L  J$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" `""$$$??$$$$$$$
   ,d$$$$$$c,"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F       `?J$$$$$$$'
  ,$$$$$$$$$$h`$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F           ?$$$$$$$P""=,
 ,$$$F?$$$$$$$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F              3$$$$II"?$h,
 $$$$$`$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P"               ;$$$??$$$,"?"
 $$$$F ?$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P",z'                3$$h   ?$F
        `?$$$$$$$$$$$$$$$??$$$$$$$$$PF"',d$P"                  "?$F
           """""""         ,z$$$$$$$$$$$$$P
                          J$$$$$$$$$$$$$$F
                         ,$$$$$$$$$$$$$$F
                         :$$$$$c?$$$$PF'
                         `$$$$$$$P
                          `?$$$$F

	Casper dork Scanner code by Eno leriand
	please use -h to see help
    """
print ("")
print(A)

parser = argparse.ArgumentParser("casper.py",formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-g","--google", help="google mode", action='store_true' )
parser.add_argument("-s","--scada", help="scada mode ", action='store_true' )
parser.add_argument("-t","--tor", help="Tor mode ", action='store_true' )
parser.add_argument("-p","--proxy", help="Proxy mode ", action='store_true' )


args = parser.parse_args()

if args.google :
 clear()
 from Modes import Gmode

if args.scada :
 clear ()
 from Modes import Scada

if args.tor :
 clear ()
 from Modes import Tor
  
if args.proxy :
 clear ()
 from Modes import Proxy

