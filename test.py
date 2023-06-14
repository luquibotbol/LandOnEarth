import time
import pandas


csv1 = "austinexp.csv"
df = pandas.read_csv(csv1)
for x in range(len(df.index)-3, len(df.index)-1):
    
    
    ffname = df["FIRST NAME"][x]
    print(ffname)


    llname = df["LAST NAME"][x]
    print(llname)

    pphone = df["PHONE"][x]
    print(pphone)

    eemail = df["EMAIL"][x]
    print(eemail)

    ppassword = df["PASSWORD"][x]
    print(ppassword)

    time.sleep(1)
    

    sstate = "Texas"
    print(sstate)
    time.sleep(1)

    llicense = df["LICENSE"][x]
    print(llicense)
    time.sleep(1)

    

    bbrokerName = df["BROKERAGE"][x]
    print(bbrokerName)
    time.sleep(1)

    bbrokerRec = df["BROKER"][x]
    print(bbrokerRec)
    


