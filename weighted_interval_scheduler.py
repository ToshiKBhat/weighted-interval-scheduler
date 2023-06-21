#referred https://www.geeksforgeeks.org/weighted-job-scheduling/


class WeightedIntervalSchedule:


    def __init__(self, sch):
        """The input is a list of weighted intervals [s,f,w], where
           s,f, and w are the start time, finish time, and the weight of each interval.
 """
        self.sc = sch

    def addRow(self, row, arr, flag):
        row_txt = f'{row} \t'
        rl = ''
        if flag:
            for i in range(0,len(arr)):
                rl += f'{i}\t'
        else:
            for i in range(0,len(arr)):
                rl += f'{arr[i]}\t'
        row_final=row_txt + rl + '\n'
        return row_final

    def previousCmptbl(self, start_sorted_array, finish_sorted_array):
        # calculate prev compatible based on decreasing start time and finish time
        #initialize f and s pointers
        f,s= len(start_sorted_array) - 1, len(start_sorted_array) - 1
        previous_compatible_array=[-1]*(s+1)
        while(f>=0 and s>=0):
            # decrease f until compatible job is found, when found, decrease start.

            # decrease f until compatible is found
            if(f>=1):
                while(finish_sorted_array[f][1] > start_sorted_array[s][0]):
                    f-=1
            if(f==0):
                if finish_sorted_array[f][1]>start_sorted_array[s][0]:
                    break
                # set previous_compatible_array of selcted job s with comp job id of f
            #previous_compatible_array[s]=finish[f][3]


            previous_compatible_array[start_sorted_array[s][3]]=f


            s-=1
        return previous_compatible_array

    def chosen_mtrx(self, maxWeight, priorCompatibleMatrix):
        chosen_array=[0]*len(maxWeight)
        i = len(maxWeight)-1
        while(i>=0):
            # look before and keep going till we find a change in maxwt
            if(maxWeight[i]!=maxWeight[i-1]):
                chosen_array[i]=1
                i=priorCompatibleMatrix[i]
                continue
            i-=1
        return chosen_array

    def getResult(self):
        """return the string s that displays the table as shown in the example
when s is printed.
        """
        sorted_jobs = sorted(self.sc, key=lambda x: x[1])
        sorted_jobs_finish = sorted(self.sc, key=lambda x: x[1])

        n = len(sorted_jobs)
        table = [0 for _ in range(n)]

        table[0] = sorted_jobs[0][2];
        prior=[-1]
        start_arr=[sorted_jobs[i][0] for i in range(0,len(sorted_jobs))]
        finish_arr=[sorted_jobs[i][1] for i in range(0,len(sorted_jobs))]
        weight_arr=[sorted_jobs[i][2] for i in range(0,len(sorted_jobs))]
        for i in range(0,len(sorted_jobs)):
            sorted_jobs_finish[i].append(i)
        sorted_jobs_start = sorted_jobs_finish
        sorted_jobs_start = sorted(sorted_jobs_start,key=lambda x: x[0])

        pc=self.previousCmptbl(sorted_jobs_start, sorted_jobs_finish)

        for i in range(1, n):

            # Find profit including the current job
            inclProf = sorted_jobs[i][2]
            l = pc[i]
            prior.append(l)

            if (l != -1):
                inclProf += table[l];



            table[i] = max(inclProf, table[i - 1])

        c=self.chosen_mtrx(table, pc)
        rp= self.addRow('Index', prior, True) + self.addRow('Start', start_arr, False) + self.addRow('Finish', finish_arr, False) + self.addRow('Weight', weight_arr, False) + self.addRow('Prior', pc, False) + self.addRow('MAX Weight', table, False) + self.addRow('Chosen', c, False) + (f'Total\t{table[n - 1]}\t')

        return (f'{rp} \n')



def test123():
    # the expected results are shown below
    t1 = [[89, 100, 7], [26, 79, 3], [17, 64, 3], [86, 96, 7], [3, 75, 9], [
        64, 87, 5], [63, 92, 5], [13, 17, 8], [64, 76, 6], [17, 88, 8]]
    t2 = [[41, 60, 8], [56, 65, 9], [49, 95, 6], [36, 80, 7], [17, 41, 5], [55, 66, 7], [32, 79, 6], [48, 72, 6], [7, 63, 3], [6, 47, 3]]
    t3 = [[77, 99, 3], [10, 93, 8], [9, 67, 6], [88, 96, 7], [9, 14, 6], [5, 40, 9], [62, 65, 7], [
        6, 93, 9], [49, 64, 5], [50, 61, 7], [48, 54, 7], [25, 34, 6], [79, 81, 4], [6, 31, 5], [30, 34, 5]]
    for s in [t1, t2, t3]:
        x = WeightedIntervalSchedule(s)
        ans = x.getResult()
        print(ans)

test123()