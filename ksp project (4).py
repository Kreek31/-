import math

G = 6.6738480*10**(-11)
PI = 3.1415926
#----------------Характеристики Кербина-------------------------------
T = 24*60*60 #Время одного оборота Кербина (сек)
M_K = 5.2915158*10**22 #Масса Кербина (кг)
R_K = 600*1000 #Радиус Кербина (м)
#Perimeter_K = 3769911 #Периметр Кербина
P_K =  2*PI*R_K#Perimeter_K #Периметр Кербина
BPO_K = 13599840256 #Большая полуось Кербина
SIDER_K = 9203545 #Сидерический период Кербина

#----------------Характеристики Дюны --------------------------------
M_D = 4.515427*10**21
R_D = 320000
P_D = 2*PI*R_D
BPO_D = 20726155264 #Большая полуось Дюны
SIDER_D = 17315400 #Сидерический период Дюны
SR_R_D = 20726155264
SR_V_ANGLE_D = 360/SIDER_D

#---------------Характеристики Аппарата------------------------------
M_SHIP_S1 = 99*1000 #Начальная масса ракеты (кг)
M_SHIP_S2 = 15560
V_ANGLE = P_K/T
V1_K = 2*PI*P_K*(V_ANGLE/360)

#----------------------------------Михаил-----------------------------------------------

def gravity_force (m1, m2, r):
    global G
    return m1*m2*G/(r*r)
def first_cosmic_speed (m1, r):
    global G
    return (G*m1/r)**(1/2)
def second_cosmic_speed (m1, r):
    global G
    return (2*G*m1/r)**(1/2)
def centrifugal_force(m, v, r):
    return m*v*v/r
def ecscentrisitet(peri, apo, r): # peri - перицентр; apo - апоцентр; r - радиус косм. тела, находящегося в фокусе
    peri += r
    apo += r
    a = (peri+apo)/2
    c = a-peri
    return c/a
def Kepler(e, t):
    global PI
    global SR_V_ANGLE_D
    M = t * SR_V_ANGLE_D * PI / 180
    m = M//(2*PI)
    if abs((M//(2*PI))-(3*PI))<abs((M//(2*PI))-PI):
        m += 1
    if PI*(m+1) <= M:
        x = max(PI*(m+1), M - e)
    if PI*(m+1) >= M:
        x = min(PI * (m + 1), M + e)
    for i in range(0, 50):
        x = x - ((x - e*math.sin(x) - M)/1-e*math.cos(x))
    v = 2*math.atan((((1+e)/(1-e))**(1/2))*math.tan(x/2))
    return (v * 180 / PI)


#--------------------------------------Руслан-----------------------------------------------

atm = 101325    #Паскаль
orbit = 54000   #Высота, на которой находится орбита (м)
s = PI*2400**2/4 #Характерная площадь ракеты

def resistance(cx,altitude,velocity,s):
    return cx*density(altitude)*velocity**2*s/2 # сx - коэфициент лобового сопротивления от числа маха, v - скорость ракеты, s - характерная площадь ракеты (см)

def density(altitude):  #плотность атмосферного давления
    return atm*math.e**(-1*altitude/5000)

def Mach(v, vs):
    return v/vs # v - скорость среды, vs - скорость звука

def velocity(I, M_SHIP, M_SHIP1):
    return I * math.log(M_SHIP/M_SHIP1) #M_SHIP1 - масса без топлива

vel_st1 = velocity(226,99000,66900)
vel_st2 = velocity(295,59900,54200)
vel_st3 = velocity(284,48400,16600)

vel_overall = vel_st1 + vel_st2 + vel_st3

print(f"\n\nСкорость 1-й ступени = {vel_st1} м/с\nСкорость 2-й ступени = {vel_st2} м/с\nСкорость 3-й ступени = {vel_st3} м/с")
print(f"Общая скорость = {vel_overall} м/с\n\n")

print(f'При такой скорости ракета выйдет на орбиту Кербина через {orbit/vel_overall} секунд после старта\n\n')

m = Mach(vel_overall,331) # cx ~ 0.3
cx = 0.3 

print(f'Число Маха, при общ.скорости ракеты = {vel_overall}, равняется {m}.\nКоэффициент лобового сопротивления ~ {cx}\n\n')


for h in range(0,orbit,5000):
    print(resistance(0.3,h,vel_overall,s))

print('\n\n',Kepler(0.051, 17315400*10))



