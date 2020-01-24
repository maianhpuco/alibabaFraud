import numpy as np 
from multiprocessing import Process
np.seterr(divide='ignore', invalid='ignore')

class Bipartite_Graph():
    def __init__(self, U, I):
        ''' 
        matrix: M is to store relationship bw U and I: 1 means there is a clicks bw U and I
        matrix: WU is to store the Weight value for each U on each I 
        matrix: WI is to store the Weight value for each I on each U  
        process when single user click to single item: 
        M update new click > update WU & WI
        '''   
        self.M = np.matrix(np.zeros(shape=(len(U), len(I))))
        self.PI = np.matrix(np.zeros(shape=(len(I), 1))) # I*1 matrix
        self.PU = np.matrix(np.zeros(shape=(len(U), 1))) # U*1 matrix 
        self.queue = []

    def update_new_click(self, click):
        self.M[click[0], click[1]] = 1 
        return 

    def update_initial_PU(self, PU):
        self.PU = np.asmatrix(PU).T
        return

    def get_array_WI(self):
        return np.asarray(np.where(sum(self.M) ==0, sum(self.M), 1/sum(self.M))) # I*1 matrix 

    def get_array_WU(self):
        return np.asarray(np.where(sum(self.M.T) ==0, sum(self.M.T), 1/sum(self.M.T))) # U* 1 matrix 

    def get_matrix_WI(self):
        return np.asmatrix(np.asarray(np.where(sum(self.M) ==0, sum(self.M), 1/sum(self.M)))*np.asarray(self.M)) # U*I matrix 
    
    def get_matrix_WU(self): 
        return np.asmatrix(np.asarray(np.where(sum(self.M.T) ==0, sum(self.M.T), 1/sum(self.M.T)))*np.asarray(self.M.T)) #I*U matrix


    def update_PI(self):
        # get PI  = (WU*PU) / WI : matrix multiplication for all value of PI 
        # import pdb; pdb.set_trace()
        numerator = np.asarray(np.dot(self.get_matrix_WU(), self.PU)) # (I*U) * (U*1) = (I*1)
        denominator = sum(self.get_matrix_WU().T).T # I*1 
        self.PI = np.asmatrix(np.where(denominator == 0, 0, numerator / denominator))
        return # I*1 matrix 

    def update_PU(self):
        # import pdb; pdb.set_trace()
        numerator = np.asarray(np.dot(self.get_matrix_WI(), self.PI)).T # (U*I) * (I*1) = (U*1)# U*1 
        denominator = sum(self.get_matrix_WI().T)
        self.PU = np.asmatrix(np.where(denominator == 0, 0, numerator / denominator).T)
        return #U*1 matrix
    
    def iterate_until_convergence(self):
        # import pdb; pdb.set_trace()
        count = 0 
        for i in range(1000):
            temp_PI = self.PI
            temp_PU = self.PU
            count += 1 
            self.update_PI()
            self.update_PU()
            # if count == 66:
                # import pdb; pdb.set_trace()

            if (self.PI == temp_PI).all() and (self.PU== temp_PU).all():
                print('done')
                print(count)
                print('PU = ', self.PU)
                print('PI = ', self.PU)
                break
            
        return

    def reading_click(self, click_stream):
        # import pdb; pdb.set_trace()
        for each_click in click_stream:
            for item in each_click[1]:
                self.update_new_click((each_click[0], item))
                print('added user', each_click[0], 'item', item)


def main():
    U = np.array([123, 234, 456, 789])
    I = np.array([11, 22, 33, 44, 55])
    BG = Bipartite_Graph(U,I)
    BG.update_initial_PU([1,1,0,0])
    click_stream_1st = [(0, [0,1,2]), (1, [2]), (2, [0])]
    BG.reading_click(click_stream_1st)
    BG.iterate_until_convergence() 

if __name__ == "__main__":
    main()
    
   



    
        
    
