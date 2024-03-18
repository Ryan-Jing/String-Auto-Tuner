import pupc

ap = pupc.pupc(20., 20.e3, 500)

Zser = ap.fZL(2.2) + 5800.

Zshu = ap.par(ap.fZC(120.e-12 + 500.e-12), 250.e3, 250.e3, 1.e6)

res = ap.vdiv(Zser, Zshu)

ap.plres(res, 'Antigua\'s pickup')