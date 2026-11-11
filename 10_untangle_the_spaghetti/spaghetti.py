# analysis script v3 FINAL (use this one) - regional SST trends
import numpy as np
rng=np.random.default_rng(2024)
nt=240
lat=np.arange(-89.5,90,1.0)
lon=np.arange(0.5,360,1.0)
t=np.arange(nt)
data=np.zeros((nt,180,360))
for k in range(nt):
    data[k]=20*np.cos(np.deg2rad(lat))[:,None]+3*np.cos(2*np.pi*k/12)+0.002*k*(1+np.sin(np.deg2rad(lat)))[:,None]+rng.normal(0,0.4,(180,360))
# region 1 = southern ocean
r1=np.zeros(nt)
w=np.cos(np.deg2rad(lat))
for k in range(nt):
    s=0;ws=0
    for j in range(180):
        if lat[j]>=-90 and lat[j]<-50:
            for i in range(360):
                s=s+data[k,j,i]*w[j];ws=ws+w[j]
    r1[k]=s/ws
# climatology region 1
c1=np.zeros(12)
for m in range(12):
    c1[m]=r1[m::12].mean()
a1=np.zeros(nt)
for k in range(nt):
    a1[k]=r1[k]-c1[k%12]
p1=np.polyfit(t/12,a1,1)
print("Southern Ocean trend: %.4f degC/yr"%p1[0])
print("Southern Ocean mean: %.3f"%r1.mean())
# region 2 = tropics
r2=np.zeros(nt)
for k in range(nt):
    s=0;ws=0
    for j in range(180):
        if lat[j]>=-20 and lat[j]<20:
            for i in range(360):
                s=s+data[k,j,i]*w[j];ws=ws+w[j]
    r2[k]=s/ws
c2=np.zeros(12)
for m in range(12):
    c2[m]=r2[m::12].mean()
a2=np.zeros(nt)
for k in range(nt):
    a2[k]=r2[k]-c2[k%12]
p2=np.polyfit(t/12,a2,1)
print("Tropics trend: %.4f degC/yr"%p2[0])
print("Tropics mean: %.3f"%r2.mean())
# region 3 = north atlantic (ish)
r3=np.zeros(nt)
for k in range(nt):
    s=0;ws=0
    for j in range(180):
        if lat[j]>=30 and lat[j]<65:
            for i in range(360):
                if lon[i]>=280 or lon[i]<10:
                    s=s+data[k,j,i]*w[j];ws=ws+w[j]
    r3[k]=s/ws
c3=np.zeros(12)
for m in range(12):
    c3[m]=r3[m::12].mean()
a3=np.zeros(nt)
for k in range(nt):
    a3[k]=r3[k]-c3[k%12]
p3=np.polyfit(t/12,a3,1)
print("North Atlantic trend: %.4f degC/yr"%p3[0])
print("North Atlantic mean: %.3f"%r3.mean())
# summary
x=[p1[0],p2[0],p3[0]]
print("largest trend:",["Southern Ocean","Tropics","North Atlantic"][int(np.argmax(x))])
print("mean of trends: %.4f"%(sum(x)/3))
if a1.std()>a2.std():
    print("SO more variable than tropics")
else:
    print("tropics more variable than SO")
print("done")
