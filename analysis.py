import json
import csv
from statistics import mode, mean

with open('llm_data_1.json', 'r') as file:
    participants = json.load(file)
pass

with open('agreement.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['participant#', 'phase 1 human mean', 'phase 1 human mode', 'phase 1 human min', 'phase 1 human max', 'phase 1 llm mean', 'phase 1 llm mode', 'phase 1 llm min', 'phase 1 llm max', 'phase 1 correlation coefficient', 'phase 1 p-value', 'phase 2 human mean', 'phase 2 human mode', 'phase 2 human min', 'phase 2 human max', 'phase 2 llm mean', 'phase 2 llm mode', 'phase 2 llm min', 'phase 2 llm max', 'phase 2 correlation coefficient', 'phase 2 p-value'])

    for i, participant in enumerate(participants):
        pass
        p1r_hu = [x[1] for x in participant["dedup_ordered_answers_1"]]
        p2r_hu = [x[1] for x in participant["dedup_ordered_answers_2"]]
        p1r_ai = sum([x[1:] for x in participant["dedup_ordered_answers_1_ai"]],[])
        p2r_ai = sum([x[1:] for x in participant["dedup_ordered_answers_2_ai"]],[])
        pass
        row = [
            i,
            mean(p1r_hu),
            mode(p1r_hu),
            min(p1r_hu),
            max(p1r_hu),
            mean(p1r_ai),
            mode(p1r_ai),
            min(p1r_ai),
            max(p1r_ai),
            participant['pearsons_1'][0],
            participant['pearsons_1'][1],
            mean(p2r_hu),
            mode(p2r_hu),
            min(p2r_hu),
            max(p2r_hu),
            mean(p2r_ai),
            mode(p2r_ai),
            min(p2r_ai),
            max(p2r_ai),
            participant['pearsons_2'][0],
            participant['pearsons_2'][1]
        ]
        writer.writerow(row)