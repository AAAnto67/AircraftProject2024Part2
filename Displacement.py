import Momentdiagram
import numpy as np

def CalcDisplace(I_root, weight, V, Rho, AoA):

    M_list, V_list, halfspan, y_list, dy = Momentdiagram.moment(weight, V, Rho, AoA)
    lamb = 0.316
    E = 70E9

    def I(y):
        I = I_root * (1-y*((1-lamb)/(halfspan)))**4 ###################
        return(I)



    angle_list = []
    displacement_list = []
    angle = 0

    for M, y in zip(M_list, y_list):
        angle_list.append(angle)
        angle += 1/(E*I(y)) * -M * dy
        
    displacement = 0
    for angle in angle_list:
        displacement_list.append(displacement)
        displacement += angle * dy

    return(displacement_list, V_list)

#plt.plot(y_list, displacement_list)
#plt.show()