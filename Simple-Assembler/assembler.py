import sys
reg={'R0':'000','R1':'001','R2':'010','R3':'011','R4':'100','R5':'101','R6':'110','FLAGS':'111'}


#ALL THE FUNCTIONS FROM LINE 6-102
def Addition(rega,regb,regc):
    s="0000000"
    s=s+reg[rega]+reg[regb]+reg[regc]
    return(s)

def Subtraction(rega,regb,regc):
    s="0000100"
    s=s+reg[rega]+reg[regb]+reg[regc]
    return(s)

def mov_imm(registor,val):
    s=""
    s+="00010"
    s+=reg[registor]
    bin_ans=format(val, '08b')
    s+=bin_ans
    return(s)

def moveRegister(reg1 , reg2):
    return("00011" + "00000" + reg[reg1] + reg[reg2])
   
    #load stores all the values if the mem_addr in the reg1
def load(reg1 , variable): #change load store and all the immediate value checkers also check the variable counter
    return("00100" + reg[reg1]+variable_dict[variable])
   

def store(reg1 , variable):
    return("00101" + reg[reg1] + variable_dict[variable])


def Multiplication(rega,regb,regc):
    s="0011000"
    s=s+reg[rega]+reg[regb]+reg[regc]
    return(s)

#for dividing the register values--
def divide(reg3,reg4):
    return("00111" + "00000" + reg[reg3] + reg[reg4])
   
def right_shift(registor,val):
    s=""
    s+="01000"
    s+=reg[registor]
    bin_ans=format(val, '08b')
    s+=bin_ans
    return(s)

def left_shift(registor,val):
    s=""
    s+="01001"
    s+=reg[registor]
    bin_ans=format(val, '08b')
    s+=bin_ans
    return(s)    

def Exclusive_OR(rega,regb,regc):
    s="0101000"
    s=s+reg[rega]+reg[regb]+reg[regc]
    return(s)

def OR(rega,regb,regc):
    s="0101100"
    s=s+reg[rega]+reg[regb]+reg[regc]
    return(s)

def AND(rega,regb,regc):
    s="0110000"
    s=s+reg[rega]+reg[regb]+reg[regc]
    return(s)

#for bitwise NOT operation--
def invert(reg1 , reg2):
    return("01101" + "00000" + reg[reg1] + reg[reg2])

#for comparing the register values--
def compare(reg1 , reg2):
    return("01110" + "00000" + reg[reg1] + reg[reg2])

#for jumping to a memory address
def UnconditionalJump(label): ##
    return("01111" + "000" + label_dict[label])

#for jumping if greater than flag = 1
def JumpIfGreaterThan(label): ##
    return("10001" + "000" + label_dict[label])

#for jumping if less than flag = 1
def JumpIfLessThan(label): ##
    return("10000" + "000" + label_dict[label])
   
#for jumping if equal to  flag = 1
def JumpIfEqualTo(label): ##
    return("10010" + "000" + label_dict[label])

def Halt():
    s="1001100000000000"
    return(s)

#FOR TAKING THE INPUT
input_list = list(map(str, sys.stdin.readlines())) #l=[intructions as strings]
#if = open('sys.txt', mode='r+')
#input_list = f.readlines()
#THE WHILE LOOP BELOW IS FOR REMOVING ALL THE SPACES FROM THE INPUT
i=0
while(i<len(input_list)):
    if input_list[i]=="\n":
        input_list.remove(input_list[i])
        i=i-1
    i=i+1
variable_dict = {}
var_count=0
output_list=[]

#THE FOR LOOP BELOW IS FOR SPLITTING ALL THE INSTRUCTIONS INTO SEPERATE COMPONENTS
for i in range(len(input_list)):
    x=input_list[i]
    x=x.split()
    input_list[i]=x
    
#IF THE INPUT IS AN EMPTY FILE
if input_list==[]:
    print("no input")
    
#THE FOR LOOP BELOW IS FOR COUNTING ALL THE VARIABLES IN THE CODE
for i in range(0 ,len(input_list)):       
    if(input_list[i][0] != "var"):
        break
    else:
        var_count+=1

temp=var_count

#THE FOR LOOP BELOW IS FOR PUTTING ALL THE VARIABLES INTO A DICTIONARY
for i in range(0,len(input_list)):     
    if(input_list[i][0] != "var"):
        break
    else:
        idx=len(input_list)-temp
        variable_dict[input_list[i][1]] = format(idx, '08b')
        temp-=1

#THE BELOE FOR LOOP IS FOR CHECKING IF THERE IS A VARIABLE DECLARED IN THE MIDDLE OF THE CODE
for i in range(var_count ,len(input_list)):
    if input_list[i][0] == "var":
        output_list.append("variables not in beginning"+" ,line no:" + str(i-var_count))



label_dict = {} #this label_dict is for storing the address of the labels

instructions=["add","sub","mov","ld","st","mul","div","rs","ls","xor","or","and","not","cmp","jmp","jlt","jgt","je","hlt"]
register=["R0","R1","R2","R3","R4","R5","R6"]
register_withFlag=["R0","R1","R2","R3","R4","R5","R6","FLAGS"]

#THE FOR LOOP BELOW IS FOR PUTTING ALL THE LABELS INTO A DICTIONARY
for i in range(var_count ,len(input_list)):
    if(input_list[i][0][-1:]==":"):
        label_dict[input_list[i][0][:-1]] = format(i-var_count, '08b')
        input_list[i] = input_list[i][1:]

hlt_missing_flag = False
if ["hlt"] not in input_list:
    output_list.append("halt instruction missing")
    hlt_missing_flag = True


if(input_list!=[] and input_list[-1]!=["hlt"] and hlt_missing_flag==False):
    print("instructions after hlt"+" ,line no:"+str(input_list.index(["hlt"])+1-var_count))
    hlt_missing_flag = True
if(input_list.count(["hlt"])>1):
    print("halt multiple error"+" ,line no:"+str(len(input_list) - 1-var_count - input_list[::-1].index(["hlt"])))
    hlt_missing_flag = True

#THE FOR LOOP BELOW FOR IMPLEMENTING THE CODE WILL ONLY START IF THE hlt INSTRUCTION IS NOT MISSING
if hlt_missing_flag == False:
    #THE FOR LOOP BELOW WILL START FROM var_count AS WE DON'T HAVE TO CONSIDER THE VARIABLES AS SEPERATE INSTRUCTIONS
    for i in range(var_count,len(input_list)):
        x=input_list[i]
        

        if x[0] not in instructions:
            output_list.append("instruction not found"+" ,line no:"+str(i-var_count))
            break

        #FOR THE ADD INSTRUCTION
        elif(x[0]=="add"):
            if(len(x)!=4):
                output_list.append("Wrong type")
                break

            elif(x[1] not in register or x[2] not in register  or x[3] not in register):
                output_list.append("Register not found"+" ,line no:"+str(i-var_count))
                break
            else:
                output_list.append(Addition(x[1],x[2],x[3]))

        #FOR THE SUBTRACT INSTRUCTION     
        elif(x[0]=="sub"):
            if(len(x)!=4):
                output_list.append("Wrong type"+" ,line no:"+str(i-var_count))
                break
            elif(x[1] not in register or x[2] not in register  or x[3] not in register):
                output_list.append("Register not found"+" ,line no:"+str(i-var_count))
                break
            else:
                output_list.append(Subtraction(x[1],x[2],x[3]))
           
        #FOR THE MOV INSTRUCTION 
        elif(x[0]=="mov"):
            if(len(x)!=3):
                output_list.append("Wrong type"+" ,line no:"+str(i-var_count))
                break

            elif(x[2][0:1]=="$"):
                if(int(x[2][1:])>255 or int(x[2][1:])<0):
                    output_list.append("Illegal Immediate value"+" ,line no:"+str(i-var_count))
                elif(x[1] not in register):
                    output_list.append("Register not found"+" ,line no:"+str(i-var_count))
                else:
                    output_list.append(mov_imm(x[1],int(x[2][1:])))
            else:
                if (x[1] not in register or x[2] not in register_withFlag):
                    output_list.append("Register not found"+" ,line no:"+str(i-var_count))
                else:
                    output_list.append(moveRegister(x[1],x[2]))
                
        #FOR THE MOV INSTRUCTION        
        elif(x[0]=="ld"):
            if(len(x)!=3):
                output_list.append("Wrong type"+" ,line no:"+str(i-var_count))
                break

            elif(x[1] not in register or x[2] not in variable_dict.keys()):
                output_list.append("Use of undefined variables"+" ,line no:"+str(i-var_count))  
                break
            elif(x[2] in label_dict):
                output_list.append("Misuse of variables as labels"+" ,line no:"+str(i-var_count))
                break
            else:
                if(type(x[2]) == str):
                    output_list.append(load(x[1],x[2]))

                else:
                    output_list.append(load(x[1],x[2]))

        #FOR THE STORE INSTRUCTION
        elif(x[0]=="st"):
            if(len(x)!=3):
                output_list.append("Wrong type"+" ,line no:"+str(i-var_count))
                break
            elif(x[1] not in register or x[2] not in variable_dict.keys()):
                output_list.append("Use of undefined variables"+" ,line no:"+str(i-var_count))  
                break
            elif(x[2] in label_dict):
                output_list.append("Misuse of variables as labels"+" ,line no:"+str(i-var_count))
                break
            else:
                if(type(x[2]) == str):
                    output_list.append(store(x[1],x[2]))

                else:
                    output_list.append(store(x[1],x[2]))
            
        #FOR THE MULTIPLY INSTRUCTION    
        elif(x[0]=="mul"):
            if(len(x)!=4):
                output_list.append("Wrong type"+" ,line no:"+str(i-var_count))
                break
            elif(x[1] not in register or x[2] not in register  or x[3] not in register):
                output_list.append ("Register not found"+" ,line no:"+str(i-var_count))
                break
            else:
                output_list.append(Multiplication(x[1],x[2],x[3]))

        #FOR THE DIVIDE INSTRUCTION    
        elif(x[0]=="div"):
            if(len(x)!=3):
                output_list.append("Wrong type"+" ,line no:"+str(i-var_count))
                break
            elif(x[1] not in register or x[2] not in register):
                output_list.append("Register not found"+" ,line no:"+str(i-var_count))
                break
            else:
                output_list.append(divide(x[1],x[2]))

        #FOR THE RIGHT SHIFT INSTRUCTION    
        elif(x[0]=="rs"):
            if(len(x)!=3):
                output_list.append("Wrong type"+" ,line no:"+str(i-var_count))
                break
            elif(int(x[2][1:])>255 or int(x[2][1:])<0):
                output_list.append("Illegal Immediate value"+" ,line no:"+str(i-var_count))
            elif(x[1] not in register):
                output_list.append ("Register not found"+" ,line no:"+str(i-var_count))
            else:
                output_list.append(right_shift(x[1],int(x[2][1:])))

        #FOR THE LEFT SHIFT INSTRUCTION    
        elif(x[0]=="ls"):
            if(len(x)!=3):
                output_list.append("Wrong type"+" ,line no:"+str(i-var_count))
                break
            elif(int(x[2][1:])>255 or int(x[2][1:])<0):
                    output_list.append("Illegal Immediate value"+" ,line no:"+str(i-var_count))
            elif(x[1] not in register):
                    output_list.append ("Register not found"+" ,line no:"+str(i-var_count))
        
            else:
                output_list.append(left_shift(x[1],int(x[2][1:])))

        #FOR THE XOR INSTRUCTION    
        elif(x[0]=="xor"):
            if(len(x)!=4):
                output_list.append("Wrong type"+" ,line no:"+str(i-var_count))
                break

            elif(x[1] not in register or x[2] not in register  or x[3] not in register):
                output_list.append ("Register not found"+" ,line no:"+str(i-var_count))
                break
            else:
                output_list.append(Exclusive_OR(x[1],x[2],x[3]))

        #FOR THE OR INSTRUCTION    
        elif(x[0]=="or"):
            if(len(x)!=4):
                output_list.append("Wrong type"+" ,line no:"+str(i-var_count))
                break

            elif(x[1] not in register or x[2] not in register  or x[3] not in register):
                output_list.append("Register not found"+" ,line no:"+str(i-var_count))
                break
            else:
                output_list.append(OR(x[1],x[2],x[3]))

        #FOR THE AND INSTRUCTION     
        elif(x[0]=="and"):
            if(len(x)!=4):
                output_list.append("Wrong type"+" ,line no:"+str(i-var_count))
                break
            elif(x[1] not in register or x[2] not in register  or x[3] not in register):
                output_list.append("Register not found"+" ,line no:"+str(i-var_count))
                break
            else:
                output_list.append(AND(x[1],x[2],x[3]))

        #FOR THE NOT INSTRUCTION  
        elif(x[0]=="not"):
            if(len(x)!=3):
                print("Wrong type"+" ,line no:"+str(i-var_count))
                break
            elif(x[1] not in register or x[2] not in register):
                output_list.append("Register not found"+" ,line no:"+str(i-var_count))
                break
            else:
                output_list.append(invert(x[1],x[2]))

        #FOR THE cmp INSTRUCTION    
        elif(x[0]=="cmp"):
            if(len(x)!=3):
                output_list.append("Wrong type"+" ,line no:"+str(i-var_count))
                break

            elif(x[1] not in register or x[2] not in register):
                output_list.append("Register not found"+" ,line no:"+str(i-var_count))
                break
            else:
                output_list.append(compare(x[1],x[2]))

        #FOR THE jmp INSTRUCTION    
        elif(x[0]=="jmp"):
            if(len(x)!=2):
                output_list.append("Wrong type"+" ,line no:"+str(i-var_count))
                break

            elif(x[1] not in label_dict.keys()):
                output_list.append("Use of undefined label"+" ,line no:"+str(i-var_count))  
                break

            elif(x[1] in variable_dict.keys()):
                output_list.append("Misuse of labels as variable"+" ,line no:"+str(i-var_count))
                break
            else:
                output_list.append(UnconditionalJump(x[1]))

        #FOR THE jlt INSTRUCTION    
        elif(x[0]=="jlt"):
            if(len(x)!=2):
                output_list.append("Wrong type"+" ,line no:"+str(i-var_count))
                break

            elif(x[1] not in label_dict.keys()):
                output_list.append("Use of undefined label"+" ,line no:"+str(i-var_count))  
                break

            elif(x[1] in variable_dict.keys()):
                output_list.append("Misuse of labels as variable"+" ,line no:"+str(i-var_count))
                break
            else:
                output_list.append(JumpIfLessThan(x[1]))
        
        #FOR THE jgt INSTRUCTION   
        elif(x[0]=="jgt"):
            if(len(x)!=2):
                output_list.append("Wrong type"+" ,line no:"+str(i-var_count))
                break

            elif(x[1] not in label_dict.keys()):
                output_list.append("Use of undefined label"+" ,line no:"+str(i-var_count))  
                break

            elif(x[1] in variable_dict.keys()):
                output_list.append("Misuse of labels as variable"+" ,line no:"+str(i-var_count))
                break
            else:
                output_list.append(JumpIfGreaterThan(x[1]))

        #FOR THE je INSTRUCTION    
        elif(x[0]=="je"):
            if(len(x)!=2):
                output_list.append("Wrong type"+" ,line no:"+str(i-var_count))
                break

            elif(x[1] not in label_dict.keys()):
                output_list.append("Use of undefined label"+" ,line no:"+str(i-var_count))  
                break

            elif(x[1] in variable_dict.keys()):
                output_list.append("Misuse of labels as variable"+" ,line no:"+str(i-var_count))
                break
            else:
                output_list.append(JumpIfEqualTo(x[1]))
        #FOR THE hlt INSTRUCTION    
        elif(x[0]=="hlt"):
            output_list.append(Halt())
            break
       
    
for x in output_list:
    print(x)