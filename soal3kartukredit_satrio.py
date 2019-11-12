import json

with open('ccNasabah.json','r') as jf:
    out = json.load(jf)

valid = []
invalid = []
for i in range(len(out)):
    nomor = out[i]['noCreditCard']
    nomor = nomor.split('-')
    nomor = ''.join(nomor)
   
    if nomor[0]=='4' and len(nomor) == 16:
            
        if ' ' in nomor:
            invalid.append(out[i])
        elif nomor[i].isalpha():
            invalid.append(out[i])
        elif '-' in nomor:
            invalid.append(out[i])
        elif '44444' in nomor:
            invalid.append(out[i])
        else: 
            valid.append(out[i])
    elif nomor[0] == '5' and len(nomor) == 16:
    
        
        if ' ' in nomor:
            invalid.append(out[i])
        elif nomor[i].isalpha():
            invalid.append(out[i])
        elif '-' in nomor:
            invalid.append(out[i])
        elif '9999' in nomor:
            invalid.append(out[i])
        else:
            valid.append(out[i])
    elif nomor[0] == '6' and len(nomor) == 16:
     
        if ' ' in nomor:
            invalid.append(out[i])
        elif nomor[i].isalpha():
            invalid.append(out[i])
        elif '-' in nomor:
            invalid.append(out[i])
        elif '61234' in nomor:
            invalid.append(out[i])
        else: 
            valid.append(out[i])
    else:
        invalid.append(out[i])

with open('ccValid.json','w') as y:
    json.dump(valid,y)
with open('ccInvalid.json','w') as yy:
    json.dump(invalid,yy)