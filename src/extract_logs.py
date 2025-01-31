import sys,os,re

def extract_logs(file, date, op="output"):
    os.makedirs(op, exist_ok=True)
    temp = os.path.join(op, f"output_{date}.txt")
    
    pat = re.compile(f"^{date}T")
    
    try:
        with open(file, 'r', encoding='utf-8') as ip_f, open(temp, 'w', encoding='utf-8') as op_f:
            for i in ip_f:
                if pat.match(i):
                    op_f.write(i)
        print("Logs saved !!!")
    except Exception as e:
        print("Error occured - ",e)


if len(sys.argv) != 2:
    print("Usage: python extract_logs.py YYYY-MM-DD")
    sys.exit(1)
    
date = sys.argv[1]
file = "test_logs.log"
extract_logs(file,date)