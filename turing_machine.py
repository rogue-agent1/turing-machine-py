#!/usr/bin/env python3
"""Turing machine simulator — single tape, infinite both directions."""
class TuringMachine:
    def __init__(self,transitions,start,accept,reject="reject",blank="_"):
        self.trans=transitions;self.start=start;self.accept=accept
        self.reject=reject;self.blank=blank
    def run(self,input_str,max_steps=10000):
        tape=dict(enumerate(input_str));head=0;state=self.start
        for step in range(max_steps):
            if state==self.accept:return True,step
            if state==self.reject:return False,step
            sym=tape.get(head,self.blank)
            key=(state,sym)
            if key not in self.trans:return False,step
            new_state,write,direction=self.trans[key]
            tape[head]=write;state=new_state
            head+=1 if direction=="R" else -1
        return None,max_steps  # didn't halt
    def tape_str(self,tape,lo,hi):
        return"".join(tape.get(i,"_") for i in range(lo,hi+1))
def main():
    # Accept strings of form 0^n 1^n
    trans={("q0","0"):("q1","X","R"),("q1","0"):("q1","0","R"),("q1","Y"):("q1","Y","R"),
           ("q1","1"):("q2","Y","L"),("q2","0"):("q2","0","L"),("q2","Y"):("q2","Y","L"),
           ("q2","X"):("q0","X","R"),("q0","Y"):("q3","Y","R"),("q3","Y"):("q3","Y","R"),
           ("q3","_"):("accept","_","R")}
    tm=TuringMachine(trans,"q0","accept")
    for s in["0011","01","000111","0110"]:
        ok,steps=tm.run(s);print(f"'{s}': {'accept' if ok else 'reject'} in {steps} steps")
if __name__=="__main__":main()
