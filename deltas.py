import json
import csv
from statistics import mode, mean

with open('llm_data_1.json', 'r') as file:
    participants = json.load(file)
pass

adherentQsetIDs = []


with open('text_questions.csv', 'r') as file:
    next(file)
    for line in file:
        columns = line.strip().split(',')
        questionSetID, gen_num, qIDs, meanOriginalOrder, meanAlternateOrders, status = columns
        if status.lower() in ['filtered', 'adherent']:
            adherentQsetIDs.append(f"{gen_num}_{questionSetID}_0")
pass

def getP1Keys(input_string, end=5):
    base = input_string[:-1]
    return [f"{base}{i}" for i in range(1, end + 1)]

pass
with open('scratch.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Participant', 'adherhent_Q#', 'P2_rating', 'P1_5_Q_avg', 'P1_Q_#', 'delta'])

    for i, participant in enumerate(participants):
        pass
        p2r = {item[0]: item[1] for item in participant["dedup_ordered_answers_2"]}
        p1r = {item[0]: item[1] for item in participant["dedup_ordered_answers_1"]}
        pass
        for qsetID in adherentQsetIDs:
            pass
            p1r_ = [p1r.get(key) for key in getP1Keys(qsetID) if p1r.get(key) is not None]
            p1rLen = len(p1r_) if p1r_ else 0
            if p1rLen != 0 and p1rLen != 5:
                print(p1rLen, p1r_)
            pass
            p1r_ = sum(p1r_)/len(p1r_) if p1r_ else None
            p2r_ = p2r[qsetID]
            delta = p2r_ - p1r_ if p1r_ else "None"
            pass
            row = [
                i,
                qsetID[:-2],
                p2r_,
                p1r_ if p1r_ else "None",
                p1rLen,
                delta
            ]
            writer.writerow(row)
print(f"{count}/{tot}")