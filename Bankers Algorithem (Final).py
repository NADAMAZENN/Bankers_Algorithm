import tkinter as tk
from tkinter import ttk
import numpy as np
#-------------------------------------------------------------------------------------------------------

class BankerGUI:
    def __init__(self):
        self.firstFrame = tk.Tk()
        self.firstFrame .title("Banker's Algorithm")
        tk.Label(self.firstFrame , text="Consider while entering the data : ").grid(row=0, column=0, sticky="w")
        tk.Label(self.firstFrame , text=" --> Between resource types (,) & between processes (;)").grid(row=1, column=0, sticky="w")
        # Labels for input fields
        tk.Label(self.firstFrame , text="Total resources:").grid(row=2, column=0, sticky="w")
        tk.Label(self.firstFrame , text="Available resources:").grid(row=3, column=0, sticky="w")
        tk.Label(self.firstFrame , text="Current allocation:").grid(row=4, column=0, sticky="w")
        tk.Label(self.firstFrame , text="Maximum need:").grid(row=5, column=0, sticky="w")

        # Entry fields for input values
        self.total_resources_entry = tk.Entry(self.firstFrame)
        self.total_resources_entry.grid(row=2, column=1)
        self.available_resources_entry = tk.Entry(self.firstFrame)
        self.available_resources_entry.grid(row=3, column=1)
        self.current_allocation_entry = tk.Entry(self.firstFrame)
        self.current_allocation_entry.grid(row=4, column=1)
        self.max_need_entry = tk.Entry(self.firstFrame)
        self.max_need_entry.grid(row=5, column=1)


        # Button to run the algorithm
        self.run_button = tk.Button(self.firstFrame, text="  Next  ", command=self.secondPage)
        self.run_button.grid(row=6, column=1)
        self.firstFrame.mainloop()
#---------------------------------------------------------------------------------------------------------------------------------------
    def errorpage(self):
        self.ErrorFrame  = tk.Tk()
        self.ErrorFrame.title("Error Message !! ")
        tk.Label(self.ErrorFrame  , text="Total resources not equal to available resources plus current allocation").grid(row=7, column=0, sticky="w") 
        self.ErrorFrame.mainloop()
#---------------------------------------------------------------------------------------------------------------------------------------
    def secondPage(self):
        

        # Get input values
        self.total_resources = [int(x) for x in self.total_resources_entry.get().split(",")]
        self.available_resources = [int(x) for x in self.available_resources_entry.get().split(",")]
        self.current_allocation = [[int(x) for x in row.split(",")] for row in self.current_allocation_entry.get().split(";")]
        self.max_need = [[int(x) for x in row.split(",")] for row in self.max_need_entry.get().split(";")]


        if self.total_resources != [sum(x) for x in zip(self.available_resources, *self.current_allocation)] :
            self.errorpage()
           

        self.currentAllocation = np.array(self.current_allocation)
        self.maxNeed = np.array(self.max_need)
        self.Resource_Need = self.maxNeed - self.currentAllocation


        needList = self.Resource_Need.tolist()

        self.secoundFrame  = tk.Tk()
        self.secoundFrame.title("Banker's Algorithm")

        
        # Create table for total resources
        total_resources_label = ttk.Label(self.secoundFrame, text="Total Resources")
        total_resources_label.grid(row=0, column=0)
        self.total_resources_table = ttk.Treeview(self.secoundFrame, columns=list(range(len(self.total_resources ))), show='headings')
        for i in range(len(self.total_resources )):
            self.total_resources_table.column(i, width=50)
            self.total_resources_table.heading(i, text=str(i+1))
        self.total_resources_table.insert("", "end", values=self.total_resources )
        self.total_resources_table.grid(row=1, column=0)

        # Create table for available resources
        available_resources_label = ttk.Label(self.secoundFrame, text="Available Resources")
        available_resources_label.grid(row=0, column=1)
        self.available_resources_table = ttk.Treeview(self.secoundFrame, columns=list(range(len(self.available_resources))), show='headings')
        for i in range(len(self.available_resources)):
            self.available_resources_table.column(i, width=50)
            self.available_resources_table.heading(i, text=str(i+1))
        self.available_resources_table.insert("", "end", values=self.available_resources)
        self.available_resources_table.grid(row=1, column=1)

        # Create table for current allocation
        current_allocation_label = ttk.Label(self.secoundFrame, text="Current Allocation")
        current_allocation_label.grid(row=2, column=0)
        self.current_allocation_table = ttk.Treeview(self.secoundFrame, columns=list(range(len( self.current_allocation [0]))), show='headings')
        for i in range(len( self.current_allocation [0])):
            self.current_allocation_table.column(i, width=50)
            self.current_allocation_table.heading(i, text=str(i+1))
        for i in range(len( self.current_allocation )):
            self.current_allocation_table.insert("", "end", values= self.current_allocation [i])
        self.current_allocation_table.grid(row=3, column=0)

        # Create table for max need
        max_need_label = ttk.Label(self.secoundFrame, text="Max Need")
        max_need_label.grid(row=2, column=1)
        self.max_need_table = ttk.Treeview(self.secoundFrame, columns=list(range(len(self.max_need[0]))), show='headings')
        for i in range(len(self.max_need[0])):
            self.max_need_table.column(i, width=50)
            self.max_need_table.heading(i, text=str(i+1))
        for i in range(len(self.max_need)):
            self.max_need_table.insert("", "end", values=self.max_need[i])
        self.max_need_table.grid(row=3, column=1)


        # Create table for Resource_Need
        needList_label = ttk.Label(self.secoundFrame, text="Resource Need")
        needList_label.grid(row=4, column=0)
        needList_table = ttk.Treeview(self.secoundFrame, columns=list(range(len(needList[0]))), show='headings')
        for i in range(len(needList[0])):
            needList_table.column(i, width=50)
            needList_table.heading(i, text=str(i+1))
        for i in range(len(needList)):
            needList_table.insert("", "end", values=needList[i])
        needList_table.grid(row=5, column=0)


        # Create table for request
        self.request_label = ttk.Label(self.secoundFrame, text="Resource requested :\n   ex: 1,0,0,0")
        self.request_label.grid(row=6, column=0)
        self.request_entry = ttk.Entry(self.secoundFrame, width=20)
        self.request_entry.grid(row=6, column=1)
        # Create table for request
        self.Process_label = ttk.Label(self.secoundFrame, text="Requesting Process :")
        self.Process_label.grid(row=6, column=2)
        self.Process_entry = ttk.Entry(self.secoundFrame, width=20)
        self.Process_entry.grid(row=6, column=3)
    
        # Create button for running algorithm
        self.run_button = ttk.Button(self.secoundFrame, text="  Run  ", command=self.banker_algorithm)
        self.run_button.grid(row=8, column=2)


        self.secoundFrame.mainloop()
        #self.thirdFrame.mainloop()
    #==========================================
    def test(self):
        print("nothing")
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def create_tables(self):
            
            available_resources_label = ttk.Label(self.thirdFrame, text="Available Resources")
            available_resources_label.grid(row=0, column=0)
            self.available_resources_table = ttk.Treeview(self.thirdFrame, columns=list(range(len(self.available_resources))), show='headings')
            for i in range(len(self.available_resources)):
                self.available_resources_table.column(i, width=50)
                self.available_resources_table.heading(i, text=str(i+1))
            self.available_resources_table.insert("", "end", values=self.available_resources)
            self.available_resources_table.grid(row=1, column=0)

            current_allocation_label = ttk.Label(self.thirdFrame, text="Current Allocation")
            current_allocation_label.grid(row=0, column=1)
            self.current_allocation_table = ttk.Treeview(self.thirdFrame, columns=list(range(len(self.current_allocation[0]))), show='headings')
            for i in range(len(self.current_allocation[0])):
                self.current_allocation_table.column(i, width=50)
                self.current_allocation_table.heading(i, text=str(i+1))
            for i in range(len(self.current_allocation)):
                self.current_allocation_table.insert("", "end", values=self.current_allocation[i])
            self.current_allocation_table.grid(row=1, column=1)

            
 

    def create_button(self):
        self.next_button = tk.Button(self.thirdFrame, text=" Next ", command=self.next_step)
        self.next_button.grid(row=7, column=1)

    def update_tables(self,AVList):
        AVList = AVList.tolist()
        CAList = self.currentAllocation.tolist()
        # Clear old data from tables
        for child in self.available_resources_table.get_children():
            self.available_resources_table.delete(child)
        for child in self.current_allocation_table.get_children():
            self.current_allocation_table.delete(child)
        
        # Insert new data into tables
        
        self.available_resources_table.insert("", "end", values=AVList)
        for i in range(len(CAList)):
            self.current_allocation_table.insert("", "end", values=CAList[i])
        

   #-------------------------------------------------------------s-------------------------------------------------------------------------------------------------------------------------
    def next_step(self):
        size = len(self.currentAllocation)

        if self.counter < len(self.currentAllocation):
            for i in range(self.currentAllocation.shape[0]):
                if not self.finish[i] and all(self.Resource_Need[i] <= self.work):
                    # If the process can finish, mark it as finished and update the available resources
                    self.work += self.currentAllocation[i]
                    # mark as finish 
                    textprint = "The process released its resources is : " + str(i)
                    tk.Label(self.thirdFrame  , text=textprint).grid(row=4, column=0, sticky="w")    
                    self.finish[i] = True
                    self.found = True  
                    break
            self.counter += 1
        self.update_tables(self.work)      
        if  self.counter >= len(self.currentAllocation):
            self.ResultPage()    
  


   
   #------------------------------------------------------------------------------------------------------------------------------
    def thirdpage(self):
        self.found = False
        self.counter = 0
        self.create_button()
        self.thirdFrame.mainloop()      
    #------------------------------------------------------------------------------------------------------------------------------
    def ResultPage(self):

        if not all(self.finish):
            # Return the allocation and available matrices to their previous state
            self.avalibleResources += self.request
            self.currentAllocation[self.Resource_Request] -= self.request
            tk.Label(self.thirdFrame , text="Request denied: granting the request would result in an unsafe state.").grid(row=6, column=1, sticky="w")
            self.next_button.config(state=tk.DISABLED)
        else:    
        # The request can be granted
            tk.Label(self.thirdFrame  , text="* * Request granted * *").grid(row=6, column=1, sticky="w")
            self.next_button.config(state=tk.DISABLED)

        #self.ResultFrame.mainloop()

    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def banker_algorithm(self):

        self.thirdFrame  = tk.Tk()
        self.thirdFrame.title("Banker's Algorithm")
        self.create_tables()

        # Convert 
        self.request = list(map(int, self.request_entry.get().split(',')))
        self.Resource_Request = int( self.Process_entry.get())

        self.avalibleResources  = np.array(self.available_resources)

        # If the request is greater than the need, deny the request
        if any(self.request > self.Resource_Need[self.Resource_Request]):
            tk.Label(self.thirdFrame , text="Request denied: process has exceeded its maximum claim.").grid(row=6, column=0, sticky="w")
            self.next_button.config(state=tk.DISABLED)

        # If the request is greater than the available resources, deny the request
        if any(self.request > self.avalibleResources):
            tk.Label(self.thirdFrame  , text="Request denied: not enough resources available.").grid(row=6, column=0, sticky="w")
            self.next_button.config(state=tk.DISABLED)

        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        self.work = self.avalibleResources.copy()
        self.finish = [False] * self.currentAllocation.shape[0]

        while True:
            self.found = False
            for j in range(self.currentAllocation.shape[0]):
                for i in range(self.currentAllocation.shape[0]):
                    # Check if the process is not finished, and if its resource needs are less than or equal to the available resources
                    if not self.finish[i] and all(self.Resource_Need[i] <= self.work):
                        # If the process can finish, mark it as finished and update the available resources
                        self.work += self.currentAllocation[i]
                        self.finish[i] = True
                        self.found = True

            # If we didn't find any processes that can finish, then we exit the loop
            if not self.found:
                break

        # If there is no safe sequence, deny the request and exit the function
        if not all(self.finish):
            tk.Label(self.thirdFrame  , text="Request denied: there is no safe sequence.").grid(row=6, column=0, sticky="w")
            self.next_button.config(state=tk.DISABLED)
            return
        
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        # Adding the request to that allocation.
        self.StepsLabel = tk.Label(self.thirdFrame  , text= "Adding the request to that allocation...").grid(row=4, column=0, sticky="w")
        self.avalibleResources -= self.request
        self.currentAllocation[self.Resource_Request] += self.request

        #Check if granting the request will result in a safe state
        self.work = self.avalibleResources.copy()
        self.finish = [False] * self.currentAllocation.shape[0]
        self.flag=True
        #++++++++++++++++++++++++++++++++++++
        self.thirdpage()
        #++++++++++++++++++++++++++++++++++++       

        return True
     #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#main
if __name__ == '__main__':
    #EXAMPLES (TEST CASES)
# safe sequence 
#total :6,5,7,6
#available = 3,1,1,2
#allocation = 1,2,2,1;1,0,3,3;1,2,1,0
#maximum = 3,3,2,2;1,2,3,4;1,3,5,0
#request = 1,0,0,0
#process = 0

#*******************************
#total :6,5,7,6
#available = 3,1,1,2
#allocation = 1,2,1,0;1,2,2,1;1,0,3,3
#maximum = 1,3,5,0;3,3,2,2;1,2,3,4
#request = 1,0,0,0
#process = 1
#******************************
# no safe sequence
#total :9,2,5
#available = 2,1,1
#allocation = 1,0,1;2,1,2;3,0,0;1,0,0
#maximum = 2,1,1;5,4,4;3,1,1;1,1,1
#request = 1,0,0
#process = 0



    BankerGUI()
