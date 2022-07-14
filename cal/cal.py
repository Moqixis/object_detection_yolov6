import json

Note = open('preds.txt',mode='r')
preds = Note.read()
preds = json.loads(preds)
Note.close()

Note = open('truth.txt',mode='r')
truth = Note.read()
truth = json.loads(truth)
Note.close()

tp = 0
fp = 0
fn = 0
tn = 0
exp = 1

# num=0
# for i in range(len(preds)):
#     if truth[i] == 1:
#         num+=1
# print(num,len(preds))

for i in range(len(preds)):
    if preds[i] == 1 and truth[i] == 1:
        tp += 1
    elif preds[i] == 1 and truth[i] == 0:
        fp += 1
    elif preds[i] == 0 and truth[i] == 1:
        fn += 1
    elif preds[i] == 0 and truth[i] == 0:
        tn += 1

print(tp,fp,fn,tn)
fnr = (fn + exp) / (tp + fn + exp)
fpr = (fp + exp) / (fp + tn + exp)
print("漏检率和误诊率分别为：",round(fnr,2), round(fpr,2))
