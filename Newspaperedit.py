import math
def para(arr_para,width):
    line_no = 0
    for para in arr_para:
        line_no+=1
        sent = ""
        for w in para:
            sent+=w
            sent+=" "
        sent = sent.strip()
        sent = "*"+sent+"*"
        if(len(sent)-2<width):
            if(len(para)%2==0):
                sent = " "*len(para)+ sent + " " *len(para)
            else:
                sent = " "*math.floor(len(para)//2) + sent + " " *math.floor(len(para)//2)
        
        if(line_no==1):
            print("*"*width)
        print(sent+"\n")
        if(line_no==len(para)-1):
            print("*"*width)

        
#test cases

arr_para = [["Hi","my","name","is","parth"],["I","Live","in","Ny"]]

para(arr_para,20)



