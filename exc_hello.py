print "hello"
print "world"
print "hello world"

if 1 > 0 :
    print "1 is greater than 0"
else:
    print "1 is not greater than 0"

Sreeram_dob = 19790502
Madhavi_dob = 19730319
Raja_dob    = 19760419

dob_list = [Sreeram_dob, Madhavi_dob, Raja_dob]

for dob in dob_list:
    print dob

oldest = 0

for dob in dob_list:
    if oldest <= dob:
        oldest = dob

print "Oldest", oldest

