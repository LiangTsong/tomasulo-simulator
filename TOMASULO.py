# LiangCong 梁聪 liang-cong@foxmail.com
# 2016013314@THU

import copy
from prettytable import PrettyTable
import websockets
import asyncio
import json

# Constants-Op
ADD = "ADD"
SUB = "SUB"
MUL = "MUL"
DIV = "DIV"
JUMP = "JUMP"
LD = "LD"
# Constants-Others
EMPTY_R = "EMPTY_R"
EMPTY = "EMPTY"
READY = "READY"
NREADY = "NREADY"
# Constants-States
NOCCUPIED = -1
ISSUE = 0
EXEC = 1
WB = 2 # Actually, this means "about to write back".
# Constants-ExecutingCycles
ALL_CYCLE = {LD:3, JUMP:1, ADD:3, SUB:3, MUL:12, DIV:40}

# Hardware
ALL_REGISTER = 32
ALL_RESERVATION = {ADD:6, MUL:3}
ALL_ALU = {ADD:3, MUL:2}
Occupied_Reservation = {ADD:0, MUL:0}
Occupied_ALU = {ADD:0, MUL:0, LD:0}
ALL_LD_ALU = 2
ALL_LD_RESERVATION = 3
Occupied_LD_RESERVATION = 0
Occupied_LD_ALU = 0

# A queue for ready instructions
ready_queue_add = list()
ready_queue_mul = list()
ready_queue_ld = list()

def aluOccupy(type, isOccupy, Name):
    "isOccupy == True: Occupy; Else: Release. Called when some RS stepping into EXEC state."
    ALUtoUSE = ""
    QUEUEtoUSE = ready_queue_add
    if type == ADD or type == SUB or type == JUMP:
        ALUtoUSE = ADD
        QUEUEtoUSE = ready_queue_add
    elif type == MUL or type == DIV:
        ALUtoUSE = MUL
        QUEUEtoUSE = ready_queue_mul
    else:
        print("aluOccupy: Error: Unknow type occured-" + type)
        exit()

    if isOccupy:
        global Occupied_ALU
        # print("🏀已经占用"+str(Occupied_ALU[ALUtoUSE])+"个"+ALUtoUSE)
        if Occupied_ALU[ALUtoUSE] >= ALL_ALU[ALUtoUSE]:
            # No un-occupied ALU, ENQueue
            RS[Name].EnQuene(ALUtoUSE)
            # print("🏀分配失败1", Name)
            return False
        else:
            # If there are RSs waiting, choose a reservation station to execute.
            if len(QUEUEtoUSE) > 0:
                if QUEUEtoUSE[-1] == Name:
                    # This is the chosen one
                    RS[Name].DeQueue(ALUtoUSE)
                    Occupied_ALU[ALUtoUSE] += 1
                    # print("🏀分配成功2", Name)
                    return True
                else:
                    # print("🏀分配失败3", Name)
                    return False
            else:
                # Just give this RS the ALU
                Occupied_ALU[ALUtoUSE] += 1
                # print("🏀分配成功4", Name)
                return True
    else:
        if Occupied_ALU[ALUtoUSE] <= 0:
            print("aluOccupy: Error: Cannot release ALU!")
            exit()
        else:
            Occupied_ALU[ALUtoUSE] -= 1
            return True

def LDaluOccupy(isOccupy, Name):
    "Called when some LD Buffer stepping into EXEC state."
    if isOccupy:
        global Occupied_LD_ALU
        # print("🚩已经占用"+str(Occupied_LD_ALU)+"个LB")
        if Occupied_LD_ALU >= ALL_LD_ALU:
            # No un-occipied LD buffer, ENQueue
            LB[Name].EnQueue()
            # print("🚩分配失败1", Name)
            return False
        else:
            # If there are some LBs waiting, choose a LB to execute.
            if len(ready_queue_ld) > 0:
                if ready_queue_ld[-1] == Name:
                    # This is the chosen one
                    LB[Name].DeQueue()
                    Occupied_LD_ALU += 1
                    # print("🚩分配成功2", Name)
                    return True
                else:
                    # print("🚩分配失败3", Name)
                    return False
            else:
                # Just give this LB the ALU
                Occupied_LD_ALU += 1
                # print("🚩分配成功4", Name)
                return True
    else:
        if Occupied_LD_ALU <= 0:
            print("LDaluOccupy: Error: Cannot release ALU!")
            exit()
        else:
            Occupied_LD_ALU -= 1
            # print("🚩释放成功5")
            return True

class ReservationStation:
    """A line of a reservstion station item."""
    Busy = False
    Op = EMPTY
    Vj = EMPTY
    Vk = EMPTY
    Qj = EMPTY
    Qk = EMPTY
    CyclesRemaining = -1
    State = NOCCUPIED
    Instruction = EMPTY # The index of the instruction that is using this reservation station.
    Name = ""
    WB_register = -1
    AlreadyInQueue = False
    Destination = -1
    Answer = -1
    Issue_Cycle = -1

    def __init__(self, Name0):
        self.Name = Name0

    def isBusy(self):
        return self.Busy

    def Clean(self):
        self.Busy = False
        self.Op = EMPTY
        self.Vj = EMPTY
        self.Vk = EMPTY
        self.Qj = EMPTY
        self.Qk = EMPTY
        self.CyclesRemaining = -1
        self.State = NOCCUPIED
        self.Instruction = EMPTY
        self.WB_register = -1
        self.AlreadyInQueue = False
        self.Destination = -1
        self.Answer = -1
        self.Issue_Cycle = -1

    def Issue(self, Op0, Vj0, Vk0, Qj0, Qk0, executing_cycles0, instruction_index, WB_register0, Issue_Cycle0, Destination0 = -1): # WB_register is an interger
        self.Busy = True
        self.Op = Op0
        self.Vj = Vj0
        self.Vk = Vk0
        self.Qj = Qj0
        self.Qk = Qk0
        self.CyclesRemaining = executing_cycles0
        self.State = ISSUE
        self.Instruction = instruction_index
        self.WB_register = WB_register0
        self.Destination = Destination0
        self.Issue_Cycle = Issue_Cycle0
        # Set register, no need when JUMP
        if WB_register0 >= 0:
            R[self.WB_register].setSource(self.Name)
        global Instruction_Ready
        global Instruction_to_Issue
        if self.Op == JUMP:
            # Once JUMP is issued, issue halted until JUMP's WB (at the same time).
            Instruction_Ready = False
        else:
            Instruction_to_Issue += 1
        # For DEBUG
        global issue_dict
        issue_dict[self.Instruction][self.Issue_Cycle] = list()
        issue_dict[self.Instruction][self.Issue_Cycle].append(Cycle)


    def EXEC_1Step(self):
        "One cycle of EXEC. Called by self.TicToc()."
        "CAUTION: Before doing this, self.CyclesRemaining must be set."
        if self.State != EXEC and self.State != WB:
            print("RS EXEC_1Step: Error: Called when isn't execting!")
            exit()
        elif self.CyclesRemaining < 0:
            print("RS EXEC_1Step: Error: self.CyclesRemaining not set!")
            exit()
        else:
            self.CyclesRemaining -= 1
            if self.CyclesRemaining == 0:
                self.State = WB
                # For DEBUG
                global issue_dict
                issue_dict[self.Instruction][self.Issue_Cycle].append(Cycle)

                # If this instruction is JUMP, now the next instruction to issue is known.
                if self.Op == JUMP:
                    if self.Qj == READY and self.Qk == READY:
                        global Instruction_to_Issue
                        global Instruction_Ready
                        Instruction_to_Issue = ALU.getAluAns(self.Op, self.Vj, self.Vk, self.Destination)
                        # print("⚠️JUMP发射指令", str(Instruction_to_Issue))
                    else:
                        print("RS EXEC_1Step: Error: ALU called while Oprands are not ready.")
                        exit()
                else:
                    self.Answer = ALU.getAluAns(self.Op, self.Vj, self.Vk)
            elif self.CyclesRemaining < 0:
                # EXE complete. Release this ALU.
                aluOccupy(self.Op, False, self.Name)
                # Ready to issue instructions
                # If it's JUMP, no need to write back
                if self.Op != JUMP:
                    if R[self.WB_register].getSource() == self.Name:
                        global Write_Rigister_Request
                        Write_Rigister_Request[self.WB_register] = self.Answer
                    # Mark READY and fill NREADY RSs
                    global Write_RS_Request
                    Write_RS_Request[self.Name] = self.Answer
                else:
                    # JUMP
                    Instruction_Ready = True
                # Do WB stuff, now.
                self.WB_1Step()
                return True
            else:
                return False

    def WB_1Step(self):
        "One cycle of WB. Called by TicToc() and EXEC_1Step()."
        "This means the reservation station should be cleaned."
        # For DEBUG
        global issue_dict
        issue_dict[self.Instruction][self.Issue_Cycle].append(Cycle)

        if self.State != WB:
            print("RS WB_1Step: Error: Called when isn't writing back!")
            exit()
        self.Clean()
        return True

    def EnQuene(self, type):
        "When all ALUs are occupied, enqueue this reservation station."
        global ready_queue_add
        global ready_queue_mul
        if not self.AlreadyInQueue:
            if type == ADD:
                ready_queue_add.append(copy.copy(self.Name))
            elif type == MUL:
                ready_queue_mul.append(copy.copy(self.Name))
            self.AlreadyInQueue = True
            return True
        return False

    def DeQueue(self, type):
        "When there's an ALU for this RS, dequeue this reservation station."
        global ready_queue_add
        global ready_queue_mul
        if self.AlreadyInQueue:
            if type == ADD:
                ready_queue_add = ready_queue_add[:-1]
            elif type == MUL:
                ready_queue_mul = ready_queue_mul[:-1]
            self.AlreadyInQueue = False
            return True
        return False

    def TicToc(self):
        "For each cycle, call this function once. If current state is done, return True."
        if self.State == NOCCUPIED:
            "In fact, this will NOT be used. I use self.Issue() instead."
            self.State = ISSUE
            return True
        elif self.State == ISSUE:
            "Check if the operands are all ready, and there exists a un-occupied ALU."
            if self.Qj == READY and self.Qk == READY and aluOccupy(self.Op, True, self.Name):
                self.State = EXEC
                # Do EXEC stuff, now.
                # In DIV, if the divisor is 0, CyclesRemaining is set to 1.
                if self.Op == DIV and self.Vk == 0:
                    # print("😄Divisor is 0!")
                    self.CyclesRemaining = 1
                self.EXEC_1Step()
                return True
            else:
                return False
        elif self.State == EXEC or self.State == WB:
            return self.EXEC_1Step()

class LDBuffer:
    """A line of a ld buffer item."""
    Busy = False
    Address = 0
    State = NOCCUPIED
    AlreadyInQueue = False
    Instruction = EMPTY # The index of the instruction that is using this ld buffer.
    Name = ""
    Register = -1
    CyclesRemaining = -1
    Issue_Cycle = 0

    def __init__(self, Name0):
        self.Name = Name0

    def isBusy(self):
        return self.Busy

    def Issue(self, Address0, executing_cycles0, Register0, Instruction_index, Issue_Cycle0):
        self.Busy = True
        self.State = NOCCUPIED
        self.Address = Address0
        self.Register = Register0
        self.Instruction = Instruction_index
        self.CyclesRemaining = executing_cycles0
        self.Issue_Cycle = Issue_Cycle0
        R[self.Register].setSource(self.Name)
        global Instruction_to_Issue
        Instruction_to_Issue += 1
        self.TicToc()
        # For DEBUG
        global issue_dict
        issue_dict[self.Instruction][self.Issue_Cycle] = list()
        issue_dict[self.Instruction][self.Issue_Cycle].append(Cycle)


    def Clean(self):
        self.Busy = False
        self.Address = 0
        self.State = NOCCUPIED
        self.AlreadyInQueue = False
        self.Instruction = EMPTY
        self.Register = -1
        self.CyclesRemaining = -1
        self.Issue_Cycle = -1

    def EnQueue(self):
        global ready_queue_ld
        if not self.AlreadyInQueue:
            ready_queue_ld.append(copy.copy(self.Name))
            self.AlreadyInQueue = True
            return True
        return False

    def DeQueue(self):
        global ready_queue_ld
        if self.AlreadyInQueue:
            ready_queue_ld = ready_queue_ld[:-1]
            self.AlreadyInQueue = False
            return True
        return False

    def EXEC_1Step(self):
        if self.State != EXEC and self.State != WB: # WB means the last cycle of EXEC
            print("LB EXEC_1Step: Error: Called when isn't execting!")
            exit()
        elif self.CyclesRemaining < 0:
            print("LB EXEC_1Step: Error: self.CyclesRemaining not set!")
            exit()
        else:
            self.CyclesRemaining -= 1
            if self.CyclesRemaining == 0:
                self.State = WB
                # For DEBUG
                global issue_dict
                issue_dict[self.Instruction][self.Issue_Cycle].append(Cycle)

            if self.CyclesRemaining < 0:
                # EXE compleate. Release this ALU.
                LDaluOccupy(False, self.Name)
                if R[self.Register].getSource() == self.Name:
                    global Write_Rigister_Request
                    Write_Rigister_Request[self.Register] = self.Address
                # Mark ready and fill RS's NREADY values
                global Write_RS_Request
                Write_RS_Request[self.Name] = self.Address
                self.WB_1Step()
                return True
            else:
                return False

    def WB_1Step(self):
        if self.State != WB:
            print("LB WB_1Step: Error: Called when isn't execting!")
            exit()
        # For DEBUG
        global issue_dict
        issue_dict[self.Instruction][self.Issue_Cycle].append(Cycle)

        # Clean this LB.
        self.Clean()
        return True
        
    
    def TicToc(self):
        if self.State == NOCCUPIED:
            self.State = ISSUE
        elif self.State == ISSUE:
            # Check if there exists an un-occupied LD Buffer
            # print("🚩当前已经有"+str(Occupied_LD_ALU)+"个LD被分配")
            if LDaluOccupy(True, self.Name):
                self.State = EXEC
                self.EXEC_1Step()
                return True
        elif self.State == EXEC or self.State == WB:
            self.EXEC_1Step()

class Register:
    """A register's state."""
    Name = -1
    Value = 0
    Source = 0
    State = READY

    def __init__(self, Name0):
        self.Name = Name0 # An integer

    def Clean(self):    
        self.Value = 0
        self.Source = 0
        self.State = READY

    def setSource(self, source0):
        self.Source = source0
        self.State = NREADY
        return True

    def setValue(self, value0):
        self.Value = value0
        self.State = READY
        self.Source = 0
        return True
    
    def getValue(self):
        return self.Value

    def getSource(self):
        return self.Source

    def getState(self):
        return self.State

class ALUs:
    Operand1 = 0
    Operand2 = 0
    Operand3 = 0
    Op = 0

    def getAluAns(self, Op0, Operand10, Operand20, Operand30 = 0):
        self.Operand1 = Operand10
        self.Operand2 = Operand20
        self.Operand3 = Operand30
        self.Op = Op0
        return self.getAns()

    def getAns(self):
        if self.Op == ADD:
            return self.Operand1 + self.Operand2
        elif self.Op == SUB:
            return self.Operand1 - self.Operand2
        elif self.Op == DIV:
            if self.Operand2 == 0:
                return int(self.Operand1)
            else:
                return int(self.Operand1 / self.Operand2)
        elif self.Op == MUL:
            return self.Operand1 * self.Operand2
        elif self.Op == JUMP:
            if self.Operand1 == self.Operand2:
                # print("⚠️符合：JUMP跳转发射指令", str(Instruction_to_Issue), str(self.Operand3))
                return Instruction_to_Issue + self.Operand3
            else:
                # print("⚠️不符合：JUMP顺序发射指令", str(self.Operand1), str(self.Operand2))
                return Instruction_to_Issue + 1
        else:
            print("ALU getAns: Error: An unknow type of operation was given.")
            exit()

#-------------------------------------------------

Instruction_to_Issue = 0
Instruction_Ready = True
Cycle = 0
Write_Rigister_Request = dict() # In the end of a cycle, write back.
Write_RS_Request = dict()

# Reservation Stations
# RS = {"Add1": ReservationStation("Add1"), "Add2": ReservationStation("Add2"), "Add3": ReservationStation("Add3"), \
#     "Add4": ReservationStation("Add4"), "Add5": ReservationStation("Add5"), "Add6": ReservationStation("Add6"), \
#     "Mul1": ReservationStation("Mul1"), "Mul2": ReservationStation("Mul2"), "Mul3": ReservationStation("Mul3")}
RS = dict()
for i in range(0, ALL_RESERVATION[ADD]):
    RS["Add"+str(i+1)] = ReservationStation("Add"+str(i+1))
for i in range(0, ALL_RESERVATION[MUL]):
    RS["Mul"+str(i+1)] = ReservationStation("Mul"+str(i+1))
# LD Buffers
# LB = {"LB1":LDBuffer("LB1"), "LB2":LDBuffer("LB2"), "LB3":LDBuffer("LB3")}
LB = dict()
for i in range(0, ALL_LD_RESERVATION):
    LB["LB"+str(i+1)] = LDBuffer("LB"+str(i+1))
# Registers
R = list()
for i in range(0, ALL_REGISTER):
    R.append(Register(i))
# ALU
ALU = ALUs()
issue_dict = dict()

#-------------------------------------------------

output = list()
def tomasulo(Instructions):
    global output
    global Instruction_to_Issue
    global Instruction_Ready
    global Cycle
    global Write_Rigister_Request
    global Write_RS_Request
    global RS
    global LB
    global R
    global ALU
    global issue_dict
    # # Read .NEL file
    # filename = input("Please type in the name of your .nel file:")
    # with open("./"+filename, 'r') as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         Instructions.append(line.strip().split(','))

    # print(Instructions)

    # Issue Table
    for i in range(0, len(Instructions)):
        issue_dict[i] = dict()

    def twos_comp(val, bits):
        "Compute the 2's complement of int value val"
        if (val & (1 << (bits - 1))) != 0:
            val = val - (1 << bits)
        return val

    # Program running
    # While all not busy, continue iteration
    Go_on = True
    while(Go_on):
        # print(str(Instruction_to_Issue))
        # input("Continue...")
        # print("\n\n\n\n\n")

        # A new cycle begins
        Cycle += 1

        # Firstly, finish the former RSs and LBs. Then, issue new instructions.
        # TicToc
        all_rs_and_ld_list = list()
        for key in RS.keys():
            if RS[key].Issue_Cycle < Cycle and RS[key].isBusy():
                all_rs_and_ld_list.append(RS[key])
        for key in LB.keys():
            if LB[key].Issue_Cycle < Cycle and LB[key].isBusy():
                all_rs_and_ld_list.append(LB[key])
        def getIssueCycle(elem):
            return elem.Issue_Cycle
        all_rs_and_ld_list.sort(key = getIssueCycle)
        for i in all_rs_and_ld_list:
            i.TicToc()

        # print("本轮的写回请求为：----------------")
        # print(Write_Rigister_Request)
        # print(Write_RS_Request)
        # Update Registers
        # Write_Rigister_Request
        for key in Write_Rigister_Request.keys():
            R[key].setValue(Write_Rigister_Request[key])
        # Update NREADY Values
        # Write_RS_Request
        for key_write in Write_RS_Request.keys():
            for key_rs in RS.keys():
                if RS[key_rs].Qj == key_write:
                    RS[key_rs].Qj = READY
                    RS[key_rs].Vj = Write_RS_Request[key_write]
                if RS[key_rs].Qk == key_write:
                    RS[key_rs].Qk = READY
                    RS[key_rs].Vk = Write_RS_Request[key_write]
        Write_Rigister_Request = dict()
        Write_RS_Request = dict()

        # Issue new instructions, only if there is no JUMP and Instruction_to_Issue is legal
        if Instruction_Ready and Instruction_to_Issue < len(Instructions):
            # print("⚠️Instruction_to_Issue = ", str(Instruction_to_Issue))
            # print("\n\n\n Continue...Instruction to issue: "  + str(Instructions[Instruction_to_Issue]))
            instr = Instructions[Instruction_to_Issue]
            if instr[0] != LD:
                the_RS_that_wanted = ''
                if instr[0] == ADD or instr[0] == SUB or instr[0] == JUMP:
                    the_RS_that_wanted = 'A'
                elif instr[0] == MUL or instr[0] == DIV:
                    the_RS_that_wanted = 'M'

                # Find a reservation station AND then Issue
                for key in RS.keys():
                    if key[0] == the_RS_that_wanted and not RS[key].isBusy():
                        # Got it
                        if instr[0] != JUMP:
                            Vj0 = ""
                            Vk0 = ""
                            Qj0 = ""
                            Qk0 = ""
                            # Now decide: If the operands instr[2] and instr[3] are ready
                            operand1_index = int(instr[2][1:])
                            operand2_index = int(instr[3][1:])
                            if R[operand1_index].getState() == NREADY:
                                Qj0 = R[operand1_index].getSource()
                                Vj0 = NREADY
                            else:
                                # Ready
                                Qj0 = READY
                                Vj0 = R[operand1_index].getValue()

                            if R[operand2_index].getState() == NREADY:
                                Qk0 = R[operand2_index].getSource()
                                Vk0 = NREADY
                            else:
                                # Ready
                                Qk0 = READY
                                Vk0 = R[operand2_index].getValue()
                            # Now Issue
                            RS[key].Issue(instr[0], Vj0, Vk0, Qj0, Qk0, ALL_CYCLE[instr[0]], Instruction_to_Issue, int(instr[1][1:]), Cycle)

                        else:
                            # For JUMP
                            # print("⚠️发射了JUMP指令！")
                            Qj0 = ""
                            Vk0 = ""
                            Qj0 = ""
                            Qk0 = ""
                            operand_index = int(instr[2][1:])
                            if R[operand_index].getState() == NREADY:
                                Qk0 = R[operand_index].getSource()
                                Vk0 = NREADY
                            else:
                                # Ready
                                Qk0 = READY
                                Vk0 = R[operand1_index].getValue()
                            RS[key].Issue(instr[0], twos_comp(int(instr[1], 16), 32), Vk0, READY, Qk0, ALL_CYCLE[instr[0]], Instruction_to_Issue, -1, Cycle, twos_comp(int(instr[3], 16),32))
                        break
            else:
                # LD
                # Find a Load Buffer AND then Issue
                for key in LB.keys():
                    if not LB[key].isBusy():
                        # Got it
                        # print("发射LB指令")
                        LB[key].Issue(twos_comp(int(instr[2], 16), 32), ALL_CYCLE[LD], int(instr[1][1:]), Instruction_to_Issue, Cycle)
                        break
        # else:
        #     print("因为JUMP，无法继续发射！")

        State_list = ["未使用", "Issue", "Exec", "EtoW"]
        single_output = list()
        # Print
        # print("This is cycle " + str(Cycle))
        # print("保留站:--------------------")
        table = PrettyTable(['保留站','Busy', 'Op','Vj','Vk','Qj','Qk','State','RemaingExecTime'])
        for key in RS.keys():
            i = RS[key]
            busy_state = ["No", "Yes"]
            single_output.append({'key':str(Cycle)+i.Name, 'name':i.Name, 'busy':busy_state[int(i.Busy)], 'op':i.Op, 'vj':i.Vj, 'vk':i.Vk, 'qj':i.Qj, 'qk':i.Qk, 'state':State_list[i.State+1], 'remainingcycle':i.CyclesRemaining})
            table.add_row([i.Name, i.Busy, i.Op, i.Vj, i.Vk, i.Qj, i.Qk, State_list[i.State+1], i.CyclesRemaining])
        # print(table)
        # print("LoadBuffer:--------------------")
        table = PrettyTable(['LoadBuffer','Busy','Address','State','RemaingExecTime'])
        for key in LB.keys():
            i = LB[key]
            busy_state = ["No", "Yes"]
            single_output.append({'key':str(Cycle)+i.Name, 'name':i.Name, 'busy':busy_state[int(i.Busy)], 'op':i.Address, 'state':State_list[i.State+1], 'remainingcycle':i.CyclesRemaining})
            table.add_row([i.Name, i.Busy, i.Address, State_list[i.State+1], i.CyclesRemaining])
        # print(table)
        # print("寄存器:--------------------")
        table = PrettyTable(['寄存器','Source','State','Value'])
        row_0 = dict() # source
        row_1 = dict() # state
        row_2 = dict() # value
        row_0["key"] = 0
        row_0["name"] = "REG"
        row_1["key"] = 1
        row_1["name"] = "REG"
        row_2["key"] = 2
        row_2["name"] = "REG"
        for i in R:
            row_0[i.Name] = i.Source
            row_1[i.Name] = i.State
            row_2[i.Name] = i.Value
            table.add_row([i.Name, i.Source, i.State, i.Value])
        single_output.append(row_0)
        single_output.append(row_1)
        single_output.append(row_2)
        # print(table)

        output.append(copy.deepcopy(single_output))

        Go_on = False
        for value in RS.values():
            if value.isBusy():
                Go_on = True
                break
        for value in LB.values():
            if value.isBusy():
                Go_on = True
                break


def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

#-------------------------------------------------
async def UI(websocket, path):
    global output
    global Occupied_LD_RESERVATION
    global Occupied_LD_ALU
    global RS
    global LB
    global R
    global ready_queue_add
    global ready_queue_mul
    global ready_queue_ld
    global issue_dict
    global Cycle
    global Instruction_to_Issue
    global Instruction_Ready
    global ALL_REGISTER
    global ALL_RESERVATION
    global ALL_ALU
    global ALL_LD_ALU
    global ALL_LD_RESERVATION
    global ALL_CYCLE

    while True:
        # Clean up
        output = list()
        Instruction_to_Issue = 0
        Instruction_Ready = True
        Occupied_LD_RESERVATION = 0
        Occupied_LD_ALU = 0
        ready_queue_add = list()
        ready_queue_mul = list()
        ready_queue_ld = list()
        issue_dict = dict()
        for i in range(0, ALL_RESERVATION[ADD]):
            RS["Add"+str(i+1)].Clean()
        for i in range(0, ALL_RESERVATION[MUL]):
            RS["Mul"+str(i+1)].Clean()
        for i in range(0, ALL_LD_RESERVATION):
            LB["LB"+str(i+1)].Clean()
        for i in range(0, ALL_REGISTER):
            R[i].Clean()
        Cycle = 0


        settings = {'RS_ADD':ALL_RESERVATION[ADD], 'RS_MUL':ALL_RESERVATION[MUL], 'R':ALL_REGISTER, 'LD':ALL_LD_RESERVATION, 'RS_ADD_ALU': ALL_ALU[ADD], 'RS_MUL_ALU': ALL_ALU[MUL], 'LD_ALU': ALL_LD_ALU, \
                'ADD':ALL_CYCLE[ADD], 'SUB':ALL_CYCLE[SUB], 'MUL':ALL_CYCLE[MUL], 'DIV':ALL_CYCLE[DIV], 'JUMP':ALL_CYCLE[JUMP], 'LOAD':ALL_CYCLE[LD]}
        json_str = json.dumps(settings)
        await websocket.send("000"+json_str)
        print("已经发送设置")

        
        # Wait for the .nel file that the UI sends to me
        nel = ""
        while True:
            nel = await websocket.recv()
            if nel[0:3] == "001":
                if nel[3:]!='null' and nel[3:] != '':
                    nel = nel[3:]
                    break
            elif nel[0:3] == "019":
                await websocket.send("020服务端成功连接")
            else:
                if not RepresentsInt(nel[3:]):
                    print("值无效！不修改。")
                elif nel[0:3] == "007":
                    # Change settings RS_ADD
                    ALL_RESERVATION[ADD] = int(nel[3:])
                    print("RSADD被设置为"+str(ALL_RESERVATION[ADD]))
                    await websocket.send("008服务端成功接受设置")
                elif nel[0:3] == "008":
                    # Change settings RS_MUL
                    ALL_RESERVATION[MUL] = int(nel[3:])
                    print("RSMUL被设置为"+str(ALL_RESERVATION[MUL]))
                    await websocket.send("008服务端成功接受设置")
                elif nel[0:3] == "009":
                    # Change settings LD
                    ALL_LD_RESERVATION = int(nel[3:])
                    print("LB被设置为"+str(ALL_LD_RESERVATION))
                    await websocket.send("008服务端成功接受设置")
                elif nel[0:3] == "010":
                    # Change settings RS_ADD_ALU
                    ALL_ALU[ADD] = int(nel[3:])
                    print("RSADDALU被设置为"+str(ALL_ALU[ADD]))
                    await websocket.send("008服务端成功接受设置")
                elif nel[0:3] == "011":
                    # Change settings RS_MUL_ALU
                    ALL_ALU[MUL] = int(nel[3:])
                    print("RSMULALU被设置为"+str(ALL_ALU[MUL]))
                    await websocket.send("008服务端成功接受设置")
                elif nel[0:3] == "012":
                    # Change settings LD_ALU
                    ALL_LD_ALU = int(nel[3:])
                    print("LDALU被设置为"+str(ALL_LD_ALU))
                    await websocket.send("008服务端成功接受设置")
                elif nel[0:3] == "013":
                    # Change settings ADD
                    ALL_CYCLE[ADD] = int(nel[3:])
                    print("ADD被设置为"+str(ALL_CYCLE[ADD]))
                    await websocket.send("008服务端成功接受设置")
                elif nel[0:3] == "014":
                    # Change settings SUB
                    ALL_CYCLE[SUB] = int(nel[3:])
                    print("SUB被设置为"+str(ALL_CYCLE[SUB]))
                    await websocket.send("008服务端成功接受设置")
                elif nel[0:3] == "015":
                    # Change settings MUL
                    ALL_CYCLE[MUL] = int(nel[3:])
                    print("MUL被设置为"+str(ALL_CYCLE[MUL]))
                    await websocket.send("008服务端成功接受设置")
                elif nel[0:3] == "016":
                    # Change settings DIV
                    ALL_CYCLE[DIV] = int(nel[3:])
                    print("DIV被设置为"+str(ALL_CYCLE[DIV]))
                    await websocket.send("008服务端成功接受设置")
                elif nel[0:3] == "017":
                    # Change settings JUMP
                    ALL_CYCLE[JUMP] = int(nel[3:])
                    print("JUMP被设置为"+str(ALL_CYCLE[JUMP]))
                    await websocket.send("008服务端成功接受设置")
                elif nel[0:3] == "018":
                    # Change settings LOAD
                    ALL_CYCLE[LD] = int(nel[3:])
                    print("LOAD被设置为"+str(ALL_CYCLE[LD]))
                    await websocket.send("008服务端成功接受设置")
                settings = {'RS_ADD':ALL_RESERVATION[ADD], 'RS_MUL':ALL_RESERVATION[MUL], 'R':ALL_REGISTER, 'LD':ALL_LD_RESERVATION, 'RS_ADD_ALU': ALL_ALU[ADD], 'RS_MUL_ALU': ALL_ALU[MUL], 'LD_ALU': ALL_LD_ALU, \
                    'ADD':ALL_CYCLE[ADD], 'SUB':ALL_CYCLE[SUB], 'MUL':ALL_CYCLE[MUL], 'DIV':ALL_CYCLE[DIV], 'JUMP':ALL_CYCLE[JUMP], 'LOAD':ALL_CYCLE[LD]}
                json_str = json.dumps(settings)
                await websocket.send("000"+json_str)
                print("已经发送设置")

        await websocket.send("003服务端成功接受NEL程序")
        # print("接受："+nel)
        Instrcutions = list()
        instr_list = nel.strip().split()
        for line in instr_list:
            Instrcutions.append(line.strip().split(','))
        json_str = json.dumps(Instrcutions)
        await websocket.send("004"+json_str)

        tomasulo(Instrcutions)

        output_issue_table = list()
        
        print(issue_dict)
        print(instr_list)
        for cycle in range(0, Cycle):
            for key in issue_dict.keys():
                if cycle in issue_dict[key]:
                    # This instruction key has been issued in Cycle cycle
                    exec_comp = issue_dict[key][cycle][1]
                    wb = issue_dict[key][cycle][2]
                    output_issue_table.append({'key':cycle, 'instruction':instr_list[key], 'issue':cycle, 'execcomp':exec_comp, 'writeback':wb})
        print(output_issue_table)

        json_str = json.dumps(output)
        await websocket.send("005"+json_str)

        json_str = json.dumps(output_issue_table)
        await websocket.send("006"+json_str)

        print("==================================")
        print("TOMASULO DONE in " + str(Cycle) + " CYCLES. THE REGISTERS ARE:")
        table = PrettyTable(['寄存器','Source','State','Value'])
        for i in R:
            table.add_row([i.Name, i.Source, i.State, i.Value])
        print(table)
        print("LiangCong 梁聪 2016013314@THU liang-cong@foxmail.com")
        print("==================================")
        
        

        

# Establish WebSockets connection
start_server = websockets.serve(UI, '127.0.0.1', 5678)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


print("==================================")
print("TOMASULO DONE in " + str(Cycle) + " CYCLES. THE REGISTERS ARE:")
table = PrettyTable(['寄存器','Source','State','Value'])
for i in R:
    table.add_row([i.Name, i.Source, i.State, i.Value])
print(table)
print("LiangCong 梁聪 2016013314@THU liang-cong@foxmail.com")
print("==================================")