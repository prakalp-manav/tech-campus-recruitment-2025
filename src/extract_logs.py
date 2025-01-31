import sys,os,re

def extract_logs(file, date, op="output"):
    os.makedirs(op, exist_ok=True)
    
    te = "output_" + date + ".txt"
    temp = os.path.join(op, te)

    pat = re.compile(f"^{date}T")
    
    try:
        with open(file, 'r', encoding='utf-8') as ip_f, open(temp, 'w', encoding='utf-8') as op_f:
            for i in ip_f:
                if pat.match(i):
                    op_f.write(i)
        print("Logs saved !!!")
    except Exception as e:
        print("Error occured - ",e)


date = sys.argv[1]
file = "test_logs.log"
extract_logs(file,date)
