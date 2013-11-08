import sys

def aaah(jon, doctor):
    if len(doctor) > len(jon):
        return 'no'
    else:
        return 'go'

def main(file_to_open):
    f = open(file_to_open, "r")
    jon = f.readline()
    doctor = f.readline()
    print aaah(jon, doctor)

main(sys.argv[1])
