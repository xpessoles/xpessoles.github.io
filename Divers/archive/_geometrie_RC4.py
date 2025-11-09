from capytale.autoeval import ValidateVariables,ValidateFunction,ValidateFunctionPretty,Validate
import random as r
import math as m

## Activité 1 : Loi en trapèze
def _calcule_temps(amax : float, vmax : float, distance : float) -> (float,float,float) :
    """
    Pour une loi en trapèze de vitesse, on calcule :
       - t1, temps à partir duquel on est à vitesse constante ;
       - t2, temps à partir duquel on décélère ;
       - t3, temps à partir duquel on est à vitesse nulle.
    Entrées :
     * amax : accélération en m²/s
     * vmax : vitesse en m/s
     * distance : distance à parcourir en mm
    """
    distance = distance/1000
    amax = amax
    vmax = vmax

    # Détermination du temps pour atteindre la vitesse max
    # vmax = t1*amax
    t1 = vmax/amax

    ## On détermine la distance minimale pour réaliser un trapèze de vitesse (non demandé)
    dmin = t1*vmax

    if distance > dmin : # On a un trapèze de vitesse
        t1 = vmax/amax
        # Distance totale (aire sous le trapèze) L = ta*v + T*v
        # T : Temps à vitesse constante
        T = (distance - t1*vmax)/vmax
        t2 = T+t1
        t3 = t2+t1
    else : # On a un triangle
        T = 0
        # calcul de la vitesse atteinte va : L = ta*va et va = ta*a
        # On a L = ta*ta*a
        ta = m.sqrt(distance/amax)
        v = amax*ta
        t1 = ta
        t2 = t1
        t3 = t1+t1
    return t1, t2, t3

valeurs_q1_01 = [(1,1,5000),(10,1,500),(5,0.5,100)]

valeurs_q1_02 = [(1,1,1),(5,0.5,10)]

test_q1_01 = ValidateFunctionPretty(
    "calcule_temps",
    valeurs_q1_01,
    valid_function = _calcule_temps)

test_q1_02 = ValidateFunctionPretty(
    "calcule_temps",
    valeurs_q1_02,
    valid_function = _calcule_temps)

## Calcul de la liste des temps
def _calcule_les_t(amax,vmax,distance,dt):
    t1,t2,t3 = _calcule_temps(amax,vmax,distance)

    les_t = []
    t = 0
    while t < t3+t1 :
        les_t.append(t)
        t = t+dt
    return les_t

valeurs_q2 = [(1,1,5000,0.1),(10,1,500,0.01),(5,0.5,100,0.001)]

test_q2 = ValidateFunctionPretty(
    "calcule_les_t",
    valeurs_q2,
    valid_function = _calcule_les_t)


## Calcul des accélérations
def _calcule_les_a(amax :float, vmax :float, distance :float, les_t: [float]) -> [float] :
    t1,t2,t3 = _calcule_temps(amax,vmax,distance)
    les_a = []

    # Génération des profils
    for t in les_t :
        # Accélération constante
        if t<t1 :
            les_a.append(amax)
        # Accélération nulle
        elif t<t2 :
            les_a.append(0)
        # Accélération constante
        elif t<t3 :
            les_a.append(-amax)
        else :
            les_a.append(0)
    return les_a

valeurs_q3 = [(1,1,5000,_calcule_les_t(1,1,5000,0.1)),
              (10,1,500,_calcule_les_t(10,1,500,0.01)),
              (5,0.5,100,_calcule_les_t(5,0.5,100,0.001))]

test_q3 = ValidateFunctionPretty(
    "calcule_les_a",
    valeurs_q3,
    valid_function = _calcule_les_a)

## Intégration d'un signal
def _integre(les_t :[float], les_y :[float]) -> [float] :
    les_s = []
    s = 0
    for i in range(len(les_y)-1):
        dt = les_t[i+1]-les_t[i]
        hy = 0.5*(les_y[i+1]+les_y[i])
        s += dt*hy
        les_s.append(s)
    les_s.append(les_s[-1])
    return les_s

valeurs_q4 = [(_calcule_les_t(5,0.5,100,0.001),
               _calcule_les_a(1,1,5000,_calcule_les_t(1,1,5000,0.1))),
              (_calcule_les_t(10,1,500,0.01),
               _calcule_les_a(10,1,500,_calcule_les_t(10,1,500,0.01))),
              (_calcule_les_t(5,0.5,100,0.001),
               _calcule_les_a(5,0.5,100,_calcule_les_t(5,0.5,100,0.001)))]

test_q4 = ValidateFunctionPretty(
    "integre",
    valeurs_q4,
    valid_function = _integre)

## Enroulement des cables
def _calcule_DPhi(H,L,theta,Xm,Xhd,Ym,Yhd):
        """
        Détermination de la distance entre le point d'ancrage et le cebtre de la poulie.

        Données du mobile :
            H : hauteur du mobile (entre deux points d'ancrages de câble)
            L : largeur du mobile (entre deux points d'ancrages de câble)
        Coordonnées du mobile
            Xm,Ym : coordonnées acutelles du centre du mobile
        Coordonnées de la poulie (en haut à droite)
            Xhd,Yhd

        """
        D =   (-(L/2)*m.cos(theta)+(H/2)*m.sin(theta)-Xm+Xhd)**2
        D = D+(-(L/2)*m.sin(theta)-(H/2)*m.cos(theta)-Ym+Yhd)**2
        D = m.sqrt(D)
        num = (-(L/2)*m.sin(theta)-(H/2)*m.cos(theta)-Ym+Yhd)
        den = (-(L/2)*m.cos(theta)+(H/2)*m.sin(theta)-Xm+Xhd)
        phi = m.atan2(num,den)

        return D,phi
Xm, Ym = 0,0
valeurs_q5 = [
    (50,100,0,Xm,675,Ym,775),          # Poulie HD
    (-50,100,0,Xm,675,Ym,-175),        # Poulie BD
    (50,-100,m.pi,Xm,-175,Ym,775),     # Poulie HG
    (-50,-100,m.pi,Xm,-175,Ym,-175),   # Poulie BG
]
Xm, Ym = 100,100
valeurs_q5.extend(
[
    (50,100,0,Xm,675,Ym,775),          # Poulie HD
    (-50,100,0,Xm,675,Ym,-175),        # Poulie BD
    (50,-100,m.pi,Xm,-175,Ym,775),     # Poulie HG
    (-50,-100,m.pi,Xm,-175,Ym,-175),   # Poulie BG
])
Xm, Ym = -100,-100
valeurs_q5.extend(
[
    (50,100,0,Xm,675,Ym,775),          # Poulie HD
    (-50,100,0,Xm,675,Ym,-175),        # Poulie BD
    (50,-100,m.pi,Xm,-175,Ym,775),     # Poulie HG
    (-50,-100,m.pi,Xm,-175,Ym,-175),   # Poulie BG
])
Xm, Ym = 100,-100
valeurs_q5.extend(
[
    (50,100,0,Xm,675,Ym,775),          # Poulie HD
    (-50,100,0,Xm,675,Ym,-175),        # Poulie BD
    (50,-100,m.pi,Xm,-175,Ym,775),     # Poulie HG
    (-50,-100,m.pi,Xm,-175,Ym,-175),   # Poulie BG
])

Xm, Ym = -100,100
valeurs_q5.extend(
[
    (50,100,0,Xm,675,Ym,775),          # Poulie HD
    (-50,100,0,Xm,675,Ym,-175),        # Poulie BD
    (50,-100,m.pi,Xm,-175,Ym,775),     # Poulie HG
    (-50,-100,m.pi,Xm,-175,Ym,-175),   # Poulie BG
])
valeurs_q5

test_q5 = ValidateFunctionPretty(
    "calcule_DPhi",
    valeurs_q5,
    valid_function = _calcule_DPhi)