def build_containers(students):
    """Будує словник груп та set груп з відмінниками."""
    # Словник {група: список студентів}
    group_dict = {}
    for s in students:
        group_dict.setdefault(s['group'], []).append(s['name'])

    # Set груп з відмінниками (усі оцінки >= 90)
    excellent_groups = {
        s['group'] for s in students if all(g >= 90 for g in s['grades'])
    }

    return group_dict, excellent_groups