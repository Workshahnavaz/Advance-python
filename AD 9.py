def mergedisc(score1, score2):
    merge = {}
    
    def updatescore(score_in):
        for student, subjects_scores in score_in.items():
            if student not in merge:
                merge[student] = {}
            for subject, score in subjects_scores.items():
                if subject not in merge[student]:
                    merge[student][subject] = score
                else:
                    merge[student][subject] = max(merge[student][subject], score)
    
    updatescore(score1)
    updatescore(score2)

    average_scores = []
    for student, subjects_scores in merge.items():
        total_score = sum(subjects_scores.values())
        num_subjects = len(subjects_scores)
        average_score = total_score / num_subjects if num_subjects > 0 else 0
        average_scores.append((student, average_score))

    return average_scores

score1 = {
    'Soham': {'math': 85, 'Science': 92},
    'Sanket': {'math': 79, 'Science': 85},
    'Rutvik': {'math': 95, 'Science': 90}
}

score2 = {
    'Soham': {'math': 88, 'Science': 91},
    'Sanket': {'math': 89, 'Science': 80},
    'Rutvik': {'math': 78, 'Science': 84}
}

result = mergedisc(score1, score2)
print(result)
