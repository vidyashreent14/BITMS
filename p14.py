def balaji(a,b):
    print("my result bank balance=",a+b)


test_dict={"fname":balaji,
           "age":50,"address":"salem"}

print("the original dictionary is :"+str(test_dict))

res=test_dict['fname'](10,20)


