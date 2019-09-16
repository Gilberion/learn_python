students_scores = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
 {'school_class': '4б', 'scores': [4,4,5,3,4]},
 {'school_class': '4в', 'scores': [3,3,2,4,2]},
 {'school_class': '4г', 'scores': [3,2,2,4,5]}]

all_intrm_scores = 0
all_intrm_len = 0

for intrm_scores in students_scores:
    intrm_scores = (intrm_scores['scores'])
    avrg_scores=sum(intrm_scores)/len(intrm_scores)
    print(avrg_scores)
    all_intrm_scores += sum(intrm_scores)
    all_intrm_len += len(intrm_scores)

#print(all_intrm_scores)
#print(all_intrm_len)
all_avrg_scores = all_intrm_scores/all_intrm_len
print('Средний балл по школе', all_avrg_scores)  