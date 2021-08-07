import re

f = open('input.txt', 'r')
ls = [line for line in f.read().split('\n\n')]
ls = [line.replace('\n', ' ') for line in ls]
passport = []

for line in ls:
    line = line.split(' ')
    temp_dict = {}
    for pair in line:
        if pair != '':
            key, value = pair.split(':')
            temp_dict[key] = value
    passport.append(temp_dict)

req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl',
              'ecl', 'pid']

valid_counter = 0


def valid_byr(byr):
    if len(byr) == 4 and 1920 <= int(byr) <= 2002:
        return True
    else:
        return False


def valid_iyr(iyr):
    if len(iyr) == 4 and 2010 <= int(iyr) <= 2020:
        return True
    else:
        return False


def valid_eyr(eyr):
    if len(eyr) == 4 and 2020 <= int(eyr) <= 2030:
        return True
    else:
        return False


def valid_hgt(hgt):
    if hgt[-2:] == 'cm' and 150 <= int(hgt[:-2]) <= 193:
        return True
    elif hgt[-2:] == 'in' and 59 <= int(hgt[:-2]) <= 76:
        return True
    else:
        return False


def valid_hcl(hcl):
    if hcl[0] == '#' and re.search(r'^[a-f0-9]*$', hcl[1:]):
        return True
    else:
        return False


def valid_ecl(ecl):
    valids = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if ecl in valids:
        return True
    else:
        return False


def valid_pid(pid):
    if len(pid) == 9 and pid.isdecimal():
        return True
    else:
        return False


for item in passport:
    functions = [valid_ecl, valid_byr, valid_eyr, 
                valid_hcl, valid_hgt, valid_iyr, 
                valid_pid]
    key_in_passport = [key in item for key in req_fields]
    if all(key_in_passport):
        valid_fields = [False]*7
        tests_passed =[test(item[(test.__name__)[-3:]]) for test in functions]
        if all(tests_passed):
            valid_counter+=1
                



print(valid_counter)