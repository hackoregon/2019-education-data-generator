from factory import factory
factory = factory.Factory(5, "demo_dist")
for pupil in factory.student_population:
    print(pupil.id_num)