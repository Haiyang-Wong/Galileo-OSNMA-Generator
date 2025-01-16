

import csv


def match_first_8_chars(str1, str2):
    # first 8 bits
    first_8_str1 = str1[:8]
    first_8_str2 = str2[:8]

    # equal
    return first_8_str1 == first_8_str2



# replace tag
with open("ttv_tag2.csv", 'r', newline='') as file_v:
    file = csv.reader(file_v)
    v_tag = list(file)
with open("tttag_msg2.csv", 'r') as file_t:
    file = csv.reader(file_t)
    t_m = list(file)
with open("mack.csv", 'r') as file_m:
    file = csv.reader(file_m)
    mack = list(file)
with open("PRN_2.csv", 'r') as files:
    file = csv.reader(files)
    message = list(file)
# # All file has been processed
print(message)
len_mes = len(message)

i = 15
i_m = 5
i_t = 0

while i < 1800:

    str1 = t_m[i_m][4][2:]
    while i_t < 280:
        str2 = v_tag[i_t][0][2:]
        if match_first_8_chars(str1, str2):  # match
            str2 = v_tag[i_t][1][2:]
            str2 = bin(int(str2, 16))[2:].zfill(len(str2 * 4))
            l1 = str2[:32]
            l2 = str2[32:32 + 8]
            print(message[i][3])
            message[i][3] = bin(int(message[i][3], 16))[2:].zfill(len(message[i][3] * 4))
            message[i][3] = message[i][3][:146] + l1 + message[i][3][146 + 32:]
            message[i][3] = f"{int(message[i][3], 2):X}".zfill((len(message[i][3]) + 3) // 4)
            print(message[i][3])
            message[i + 1][3] = bin(int(message[i + 1][3], 16))[2:].zfill(len(message[i + 1][3] * 4))
            message[i + 1][3] = message[i + 1][3][:146] + l2 + message[i + 1][3][146 + 8:]
            message[i + 1][3] = f"{int(message[i + 1][3], 2):X}".zfill((len(message[i + 1][3]) + 3) // 4)
            # i_t += 1
            break
        else:
            i_t += 1
    i += 15
    i_m += 6
ss = []
with open("4.csv", 'a', newline='') as f1:
    f = csv.writer(f1)
    for row in message:
        ss.append(row[0])
        ss.append(row[1])
        ss.append(row[2])
        ss.append(row[3])
        print(row[3])
        f.writerow(ss)
        ss = []
        

# Automated calculation of tag
#todo
tag_length = 40
tesla_key = []
authentication_data = []
def authenticate(mac_function):
    computed_tag = mac_function(tesla_key, authentication_data)
    computed_tag_trunc = computed_tag[:tag_length]
    return computed_tag_trunc

