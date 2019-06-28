thh=input()
if thh==thh[::-1]:
    print("yes")
else:
    value=thh.strip("0")
    if value==value[::-1]:
        print("yes")
    else:
        value=thh.lstrip("0")
        if value==value[::-1]:
            print("yes")
        else:
            print("no")
