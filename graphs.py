import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

def runtime_graphs():
    #RUNTIME Graphs:
    datasets_counter = [98, 546, 1585, 4460, 13238]
    runtimes_RW_only = [12.83, 15.25, 24.03, 47.39, 98.65]
    runtimes_RW_and_SY = [12.49, 18.16, 55.59, 496.27, 3951.54]
    runtimes_RW_and_SY_update = [12.19, 16.00, 39.85, 367.49, 3300]

    plt.plot(datasets_counter, runtimes_RW_only, color='red', marker='o', label="RW Only")
    plt.plot(datasets_counter, runtimes_RW_and_SY, color='blue', marker='o', label="RW+SY - Original")
    plt.plot(datasets_counter, runtimes_RW_and_SY_update, color='black', marker='o', label="RW+SY - Optimised")
    plt.title('RW vs RW+SY (Orig&Optimal) Runtime', fontsize=14)
    plt.xlabel('Number of objects in Datasets', fontsize=14)
    plt.ylabel('Running time (seconds)', fontsize=14)
    plt.grid(True)
    plt.show()

def main():
    oper_performed_small = np.array([307, 42, 160, 128, 129])
    oper_performed_subset1 = np.array([3558, 95, 2163, 497, 1130])
    oper_performed_subset2 = np.array([10766, 345, 18574, 4370, 9644])
    oper_performed_subset3 = np.array([26998, 1674, 221303, 53395, 133583])
    oper_performed_original = np.array([73810, 6665, 2132626, 723216, 1227771])

    oper_performed_small_updated = np.array([288, 43, 4, 130, 129])
    oper_performed_subset1_updated = np.array([3463, 96, 11, 501, 845])
    oper_performed_subset2_updated = np.array([10403, 366, 34, 4761, 8359])
    oper_performed_subset3_updated = np.array([26214, 1663, 182, 49667, 133583])
    oper_performed_original_updated = np.array([72717, 6705, 550, 705154, 1221477])

    all_oper_orig = [oper_performed_small, oper_performed_subset1, oper_performed_subset2, oper_performed_subset3,
                oper_performed_original]
    all_oper_updated = [oper_performed_small_updated, oper_performed_subset1_updated, oper_performed_subset2_updated,
                        oper_performed_subset3_updated, oper_performed_original_updated]

    mylabels = ["RW Simplifications", "SY Successful Simplifications", "SY Failed from Initial Creation",
                "SY Failed from self-intersection", "SY Failed from intersection w/ other obj"]

    #myexplode = [0.2, 0, 0, 0, 0]

    i = 1
    #PIE-CHARTS:
    #for oper in all_oper:

    #    plt.pie(oper, labels=mylabels, explode=myexplode)
        #plt.title(f'Operations For Strucutre {i}')
    #    plt.show()

    #    i+=1

    #Bar-CHARTS:
    for oper in all_oper_orig:

        plt.bar(oper, labels=mylabels, height=1) #, explode=myexplode)
        plt.title(f'Operations For Strucutre {i}')
        plt.show()

        i+=1






if __name__ == "__main__":
    #main()
    runtime_graphs()
