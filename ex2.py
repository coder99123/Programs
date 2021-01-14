#!/usr/bin/env python
# coding: utf-8

# # Previously on the IBM Quantum Challenge
# *Ryoko has been stuck in the quantum realm. Please DM Ryoko and ask her about the **quantum realm** and you will find out more.  <br/>
# She is in a square room with excited qubits blocking her passage. <br/>
# How can you help Dr. Ryoko get out of the room?<br/>
# You can do this by learning how to solve a famous classic puzzle called "lights out." Good luck!*
# 
# [<< Click here to communicate with Dr. Ryoko through the web cam >>](https://youtu.be/kLizHnvTguE)

# In[1]:


from IPython.display import Image, display
Image('ryoko_pillars.png')


# # Week2-A: Lights Out Puzzle
# 
# **Lights out** is a famous puzzle game. The player is given a rectangular grid of lights which can be switched on and off. When you flip a switch inside one of those squares, it will toggle the on/off state of this and adjacent squares (up, down, left and right). Your goal is to turn all the lights off from a random starting light pattern.
# 
# ## Example Puzzle
# 
# An example of the puzzle with 3 x 3 grid is shown in the figure below. The light squares are labelled from 0 to 8. We can represent the starting pattern using a list of numbers, where `1` represents lights switched on and `0` represnts ligths switched off. The list `lights` below represents the starting pattern in this example (squares 3, 5, 6, 7 are on and the rest are off):
# 
# ```python
# lights = [0, 0, 0, 1, 0, 1, 1, 1, 0]
# ```
# 
# The example puzzle can be solved by flipping the switches in square 0, 3 and 4 as illustrated step by step in the figure. If you play with it a little bit, you will soon notice **two important properties of this puzzle game**:
# 
# 1. You don't need to flip a switch more than once.
# 2. The order of flipping doesn't matter.
# 
# Therefore, we can represent the puzzle solution as a list of numbers similar to the starting pattern. However, the meaning of `0` and `1` are different here:  `1` represents flipping a switch and `0` represents *not* flipping a switch. 
# 
# ```python
# solution = [1, 0, 0, 1, 1, 0, 0, 0, 0]
# ```

# In[2]:


Image('lights_out_rule.png')


# # Learning Exercise II-A
# 
# Let's try to solve a "Lights Out" puzzle using **Grover's algorithm**! The information you learned last week will be helpful in solving this puzzle.
# 
# Answer by creating a quantum circuit to solve the puzzle shown in the figure below. In the quantum circuit to be submitted, measure **only the `solution` (9bit)** that solves the puzzle. 
# To submit your solution, create a function which takes `lights` as an input and then returns a  `QuantumCircuit`.  You can name the function as you like. Make sure it works even with another dataset of "lights". We will validate your circuit with different inputs.
# 
# **In addition, please implement the quantum circuit within 28 qubits.**
# 
# There are several ways to solve it without using Grover's algorithm, but we ask you to **use Grover's algorithm** for this exercise. It should help you in solving other challenges.
# 
# Please note that you can get the answer with the same endian as the one used in the description. You can also use the following function.
# ```python
# qc = qc.reverse_bits()
# ```

# In[3]:


Image('lights_out_prob.png')


# ## Hint
# You’ll need a more complex oracle than the “Week1-B oracle” to solve this problem. The added auxiliary qubits will help you design the oracle part, but they need to be handled with care.  At the end of the oracle part, all auxiliary qubits must be returned to their initial state (this operation is sometimes called Uncomputation). [Week 3 of last year’s IBM Quantum Challenge](https://github.com/quantum-challenge/2019/blob/master/problems/week3/week3_en.ipynb) will support your understanding of this concept. 
# 
# If you are not sure about the optimal number of iterations for Grover's algorithm, solve [this quiz](https://github.com/qiskit-community/IBMQuantumChallenge2020/tree/main/quizzes/quiz_1) and talk to Dr. Ryoko(@ryoko) in the [Qiskit slack](qiskit.slack.com) via direct message. You can get important formulas of the theoretical aspects of week 1-B.

# In[309]:


# The starting pattern is represented by this list of numbers.
# Please use it as an input for your solution.

#initialization
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np

# importing Qiskit
from qiskit import IBMQ, BasicAer
from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute,transpile

# import basic plot tools
from qiskit.tools.visualization import plot_histogram

lights = [1, 1, 0, 0, 1, 0, 0, 0, 0]
#lights.reverse()
def week2a_ans_func(lights):
    ##### build your quantum circuit here
    oracle_bit = QuantumRegister(1,name="oracle")
    solution = QuantumRegister(9,name="sol")
    board = QuantumRegister(9,name="board")
    measure = ClassicalRegister(9)
    qc = QuantumCircuit(solution,board,oracle_bit,measure)
    
    #Setup_Board
    for index,value in enumerate(lights):
        if (value == 1):
            qc.x(board[index])
    qc.h(solution)
    qc.x(oracle_bit)
    qc.h(oracle_bit)
    qc.barrier()        
    #Setup_Oracle
    def oracle():
        
        #Button_0
        qc.cx(solution[0],board[0])
        qc.cx(solution[0],board[1])
        qc.cx(solution[0],board[3])
        
        #Button_1
        qc.cx(solution[1],board[1])
        qc.cx(solution[1],board[0])
        qc.cx(solution[1],board[4])
        qc.cx(solution[1],board[2])
        
        #Button_2
        qc.cx(solution[2],board[2])
        qc.cx(solution[2],board[1])
        qc.cx(solution[2],board[5])
        
        #Button_3
        qc.cx(solution[3],board[0])
        qc.cx(solution[3],board[4])
        qc.cx(solution[3],board[3])
        qc.cx(solution[3],board[6])
        
        #Button_4
        qc.cx(solution[4],board[1])
        qc.cx(solution[4],board[4])
        qc.cx(solution[4],board[3])
        qc.cx(solution[4],board[5])
        qc.cx(solution[4],board[7])
        
        #Button_5
        qc.cx(solution[5],board[5])
        qc.cx(solution[5],board[2])
        qc.cx(solution[5],board[4])
        qc.cx(solution[5],board[8])
        
        #Button_6
        qc.cx(solution[6],board[6])
        qc.cx(solution[6],board[7])
        qc.cx(solution[6],board[3])
        
        #Button_7
        qc.cx(solution[7],board[6])
        qc.cx(solution[7],board[7])
        qc.cx(solution[7],board[4])
        qc.cx(solution[7],board[8])
        
        #Button 8
        qc.cx(solution[8],board[8])
        qc.cx(solution[8],board[7])
        qc.cx(solution[8],board[5])
        qc.barrier()
    #Setup_Check
    
    def check():
        qc.x(board)
        qc.mct(board[0:9],oracle_bit[0])
        qc.x(board[0:9])
        qc.barrier()
        
    #Setup_Diffusion
    def diffusion():
        qc.h(solution)
        qc.x(solution)
        qc.h(solution[8])
        qc.mct(solution[0:8],solution[8])
        qc.h(solution[8])
        qc.x(solution)
        qc.h(solution)
        qc.barrier()
        
    for i in range(1):
        oracle()
        check()
        oracle()
        diffusion()
    
    qc.h(oracle_bit)
    qc.x(oracle_bit)

    qc.measure(solution,measure)
    qc = qc.reverse_bits()
    
    from qiskit.transpiler import PassManager
    from qiskit.transpiler.passes import Unroller
    pass_ = Unroller(['u3', 'cx'])
    pm = PassManager(pass_)
    new_circ = pm.run(qc)
    qc = transpile(new_circ, basis_gates=['u3','cx'],optimization_level=3)
    #####  In addition, please make it a function that can solve the problem even with different inputs (lights). We do validation with different inputs.
    
    return qc

#qc=week2a_ans_func(lights)
#qc.draw(output="mpl")


# In[310]:


# Submission code
from qc_grader import prepare_ex2a, grade_ex2a, submit_ex2a

# Execute your circuit with following prepare_ex2a() function.
# The prepare_ex2a () function works like the execute() function with only QuantumCircuit as an argument.
job = prepare_ex2a(week2a_ans_func)

result = job.result()
count = result.get_counts()
original_problem_set_counts = count[0]

original_problem_set_counts
# The bit string with the highest number of observations is treated as the solution.


# In[311]:


# Check your answer by executing following code.
# The quantum cost of the QuantumCircuit is obtained as the score. The quantum cost is related to rank only in the third week.
grade_ex2a(job)


# In[296]:


# Submit your results by executing following code. You can submit as many times as you like during the period. 
submit_ex2a(job)


# In[ ]:




