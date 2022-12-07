import random
cnt=1
while cnt > 0:
    print('\n',cnt,'-shi oyin')
    number = random.randint(1,100)
    print('men bir san oyladim, sen sol sandi tabiwin\' kerek')
    s=1
    san=int(input("1-shi urinis\nbir san sayla:"))
    if san!=number:
        s=s+1
        while s<8:
            if san>number:
                print('\n',s,'-shi urinis',"\nmenin sanim kishi-")
                san=int(input('basqa san saylan:'))
                s=s+1
            elif san<number:
                print('\n',s,'-shi urinis'"\nmenin sanim ulken+")
                san=int(input('basqa san saylan:'))
                s=s+1
            elif san==number:
                s=8
        if san!=number:
            print('sen taba almadin\' ha\'m oyin tawsildi')
        else:
            print("\n sen tapdin\' \n ")
    elif number == san:
        print("\n sen tapdin\' malades \n ")
    cnt=cnt+1
