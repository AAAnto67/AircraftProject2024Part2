OEW = 19788
MTOW = 33819
RandoWeight = 29091
import XFLR5

WeightsList = [19788, 19788, 19788, 19788, 19788
               , 33819, 33819, 33819, 33819, 33819, 33819
               , 29091, 29091, 29091, 29091, 29091, 29091
               , 19788, 19788, 19788, 19788, 19788
               , 33819, 33819, 33819, 33819, 33819, 33819
               , 29091, 29091, 29091, 29091, 29091, 29091
               , 19788, 19788, 19788, 19788
               , 33819, 33819, 33819, 33819, 33819
               , 29091, 29091, 29091, 29091, 29091
               , 19788, 19788, 19788, 19788
               , 33819, 33819, 33819, 33819, 33819
               , 29091, 29091, 29091, 29091, 29091]

LoadFactorsList = [3, 2, 1, 3, 3, 3, 2, 1, 3, 3, 2.6, 3, 2, 1, 3, 3, 2.3, 3, 2, 1, 3, 3, 3, 2, 1, 3, 3, 2.6, 3, 2, 1, 3, 3, 2.3
                   , -1, -1, -1, 0, -1, -1, -1, 0, -1, -1, -1, -1, 0, -1, -1, -1, -1, 0, -1, -1, -1, 0, -1, -1, -1, -1, 0, -1]

SpeedFactorsList = [92.46, 44.66, 53.56, 122.92, 153.64
                    , 120.87, 58.39, 70.03, 127.17, 158.96, 112.04
                    , 112.11, 54.15, 64.95, 122.92, 153.64, 97.48
                    , 171.75, 82.96, 99.50, 228.33, 243.15
                    , 217.02, 104.83, 125.73, 228.33, 243.15, 201.17
                    , 201.28, 97.23, 116.61, 228.33, 243.15, 175.01
                    , 92.46, 53.56, 122.92, 153.64
                    , 120.87, 70.03, 127.17, 158.96, 112.04
                    , 112.11, 64.95, 122.92, 153.64, 97.48
                    , 171.75, 99.50, 228.33, 243.15
                    , 217.02, 125.73, 228.33, 243.15, 201.17
                    , 201.28, 116.61, 228.33, 243.15, 175.01]

DensitiesList = [1.225, 1.225, 1.225, 1.225, 1.225
                 , 1.225, 1.225, 1.225, 1.225, 1.225, 1.225
                 , 1.225, 1.225, 1.225, 1.225, 1.225, 1.225
                 , 0.38, 0.38, 0.38, 0.38, 0.38
                 , 0.38, 0.38, 0.38, 0.38, 0.38, 0.38
                 , 0.38, 0.38, 0.38, 0.38, 0.38, 0.38
                 , 1.225, 1.225, 1.225, 1.225
                 , 1.225, 1.225, 1.225, 1.225, 1.225
                 , 1.225, 1.225, 1.225, 1.225, 1.225
                 , 0.38, 0.38, 0.38, 0.38
                 , 0.38, 0.38, 0.38, 0.38, 0.38
                 , 0.38, 0.38, 0.38, 0.38, 0.38]


Va = 11
Vs0 = 23.2
Vs1 = 20
Vc = 1.63
Vd = 1.63
Vf = 20

AoAList = [Va, Vs0, Vs1, Vc, Vd
           , Va, Vs0, Vs1, Vc, Vd, Vf
           , Va, Vs0, Vs1, Vc, Vd, Vf
           , Va, Vs0, Vs1, Vc, Vd
           , Va, Vs0, Vs1, Vc, Vd, Vf
           , Va, Vs0, Vs1, Vc, Vd, Vf
           , Va, Vs1, Vc, Vd
           , Va, Vs1, Vc, Vd, Vf
           , Va, Vs1, Vc, Vd, Vf
           , Va, Vs1, Vc, Vd
           , Va, Vs1, Vc, Vd, Vf
           , Va, Vs1, Vc, Vd, Vf]

NewAoAList = [(WeightsList[i] * LoadFactorsList[i] / (0.5 * DensitiesList[i] * SpeedFactorsList[i]**2 * 75.632)) for i in range(len(WeightsList))]