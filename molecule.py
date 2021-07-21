#python 3.7.1
print('Please enter formula such as "H2O" or "Mg(OH)2"')
a=input("enter formula of compound  ")
#values of compounds has taken 0 to reduce chances of error
A=''
O,C,Cl,Na,H,P,Ca,S,N,K,Al,Fe,Cu,Mg=0,0,0,0,0,0,0,0,0,0,0,0,0,0
c,o,cl,na,h,p,ca,s,k,al,fe,cu,mg,n='','','','','','','','','','','','','',''
BM=''
bracketmultiplyer=1
bracketspace=0
bracketO,bracketC=len(a),len(a)
#initialisations for Number of atoms
nO,nC,nCl,nNa,nH,nP,nCa,nS,nN,nK,nAl,nFe,nCu,nMg=0,0,0,0,0,0,0,0,0,0,0,0,0,0
#for molecular mass calculations
i=0
while(i<len(a)):
        if(a[i]=='(' or a[i]=='['):
                bracketO=i
                for j in range(i,len(a)):
                        for k in range(i,bracketC):
                                if (k+1<len(a) and a[k]==')' or a[i]==']'):
                                        bracketC=k
                                        for l in range(k+1,len(a)):
                                                if (a[l].isnumeric()):
                                                        BM=BM+a[l]
                                                else:
                                                        break
                                        if (BM.isnumeric()):
                                                bracketmultiplyer=int(BM)
                                                BM=''
                        if (a[j]==')' or a[i]==']'):
                                bracketspace=bracketC-bracketO
                                i=i+bracketspace
                                bracketmultiplyer=1
                                bracketspace=0
                                bracketO,bracketC=len(a),len(a)
                                break
                        elif (a[j]=='C' and a[j+1]!='l' and a[j+1]!='a' and a[j+1]!='u'):
                                if (j+1 < len(a)):
                                        for k in range(j+1,len(a)):
                                                if (a[k].isnumeric()):
                                                        c=c+a[k]
                                                else:
                                                        break
                                if (c.isnumeric()):
                                        C=C+12*int(c)*bracketmultiplyer
                                        nC=nC+int(c)*bracketmultiplyer
                                else:
                                        C=C+12*bracketmultiplyer
                                        nC=nC+1*bracketmultiplyer
                                c=''
                        elif (a[j]=='O'):
                                if (j+1 < len(a)):
                                        for k in range(j+1,len(a)):
                                                if (a[k].isnumeric()):
                                                        o=o+a[k]
                                                else:
                                                        break
                                if (o.isnumeric()):
                                        O=O+16*int(o)*bracketmultiplyer
                                        nO=nO+int(o)*bracketmultiplyer
                                else:
                                        O=O+16*bracketmultiplyer
                                        nO=nO+1*bracketmultiplyer
                                o=''
                        elif (a[j]=='N' and a[j+1]!='a'):
                                if (j+1 < len(a)):
                                        for k in range(j+1,len(a)):
                                                if (a[k].isnumeric()):
                                                        n=n+a[k]
                                                else:
                                                        break
                                if (n.isnumeric()):
                                        N=N+14*int(n)*bracketmultiplyer
                                        nN=nN+int(n)*bracketmultiplyer
                                else:
                                        N=N+14*bracketmultiplyer
                                        nN=nN+1*bracketmultiplyer
                                n=''
                        elif (a[j]=='H'):
                                if (j+1 < len(a)):
                                        for k in range(j+1,len(a)):
                                                if (a[k].isnumeric()):
                                                        h=h+a[k]
                                                else:
                                                        break
                                if (h.isnumeric()):
                                        H=H+int(h)*bracketmultiplyer
                                        nH=nH+int(h)*bracketmultiplyer
                                else:
                                        H=H+1*bracketmultiplyer
                                        nH=nH+1*bracketmultiplyer
                                h=''
                        elif (a[j]=='C' and a[j+1]=='l'):
                                if (j+2 < len(a)):
                                        for k in range(j+2,len(a)):
                                                if (a[k].isnumeric()):
                                                        cl=cl+a[k]
                                                else:
                                                        break
                                if (cl.isnumeric()):
                                        Cl=Cl+35*int(cl)*bracketmultiplyer
                                        nCl=nCl+int(cl)*bracketmultiplyer
                                else:
                                        Cl=Cl+35*bracketmultiplyer
                                        nCl=nCl+1*bracketmultiplyer
                                cl=''
                        elif (a[j]=='N' and a[j+1]=='a'):
                                if (j+2 < len(a)):
                                        for k in range(j+2,len(a)):
                                                if (a[k].isnumeric()):
                                                        na=na+a[k]
                                                else:
                                                        break
                                if (na.isnumeric()):
                                        Na=Na+23*int(na)*bracketmultiplyer
                                        nNa=nNa+int(na)*bracketmultiplyer
                                else:
                                        Na=Na+23*bracketmultiplyer
                                        nNa=nNa+1*bracketmultiplyer
                                na=''
                        elif (a[j]=='S'):
                                if (j+1 < len(a)):
                                        for k in range(j+1,len(a)):
                                                if (a[k].isnumeric()):
                                                        s=s+a[k]
                                                else:
                                                        break
                                if (s.isnumeric()):
                                        S=S+32*int(s)*bracketmultiplyer
                                        nS=nS+int(s)*bracketmultiplyer
                                else:
                                        S=S+32*bracketmultiplyer
                                        nS=nS+1*bracketmultiplyer
                                s=''
                        elif (a[j]=='K'):
                                if (j+1 < len(a)):
                                        for k in range(j+1,len(a)):
                                                if (a[k].isnumeric()):
                                                        k=k+a[k]
                                                else:
                                                        break
                                if (k.isnumeric()):
                                        K=K+39*int(k)*bracketmultiplyer
                                        nK=nK+int(k)*bracketmultiplyer
                                else:
                                        K=K+39*bracketmultiplyer
                                        nK=nK+1*bracketmultiplyer
                                k=''
                        elif (a[j]=='P'):
                                if (j+1 < len(a)):
                                        for k in range(j+1,len(a)):
                                                if (a[k].isnumeric()):
                                                        p=p+a[k]
                                                else:
                                                        break
                                if (p.isnumeric()):
                                        P=P+31*int(p)*bracketmultiplyer
                                        nP=nP+int(p)*bracketmultiplyer
                                else:
                                        P=P+31*bracketmultiplyer
                                        nP=nP+1*bracketmultiplyer
                                p=''
                        elif (a[j]=='C' and a[j+1]=='a'):
                                if (j+2 < len(a)):
                                        for k in range(j+2,len(a)):
                                                if (a[k].isnumeric()):
                                                        ca=ca+a[k]
                                                else:
                                                        break
                                if (ca.isnumeric()):
                                        Ca=Ca+40*int(ca)*bracketmultiplyer
                                        nCa=nCa+int(ca)*bracketmultiplyer
                                else:
                                        Ca=Ca+40*bracketmultiplyer
                                        nCa=nCa+1*bracketmultiplyer
                                ca=''
                        elif (a[j]=='A' and a[j+1]=='l'):
                                if (j+2 < len(a)):
                                        for k in range(j+2,len(a)):
                                                if (a[k].isnumeric()):
                                                        al=al+a[k]
                                                else:
                                                        break
                                if (al.isnumeric()):
                                        Al=Al+27*int(al)*bracketmultiplyer
                                        nAl=nAl+int(al)*bracketmultiplyer
                                else:
                                        Al=Al+27*bracketmultiplyer
                                        nAl=nAl+1*bracketmultiplyer
                                al=''
                        elif (a[j]=='F' and a[j+1]=='e'):
                                if (j+2 < len(a)):
                                        for k in range(j+2,len(a)):
                                                if (a[k].isnumeric()):
                                                        fe=fe+a[k]
                                                else:
                                                        break
                                if (fe.isnumeric()):
                                        Fe=Fe+56*int(fe)*bracketmultiplyer
                                        nFe=nFe+int(fe)*bracketmultiplyer
                                else:
                                        Fe=Fe+56*bracketmultiplyer
                                        nFe=nFe+1*bracketmultiplyer
                                fe=''
                        elif (a[j]=='C' and a[j+1]=='u'):
                                if (j+2 < len(a)):
                                        for k in range(j+2,len(a)):
                                                if (a[k].isnumeric()):
                                                        cu=cu+a[k]
                                                else:
                                                        break
                                if (cu.isnumeric()):
                                        Cu=Cu+63*int(cu)*bracketmultiplyer
                                        nCu=nCu+int(cu)*bracketmultiplyer
                                else:
                                        Cu=Cu+63*bracketmultiplyer
                                        nCu=nCu+1*bracketmultiplyer
                                cu=''
                        elif (a[j]=='M' and a[j+1]=='g'):
                                if (j+2 < len(a)):
                                        for k in range(j+2,len(a)):
                                                if (a[k].isnumeric()):
                                                        mg=mg+a[k]
                                                else:
                                                        break
                                if (mg.isnumeric()):
                                        Mg=Mg+24*int(mg)*bracketmultiplyer
                                        nMg=nMg+int(mg)*bracketmultiplyer
                                else:
                                        Mg=Mg+24*bracketmultiplyer
                                        nMgnMg+1*bracketmultiplyer
                                mg=''
#Main calculations
        elif (a[i]=='C' and a[i+1]!='l' and a[i+1]!='a' and a[i+1]!='u'):
                if (i+1 < len(a)):
                        for j in range(i+1,len(a)):
                                if (a[j].isnumeric()):
                                        c=c+a[j]
                                else:
                                        break
                if (c.isnumeric()):
                        C=C+12*int(c)
                        nC=nC+int(c)
                else:
                        C=C+12
                        nC=nC+1
                c=''
        elif (a[i]=='O'):
                if (i+1 < len(a)):
                        for j in range(i+1,len(a)):
                                if (a[j].isnumeric()):
                                        o=o+a[j]
                                else:
                                        break
                if (o.isnumeric()):
                        O=O+16*int(o)
                        nO=nO+int(o)
                else:
                        O=O+16
                        nO=nO+1
                o=''
        elif (a[i]=='N' and a[i+1]!='a'):
                if (i+1 < len(a)):
                        for j in range(i+1,len(a)):
                                if (a[j].isnumeric()):
                                        n=n+a[j]
                                else:
                                        break
                if (n.isnumeric()):
                        N=N+14*int(n)
                        nN=nN+int(n)
                else:
                        N=N+14
                        nN=nN+1
                n=''
        elif (a[i]=='H'):
                if (i+1 < len(a)):
                        for j in range(i+1,len(a)):
                                if (a[j].isnumeric()):
                                        h=h+a[j]
                                else:
                                        break
                if (h.isnumeric()):
                        H=H+int(h)
                        nH=nH+int(h)
                else:
                        H=H+1
                        nH=nH+1
                h=''
        elif (a[i]=='C' and a[i+1]=='l'):
                if (i+2 < len(a)):
                        for j in range(i+2,len(a)):
                                if (a[j].isnumeric()):
                                        cl=cl+a[j]
                                else:
                                        break
                if (cl.isnumeric()):
                        Cl=Cl+35*int(cl)
                        nCl=nCl+int(cl)
                else:
                        Cl=Cl+35
                        nCl=nCl+1
                cl=''
        elif (a[i]=='N' and a[i+1]=='a'):
                if (i+2 < len(a)):
                        for j in range(i+2,len(a)):
                                if (a[j].isnumeric()):
                                        na=na+a[j]
                                else:
                                        break
                if (na.isnumeric()):
                        Na=Na+23*int(na)
                        nNa=nNa+int(na)
                else:
                        Na=Na+23
                        nNa=nNa+1
                na=''
        elif (a[i]=='S'):
                if (i+1 < len(a)):
                        for j in range(i+1,len(a)):
                                if (a[j].isnumeric()):
                                        s=s+a[j]
                                else:
                                        break
                if (s.isnumeric()):
                        S=S+32*int(s)
                        nS=nS+int(s)
                else:
                        S=S+32
                        nS=nS+1
                s=''
        elif (a[i]=='K'):
                if (i+1 < len(a)):
                        for j in range(i+1,len(a)):
                                if (a[j].isnumeric()):
                                        k=k+a[j]
                                else:
                                        break
                if (k.isnumeric()):
                        K=K+39*int(k)
                        nK=nK+int(k)
                else:
                        K=K+39
                        nK=nK+1
                k=''
        elif (a[i]=='P'):
                if (i+1 < len(a)):
                        for j in range(i+1,len(a)):
                                if (a[j].isnumeric()):
                                        p=p+a[j]
                                else:
                                        break
                if (p.isnumeric()):
                        P=P+31*int(p)
                        nP=nP+int(p)
                else:
                        P=P+31
                        nP=nP+1
                p=''
        elif (a[i]=='C' and a[i+1]=='a'):
                if (i+2 < len(a)):
                        for j in range(i+2,len(a)):
                                if (a[j].isnumeric()):
                                        ca=ca+a[j]
                                else:
                                        break
                if (ca.isnumeric()):
                        Ca=Ca+40*int(ca)
                        nCa=nCa+int(ca)
                else:
                        Ca=Ca+40
                        nCa=nCa+1
                ca=''
        elif (a[i]=='A' and a[i+1]=='l'):
                if (i+2 < len(a)):
                        for j in range(i+2,len(a)):
                                if (a[j].isnumeric()):
                                        al=al+a[j]
                                else:
                                        break
                if (al.isnumeric()):
                        Al=Al+27*int(al)
                        nAl=nAl+int(al)
                else:
                        Al=Al+27
                        nAl=nAl+1
                al=''
        elif (a[i]=='F' and a[i+1]=='e'):
                if (i+2 < len(a)):
                        for j in range(i+2,len(a)):
                                if (a[j].isnumeric()):
                                        fe=fe+a[j]
                                else:
                                        break
                if (fe.isnumeric()):
                        Fe=Fe+56*int(fe)
                        nFe=nFe+int(fe)
                else:
                        Fe=Fe+56
                        nFe=nFe+1
                fe=''
        elif (a[i]=='C' and a[i+1]=='u'):
                if (i+2 < len(a)):
                        for j in range(i+2,len(a)):
                                if (a[j].isnumeric()):
                                        cu=cu+a[j]
                                else:
                                        break
                if (cu.isnumeric()):
                        Cu=Cu+63*int(cu)
                        nCu=nCu+int(cu)
                else:
                        Cu=Cu+63
                        nCu=nCu+1
                cu=''
        elif (a[i]=='M' and a[i+1]=='g'):
                if (i+2 < len(a)):
                        for j in range(i+2,len(a)):
                                if (a[j].isnumeric()):
                                        mg=mg+a[j]
                                else:
                                        break
                if (mg.isnumeric()):
                        Mg=Mg+24*int(mg)
                        nMg=nMg+int(mg)
                else:
                        Mg=Mg+24
                        nMg=nMg+1
                mg=''
        i=i+1
print ('mass of compound= ',Na+C+Cl+O+S+K+P+Ca+H+Al+Fe+Cu+N+Mg,"gm/mol")
b=Na+C+Cl+O+S+K+H+P+Ca+Al+Fe+Cu+N+Mg

print('\nMOlecular Formula')
#print for MOlecular Formula
if (nK>0):
        print('K'+str(nK),end='')
        A=A+'K'+str(nK)
if (nNa>0):
        print('Na'+str(nNa),end='')
        A=A+'Na'+str(nNa)
if (nCa>0):
        print('Ca'+str(nCa),end='')
        A=A+'Ca'+str(nCa)
if (nMg>0):
        print('Mg'+str(nMg),end='')
        A=A+'Mg'+str(nMg)
if (nAl>0):
        print('Al'+str(nAl),end='')
        A=A+'Al'+str(nAl)
if (nFe>0):
        print('Fe'+str(nFe),end='')
        A=A+'Fe'+str(nFe)
if (nCu>0):
        print('Cu'+str(nCu),end='')
        A=A+'Cu'+str(nCu)
if (nC>0):
        print('C'+str(nC),end='')
        A=A+'C'+str(nC)
if (nH>0):
        print('H'+str(nH),end='')
        A=A+'H'+str(nH)
if (nP>0):
        print('P'+str(nP),end='')
        A=A+'P'+str(nP)
if (nS>0):
        print('S'+str(nS),end='')
        A=A+'S'+str(nS)
if (nN>0):
        print('N'+str(nN),end='')
        A=A+'N'+str(nN)
if (nCl>0):
        print('Cl'+str(nCl),end='')
        A=A+'Cl'+str(nCl)
if (nO>0):
        print('O'+str(nO),end='')
        A=A+'O'+str(nO)
print()
print('\nAtomacity')
for i in range(0,len(A)):
        if (A[i]=='K'):
                print ('K  ───>',nK)
        elif (A[i]=='N' and A[i+1]=='a'):
                print ('Na ───>',nNa)
        elif (A[i]=='C' and A[i+1]=='a'):
                print ('Ca ───>',nCa)
        elif (A[i]=='M' and A[i+1]=='g'):
                print ('Mg ───>',nMg)
        elif (A[i]=='A' and A[i+1]=='l'):
                print ('Al ───>',nAl)
        elif (A[i]=='F' and A[i+1]=='e'):
                print ('Fe ───>',nFe)
        elif (A[i]=='C' and A[i+1]=='u'):
                print ('Cu ───>',nCu)
        elif (A[i]=='C' and A[i+1]!='a' and A[i+1]!='u' and A[i+1]!='l'):
                print ('C  ───>',nC)
        elif (A[i]=='H'):
                print ('H  ───>',nH)
        elif (A[i]=='P'):
                print ('P  ───>',nP)
        elif (A[i]=='S'):
                print ('S  ───>',nS)
        elif (A[i]=='N' and A[i+1]!='a'):
                print ('N  ───>',nN)
        elif (A[i]=='C' and A[i+1]=='l'):
                print ('Cl ───>',nCl)
        elif (A[i]=='O'):
                print ('O  ───>',nO)
#mass percent calculations
print ('\npersentage by mass')
for j in range (0,len(A)):
        if (A[j]=='S'):
                s=(S/b)*100
        elif (A[j]=='C' and A[j+1]=='u'):
                cu=(Cu/b)*100
        elif (A[j]=='M' and A[j+1]=='g'):
                mg=(Mg/b)*100
        elif (A[j]=='N' and A[j+1]!='a'):
                n=(N/b)*100
        elif (A[j]=='C' and A[j+1]=='a'):
                ca=(Ca/b)*100   
        elif (A[j]=='C' and A[j+1]!='l'):
                c=(C/b)*100
        elif (A[j]=='O'):
                o=(O/b)*100
        elif (A[j]=='K'):
                k=(K/b)*100
        elif (A[j]=='C' and A[j+1]=='l'):
                cl=(Cl/b)*100
        elif (A[j]=='N' and A[j+1]=='a'):
                na=(Na/b)*100   
        elif (A[j]=='H'):
                h=(H/b)*100
        elif (A[j]=='P'):
                p=(P/b)*100
        elif (A[j]=='A' and A[j+1]=='l'):
                al=(Al/b)*100
        elif (A[j]=='F' and A[j+1]=='e'):
                fe=(Fe/b)*100
#print for mass percent 
for j in range(0,len(A)):
        if (A[j]=='S'):
                print ("S= ",s,"%")
        elif (A[j]=='C' and A[j+1]!='l' and A[j+1]!='a' and A[j+1]!='u'):
                print ("C= ",c,"%")
        elif (A[j]=='N' and A[j+1]!='a'):
                print ("N= ",n,"%")
        elif (A[j]=='O'):
                print ("O= ",o,"%")
        elif (A[j]=='K'):
                print ("K= ",k,"%")
        elif (A[j]=='C' and A[j+1]=='l'):
                print ("Cl= ",cl,"%")
        elif (A[j]=='N' and A[j+1]=='a'):
                print ("Na= ",na,"%")
        elif (A[j]=='C' and A[j+1]=='a'):
                print ("Ca= ",ca,"%")
        elif (A[j]=='H'):
                print ("H= ",h,"%")
        elif (A[j]=='P'):
                print ("P= ",p,"%")
        elif (A[j]=='A' and A[j+1]=='l'):
                print ("Al= ",al,"%")
        elif (A[j]=='F' and A[j+1]=='e'):
                print ("Fe= ",fe,"%")
        elif (A[j]=='C' and A[j+1]=='u'):
                print ("Cu= ",cu,"%")
        elif (A[j]=='M' and A[j+1]=='g'):
                print ("Mg= ",mg,"%")
print('\n\nBy — debasish')