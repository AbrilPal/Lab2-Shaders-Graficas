# Andrea Abril Palencia Gutierrez, 18198
# Graficas por computadora, seccion 20
# 04/08/2020

def normal_fro(norm):
    return((norm[0]**2+norm[1]**2+norm[2]**2)**(1/2))
    
def resta_lis(x0, x1, y0, y1, z0, z1):
    arr_sub = []
    arr_sub.extend((x0 - x1, y0 - y1, z0 - z1))
    return arr_sub

def division_lis_fro(norm, frobenius):
    if (frobenius==0):
        resultado=[]
        resultado.append(float('NaN'))
        resultado.append(float('NaN'))
        resultado.append(float('NaN'))
        return resultado
    else:
        resultado=[]
        resultado.append(norm[0]/ frobenius)
        resultado.append(norm[1]/ frobenius)
        resultado.append(norm[2]/ frobenius)
        return resultado

def punto(normal, lightx, lighty, lightz):
    return (normal[0]*lightx+normal[1]*lighty+normal[2]*lightz)

def baryCoords(Ax, Bx, Cx, Ay, By, Cy, Px, Py):
    # u es para la A, v es para B, w para C
    try:
        u = ( ((By - Cy)*(Px - Cx) + (Cx - Bx)*(Py - Cy) ) /
              ((By - Cy)*(Ax - Cx) + (Cx - Bx)*(Ay - Cy)) )

        v = ( ((Cy - Ay)*(Px - Cx) + (Ax - Cx)*(Py - Cy) ) /
              ((By - Cy)*(Ax - Cx) + (Cx - Bx)*(Ay - Cy)) )

        w = 1 - u - v
    except:
        return -1, -1, -1

    return u, v, w

def cruz_lis(v0, v1):
    resultado=[]
    resultado.append(v0[1]*v1[2]-v1[1]*v0[2])
    resultado.append(-(v0[0]*v1[2]-v1[0]*v0[2]))
    resultado.append(v0[0]*v1[1]-v1[0]*v0[1])
    return resultado