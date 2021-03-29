CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CUDRL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'

class Color():
    CBLACK  = '\33[30m'
    CRED    = '\33[31m'
    CGREEN  = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE   = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE  = '\33[36m'
    CWHITE  = '\33[37m'

    CGREY    = '\33[90m'
    CRED2    = '\33[91m'
    CGREEN2  = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2   = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2  = '\33[96m'
    CWHITE2  = '\33[97m'

    # CBLACKBG  = '\33[40m'
    # CREDBG    = '\33[41m'
    # CGREENBG  = '\33[42m'
    # CYELLOWBG = '\33[43m'
    # CBLUEBG   = '\33[44m'
    # CVIOLETBG = '\33[45m'
    # CBEIGEBG  = '\33[46m'
    # CWHITEBG  = '\33[47m'



    # CGREYBG    = '\33[100m'
    # CREDBG2    = '\33[101m'
    # CGREENBG2  = '\33[102m'
    # CYELLOWBG2 = '\33[103m'
    # CBLUEBG2   = '\33[104m'
    # CVIOLETBG2 = '\33[105m'
    # CBEIGEBG2  = '\33[106m'
    # CWHITEBG2  = '\33[107m'


class Logger:
    def __init__(self, is_debug=False, is_verbose=False):
        self.is_debug = is_debug
        self.is_verbose = is_verbose
    
    def succeed(self, msg):
        self.myprint(msg, Color.CGREEN)

    def warn(self, msg):
        self.myprint('Warning: '+msg, Color.CYELLOW)

    def fail(self, msg):
        self.myprint(msg, Color.CRED)

    def log(self, msg):
        if self.is_verbose:
            self.myprint(msg, Color.CGREY)

    def myprint(self, msg, color=Color.CWHITE):
        print(color + msg + CEND)    