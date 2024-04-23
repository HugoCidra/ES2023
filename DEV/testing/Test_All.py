import os

def run_tests():
    PATH = os.getcwd()

    if PATH.endswith("quirked-up-software"):
        PATH += "\\DEV\\testing"
        os.chdir(PATH)

    elif PATH.endswith("DEV"):
        PATH += "\\testing"
        os.chdir(PATH)
        
    REQS = os.listdir()

    for REQ in REQS:
        SUBPATH = PATH + '\\' + REQ
        if os.path.isdir(SUBPATH):
            os.chdir(SUBPATH)
            FILES = os.listdir()
            for TEST in FILES:
                if TEST.startswith("Test"):
                    os.system('python ' + TEST)
    return

if __name__ == "__main__":
    run_tests()