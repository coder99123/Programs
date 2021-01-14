#!/usr/bin/env python
# coding: utf-8

# In[6]:


problem_set = [
    [['0', '2'], ['1', '0'], ['1', '2'], ['1', '3'], ['2', '0'], ['3', '3']],
    [['0', '0'], ['0', '1'], ['1', '2'], ['2', '2'], ['3', '0'], ['3', '3']],
    [['0', '0'], ['1', '1'], ['1', '3'], ['2', '0'], ['3', '2'], ['3', '3']],
    [['0', '0'], ['0', '1'], ['1', '1'], ['1', '3'], ['3', '2'], ['3', '3']],
    [['0', '2'], ['1', '0'], ['1', '3'], ['2', '0'], ['3', '2'], ['3', '3']],
    [['1', '1'], ['1', '2'], ['2', '0'], ['2', '1'], ['3', '1'], ['3', '3']],
    [['0', '2'], ['0', '3'], ['1', '2'], ['2', '0'], ['2', '1'], ['3', '3']],
    [['0', '0'], ['0', '3'], ['1', '2'], ['2', '2'], ['2', '3'], ['3', '0']],
    [['0', '3'], ['1', '1'], ['1', '2'], ['2', '0'], ['2', '1'], ['3', '3']],
    [['0', '0'], ['0', '1'], ['1', '3'], ['2', '1'], ['2', '3'], ['3', '0']],
    [['0', '1'], ['0', '3'], ['1', '2'], ['1', '3'], ['2', '0'], ['3', '2']],
    [['0', '0'], ['1', '3'], ['2', '0'], ['2', '1'], ['2', '3'], ['3', '1']],
    [['0', '1'], ['0', '2'], ['1', '0'], ['1', '2'], ['2', '2'], ['2', '3']],
    [['0', '3'], ['1', '0'], ['1', '3'], ['2', '1'], ['2', '2'], ['3', '0']],
    [['0', '2'], ['0', '3'], ['1', '2'], ['2', '3'], ['3', '0'], ['3', '1']],
    [['0', '1'], ['1', '0'], ['1', '2'], ['2', '2'], ['3', '0'], ['3', '1']]
]


# In[ ]:


problem_set = [
    [['1', '1'], ['1', '2'], ['2', '0'], ['2', '2'], ['3', '2'], ['3', '3']], [['0', '2'], ['0', '3'], ['1', '0'], ['1', '2'], ['2', '1'], ['3', '2']], [['0', '2'], ['0', '3'], ['1', '2'], ['2', '0'], ['2', '1'], ['3', '3']], [['0', '1'], ['0', '3'], ['1', '3'], ['2', '0'], ['2', '2'], ['3', '1']], [['0', '0'], ['0', '3'], ['1', '1'], ['1', '2'], ['2', '1'], ['3', '2']], [['0', '0'], ['0', '3'], ['1', '1'], ['1', '3'], ['2', '0'], ['3', '1']], [['0', '1'], ['0', '3'], ['2', '2'], ['2', '3'], ['3', '0'], ['3', '2']], [['0', '0'], ['0', '2'], ['1', '1'], ['1', '2'], ['2', '3'], ['3', '3']], [['0', '1'], ['1', '1'], ['1', '2'], ['2', '2'], ['2', '3'], ['3', '3']], [['1', '1'], ['1', '3'], ['2', '2'], ['2', '3'], ['3', '0'], ['3', '2']], [['0', '2'], ['1', '1'], ['1', '3'], ['2', '0'], ['2', '3'], ['3', '2']], [['0', '0'], ['1', '2'], ['2', '1'], ['3', '0'], ['3', '1'], ['3', '2']], [['0', '1'], ['1', '0'], ['2', '1'], ['2', '2'], ['3', '0'], ['3', '2']], [['0', '1'], ['0', '2'], ['1', '2'], ['1', '3'], ['3', '0'], ['3', '2']], [['0', '1'], ['0', '2'], ['2', '1'], ['2', '3'], ['3', '0'], ['3', '3']], [['0', '3'], ['1', '1'], ['1', '3'], ['2', '0'], ['3', '0'], ['3', '1']]
]


# In[5]:


from qiskit import *
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import IBMQ, Aer, execute
provider = IBMQ.load_account()

from qiskit.transpiler import PassManager
from qiskit.transpiler.passes import Unroller
import math
from qiskit.qasm import pi


def week3_ans_func(problem_set2):

    """
    def rccx023_rccx123(qc, q0, q1, q2, q3):
        ## rccx(q0, q2, q3)
        qc.u2(0,pi,q3)
        qc.u1(pi/4,q3)
        qc.cx(q2,q3)
        qc.u1(-pi/4,q3)
        qc.cx(q0,q3)
        #qc.u1(pi/4,q3)
        #qc.cx(q2,q3)
        #qc.u1(-pi/4,q3)
        #qc.u2(0,pi,q3)

        ## rccx(q1, q2, q3)
        #qc.u2(0,pi,q3)
        #qc.u1(pi/4,q3)
        #qc.cx(q2,q3)
        #qc.u1(-pi/4,q3)
        qc.cx(q1,q3)
        qc.u1(pi/4,q3)
        qc.cx(q2,q3)
        qc.u1(-pi/4,q3)
        qc.u2(0,pi,q3)
    """

    # use u and p instead of u2 and u1
    def rccx023_rccx123(qc, q0, q1, q2, q3):
        ## rccx(q0, q2, q3)
        qc.u(pi/2,0,pi,q3)
        qc.p(pi/4,q3)
        qc.cx(q2,q3)
        qc.p(-pi/4,q3)
        qc.cx(q0,q3)
        #qc.u1(pi/4,q3)
        #qc.cx(q2,q3)
        #qc.u1(-pi/4,q3)
        #qc.u2(0,pi,q3)

        ## rccx(q1, q2, q3)
        #qc.u2(0,pi,q3)
        #qc.u1(pi/4,q3)
        #qc.cx(q2,q3)
        #qc.u1(-pi/4,q3)
        qc.cx(q1,q3)
        qc.p(pi/4,q3)
        qc.cx(q2,q3)
        qc.p(-pi/4,q3)
        qc.u(pi/2,0,pi,q3)    
    
    def rccx013_rccx023(qc, q0, q1, q2, q3):
        rccx023_rccx123(qc, q1, q2, q0, q3)        
    
    def qram_old(qc, ancillae, addr, tile, problem_set2):
        def record(qc, flag, tile, problem_set2, addr_bits):
            for star_i in range(0,6):
                x = int(problem_set2[addr_bits][star_i][0])
                y = int(problem_set2[addr_bits][star_i][1])
                qc.cx(flag, tile[y*4+x])
            
        for a in range(0,2):
            if a == 0:
                qc.x(addr[0])
            for b in range(0,2):
                if b == 0:
                    qc.x(addr[1])
                qc.rccx(addr[0], addr[1], ancillae[0])
                for c in range(0,2):
                    if c == 0:
                        qc.x(addr[2])
                    qc.rccx(ancillae[0], addr[2], ancillae[1])
                    for d in range(0,2):
                        if d == 0:
                            qc.x(addr[3])
                        qc.rccx(ancillae[1], addr[3], ancillae[2])
                        i = (a << 0) | (b << 1) | (c << 2) | (d << 3)
                        record(qc, ancillae[2], tile, problem_set2, i)  
                        qc.rccx(ancillae[1], addr[3], ancillae[2])
                        if d == 0:
                            qc.x(addr[3])
                    qc.rccx(ancillae[0], addr[2], ancillae[1])
                    if c == 0:
                        qc.x(addr[2])
                qc.rccx(addr[0], addr[1], ancillae[0])
                if b == 0:
                    qc.x(addr[1])
            if a == 0:
                qc.x(addr[0])

    
    def qram(qc, ancillae, addr, tile, problem_set2):
        def record(qc, flag, tile, problem_set2, addr_bits):
            for star_i in range(0,6):
                x = int(problem_set2[addr_bits][star_i][0])
                y = int(problem_set2[addr_bits][star_i][1])
                qc.cx(flag, tile[y*4+x])
            
        for a in range(0,2):
            if a == 0:
                qc.x(addr[0])
            for b in range(0,2):
                if b == 0:
                    qc.x(addr[1])
                    qc.rccx(addr[0], addr[1], ancillae[0])
                else:
                    qc.cx(addr[0], ancillae[0])
                    qc.x(addr[1])
                for c in range(0,2):
                    if c == 0:
                        qc.x(addr[2])
                        qc.rccx(ancillae[0], addr[2], ancillae[1])
                    else:
                        qc.cx(ancillae[0], ancillae[1])
                        qc.x(addr[2])
                    for d in range(0,2):
                        if d == 0:
                            qc.x(addr[3])
                            qc.rccx(ancillae[1], addr[3], ancillae[2])
                        else:
                            qc.cx(ancillae[1], ancillae[2])
                            qc.x(addr[3])
                        i = (a << 0) | (b << 1) | (c << 2) | (d << 3)
                        record(qc, ancillae[2], tile, problem_set2, i)  
                        if d == 0:
                            pass
                        else:
                            qc.x(addr[3])
                            qc.cx(ancillae[1], ancillae[2])
                            qc.rccx(ancillae[1], addr[3], ancillae[2])
                            qc.x(addr[3])                            
                    if c == 0:
                        pass
                    else:
                        qc.x(addr[2])
                        qc.cx(ancillae[0], ancillae[1])
                        qc.rccx(ancillae[0], addr[2], ancillae[1])
                        qc.x(addr[2])
                if b == 0:
                    pass
                else:
                    qc.x(addr[1])
                    qc.cx(addr[0], ancillae[0])
                    qc.rccx(addr[0], addr[1], ancillae[0])
                    qc.x(addr[1])
            if a == 0:
                qc.x(addr[0])
        
    def oracle(qc, ancillae, tile, addr_oracle):
        qram(qc, ancillae, addr, tile, problem_set2)
        
        qc.x(ancillae[4])
        for a in range(0,4):
            bs = []
            for b in range(0,4):
                if a == b:
                    continue
                bs.append(b)
            for bi in range(0,len(bs)):
                b = bs[bi]
            #for b in range(0,4):
                if a == b:
                    continue
                if a < b:
                    qc.rccx(tile[4*0+b], tile[4*1+a], ancillae[4])
                if bi == 0:
                    qc.rccx(tile[4*0+a], tile[4*1+b], ancillae[0])
                else:
                    prev_b = bs[bi-1]
                    rccx013_rccx023(qc, tile[4*0+a], tile[4*1+prev_b], tile[4*1+b], ancillae[0])
                #qc.rccx(tile[4*0+a], tile[4*1+b], ancillae[0])
                cs = []
                for c in range(0,4):
                    if a == c or b == c:
                        continue
                    cs.append(c)
                for ci in range(0,len(cs)):
                    c = cs[ci]
                    
                # for c in range(0,4):
                    if a == c or b == c:
                        continue
                    if a < c:
                        qc.rccx(tile[4*0+c], tile[4*2+a], ancillae[4])
                    if b < c:
                        qc.rccx(tile[4*1+c], tile[4*2+b], ancillae[4])
                    if ci == 0:
                        qc.rccx(tile[4*2+c], ancillae[0], ancillae[1])
                    else:
                        prev_c = cs[ci-1]
                        rccx023_rccx123(qc, tile[4*2+prev_c], tile[4*2+c], ancillae[0], ancillae[1])
                    #qc.rccx(tile[4*2+c], ancillae[0], ancillae[1])
                    ds = []
                    for d in range(0,4):
                        if a == d or b == d or c == d:
                            continue
                        ds.append(d)
                    for di in range(0,len(ds)):
                        d = ds[di]
                    # for d in range(0,4):
                        if a == d or b == d or c == d:
                            continue
                        if a < d:
                            qc.rccx(tile[4*0+d], tile[4*3+a], ancillae[4])
                        if b < d:
                            qc.rccx(tile[4*1+d], tile[4*3+b], ancillae[4])
                        if c < d:
                            qc.rccx(tile[4*2+d], tile[4*3+c], ancillae[4])
                        if di == 0:
                            qc.rccx(tile[4*3+d], ancillae[1], ancillae[2])
                        else:
                            prev_d = ds[di-1]
                            rccx023_rccx123(tile[4*3+prev_d], tile[4*3+d], ancillae[1], ancillae[2])
                        # qc.rccx(tile[4*3+d], ancillae[1], ancillae[2])
                        # ancillae[2] -> abcd-and
                        # ancillae[4] -> 2-flip-abcd-exists, and count
                        # ancillae[2] = 0, ancillae[4] = 0 => not flip
                        # ancillae[2] = 0, ancillae[4] = 1 => not flip
                        # ancillae[2] = 1, ancillae[4] = 0 => not flip
                        # ancillae[2] = 1, ancillae[4] = 1 =>     flip
                        qc.ccx(ancillae[2], ancillae[4], addr_oracle)
                        if di + 1 == len(ds):
                            qc.rccx(tile[4*3+d], ancillae[1], ancillae[2])                            
                        #qc.rccx(tile[4*3+d], ancillae[1], ancillae[2])
                        if c < d:
                            qc.rccx(tile[4*2+d], tile[4*3+c], ancillae[4])
                        if b < d:
                            qc.rccx(tile[4*1+d], tile[4*3+b], ancillae[4])
                        if a < d:
                            qc.rccx(tile[4*0+d], tile[4*3+a], ancillae[4])
                    # qc.rccx(tile[4*2+c], ancillae[0], ancillae[1])
                    if ci + 1 == len(cs):
                        qc.rccx(tile[4*2+c], ancillae[0], ancillae[1])
                    if b < c:
                        qc.rccx(tile[4*1+c], tile[4*2+b], ancillae[4])
                    if a < c:
                        qc.rccx(tile[4*0+c], tile[4*2+a], ancillae[4])
                # qc.rccx(tile[4*0+a], tile[4*1+b], ancillae[0])
                if bi + 1 == len(bs):
                    qc.rccx(tile[4*0+a], tile[4*1+b], ancillae[0])
                if a < b:
                    qc.rccx(tile[4*0+b], tile[4*1+a], ancillae[4])
        qc.x(ancillae[4])

        qram(qc, ancillae, addr, tile, problem_set2)

    def diffusion(qc, ancillae, addr):
        qc.h(addr)
        qc.x(addr)
        qc.h(addr[-1])
        qc.mct(addr[:-1], addr[-1], ancillae, mode='v-chain')
        qc.h(addr[-1])
        qc.x(addr)
        qc.h(addr)
        
    
    addr         = QuantumRegister(4)
    tile         = QuantumRegister(16)
    addr_oracle  = QuantumRegister(1)
    ancillae     = QuantumRegister(5)
    
    
    cr = ClassicalRegister(4)
    
    qc = QuantumCircuit(
        addr, tile, addr_oracle, ancillae,
        cr
    )
    
    qc.h(addr)
    
    qc.x(addr_oracle)
    qc.h(addr_oracle)
    
    for grover_iter in range(1):
        oracle(qc, ancillae, tile, addr_oracle)
        diffusion(qc, ancillae, addr)
        
    # qc.h(addr_oracle)
    # qc.x(addr_oracle)
    
    qc.measure(addr, cr)
                    
    qc = qc.reverse_bits()
    
    #pass_ = Unroller(['u3', 'cx'])
    #pm = PassManager(pass_)
    #new_circuit = pm.run(qc) 
    #print(new_circuit.count_ops())
    
    return qc


# In[10]:


# sample problems and answers for week-3
# problem_name = [[input], 'answer']
q1 = [[
    [['0', '1'], ['0', '2'], ['1', '0'], ['2', '0'], ['3', '1'], ['3', '3']],
    [['0', '2'], ['0', '3'], ['1', '1'], ['1', '3'], ['2', '0'], ['2', '1']],
    [['0', '0'], ['0', '3'], ['2', '1'], ['2', '2'], ['3', '0'], ['3', '1']],
    [['0', '0'], ['0', '1'], ['0', '2'], ['1', '1'], ['2', '0'], ['3', '2']],
    [['0', '1'], ['1', '2'], ['1', '3'], ['2', '0'], ['3', '0'], ['3', '1']],
    [['0', '2'], ['0', '3'], ['1', '1'], ['2', '0'], ['2', '1'], ['3', '0']],
    [['0', '0'], ['0', '3'], ['1', '2'], ['2', '0'], ['2', '1'], ['3', '3']],
    [['0', '2'], ['1', '1'], ['1', '3'], ['2', '0'], ['2', '3'], ['3', '2']],
    [['0', '1'], ['0', '3'], ['2', '0'], ['2', '2'], ['3', '0'], ['3', '3']],
    [['0', '0'], ['0', '2'], ['1', '0'], ['2', '2'], ['2', '3'], ['3', '3']],
    [['1', '0'], ['1', '3'], ['2', '1'], ['2', '2'], ['3', '2'], ['3', '3']],
    [['0', '0'], ['1', '0'], ['2', '1'], ['2', '2'], ['3', '2'], ['3', '3']],
    [['0', '0'], ['1', '1'], ['1', '2'], ['2', '1'], ['2', '3'], ['3', '0']],
    [['0', '1'], ['0', '3'], ['2', '1'], ['2', '2'], ['3', '0'], ['3', '1']],
    [['0', '0'], ['0', '1'], ['1', '1'], ['1', '3'], ['3', '2'], ['3', '3']],
    [['0', '0'], ['0', '3'], ['1', '2'], ['1', '3'], ['3', '0'], ['3', '1']]], '6'
]
q2 = [[
    [['0', '0'], ['0', '2'], ['1', '0'], ['1', '1'], ['3', '1'], ['3', '3']],
    [['0', '2'], ['0', '3'], ['1', '1'], ['1', '3'], ['2', '0'], ['2', '1']],
    [['0', '0'], ['1', '0'], ['2', '1'], ['2', '3'], ['3', '2'], ['3', '3']],
    [['0', '2'], ['0', '3'], ['1', '1'], ['1', '2'], ['3', '0'], ['3', '2']],
    [['0', '2'], ['0', '3'], ['2', '0'], ['2', '1'], ['3', '1'], ['3', '3']],
    [['0', '1'], ['0', '3'], ['1', '2'], ['1', '3'], ['2', '2'], ['3', '1']],
    [['0', '0'], ['1', '0'], ['2', '2'], ['2', '3'], ['3', '1'], ['3', '3']],
    [['0', '0'], ['0', '1'], ['1', '2'], ['2', '0'], ['3', '1'], ['3', '2']],
    [['0', '1'], ['0', '2'], ['1', '0'], ['1', '3'], ['3', '0'], ['3', '1']],
    [['0', '0'], ['0', '2'], ['1', '0'], ['1', '3'], ['2', '1'], ['2', '2']],
    [['0', '0'], ['0', '1'], ['0', '3'], ['1', '0'], ['2', '1'], ['3', '3']],
    [['0', '0'], ['0', '3'], ['1', '1'], ['1', '3'], ['2', '0'], ['2', '2']],
    [['0', '1'], ['1', '3'], ['2', '0'], ['2', '1'], ['2', '3'], ['3', '0']],
    [['0', '0'], ['1', '1'], ['2', '0'], ['2', '3'], ['3', '1'], ['3', '2']],
    [['0', '0'], ['0', '3'], ['1', '2'], ['2', '2'], ['3', '1'], ['3', '3']],
    [['0', '2'], ['0', '3'], ['1', '0'], ['1', '2'], ['2', '1'], ['2', '2']]], '13'
]
q3 = [[
    [['0', '2'], ['0', '3'], ['1', '1'], ['2', '0'], ['3', '0'], ['3', '1']],
    [['0', '1'], ['0', '3'], ['2', '0'], ['2', '2'], ['3', '0'], ['3', '1']],
    [['0', '0'], ['0', '3'], ['1', '1'], ['1', '3'], ['2', '2'], ['2', '3']],
    [['0', '2'], ['0', '3'], ['1', '0'], ['1', '1'], ['2', '3'], ['3', '1']],
    [['0', '1'], ['0', '2'], ['1', '0'], ['2', '0'], ['2', '3'], ['3', '3']],
    [['0', '3'], ['1', '0'], ['1', '2'], ['2', '1'], ['2', '2'], ['3', '3']],
    [['0', '1'], ['0', '3'], ['2', '0'], ['2', '3'], ['3', '2'], ['3', '3']],
    [['1', '0'], ['1', '1'], ['2', '1'], ['2', '3'], ['3', '2'], ['3', '3']],
    [['0', '1'], ['0', '2'], ['1', '0'], ['1', '3'], ['2', '3'], ['3', '0']],
    [['0', '0'], ['1', '1'], ['1', '3'], ['2', '0'], ['3', '2'], ['3', '3']],
    [['0', '1'], ['0', '2'], ['1', '3'], ['2', '0'], ['3', '0'], ['3', '3']],
    [['0', '0'], ['0', '1'], ['2', '0'], ['2', '3'], ['3', '2'], ['3', '3']],
    [['0', '3'], ['1', '0'], ['1', '2'], ['2', '2'], ['3', '0'], ['3', '3']],
    [['0', '0'], ['0', '3'], ['1', '0'], ['1', '1'], ['2', '0'], ['2', '2']],
    [['0', '1'], ['0', '3'], ['1', '2'], ['2', '0'], ['2', '1'], ['3', '2']],
    [['0', '2'], ['0', '3'], ['1', '3'], ['2', '0'], ['2', '2'], ['3', '0']]], '3'
]

qc = week3_ans_func(q1[0])
backend = provider.get_backend('ibmq_qasm_simulator')
job = execute(qc, backend=backend, shots=8192)
result = job.result()
count =result.get_counts()
print(count)


# In[7]:



from qc_grader import grade_ex3, prepare_ex3, submit_ex3


job = prepare_ex3(week3_ans_func)

result = job.result()
counts = result.get_counts()
original_problem_set_counts = counts[0]



