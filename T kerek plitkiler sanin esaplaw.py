cnt=1
while cnt > 0:
    print(cnt,")")
    jerdin_uzinligi = int(input('jerdin uzinligi='))
    jerdin_eni = int(input('jerdin eni='))
    plitkanin_uzinligi = int(input('plitkinin uzinligi='))
    plitkanin_eni = int(input('plikinin eni='))

    vq = jerdin_uzinligi // plitkanin_uzinligi
    va = jerdin_uzinligi % plitkanin_uzinligi
    
    if va > 0:
        vq=vq+1
    gq = jerdin_eni // plitkanin_eni
    ga = jerdin_eni % plitkanin_eni
    
    if ga > 0:
        gq = gq+1
    ps = gq * vq
    print("kerek plitkiler sani=",ps,"\n")
    cnt=cnt+1
