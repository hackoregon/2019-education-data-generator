from .student import Student
import numpy as np
import csv


class Factory:
    """This class produces fake data using the student class contained
    in this module. The constructor takes a number to be used as the size
    of the student population. The constructor also takes a distribution to
    be used for applying demographics characteristics of the students across
    the generated population. TODO: determine the type of the output to be generated."""

    def __init__(self, count, demographic_distribution, strategy):
        """
        Student Params
            id_num: The ID number of the student (proxy for SSN, int)
            year_k: The year the student started kindergarten
            gender: The gender of the student, "m" or "f" for now (string)
            race: A code for the student's race (int)
            ell: English language learner (boolean)
            poverty: Whether the student receives free/reduced lunches (boolean)
            disabled: Whether the student has any disabilities (boolean)
            strategy: How to use the above features to scale RIT scores (Strategy)
        """
        self.count = count
        self.demo = demographic_distribution
        self.strategy = strategy
        self.student_population = []
        years = list(range(2000, 2015))
        for i in range(count):
            if np.random.uniform() < self.demo['gender']:
                gender = 'f'
            else:
                gender = 'm'
            race_rand = np.random.uniform(0, sum(self.demo['race']['distribution']))
            race_code = 0
            cum_sum = 0
            for race_prop in self.demo['race']['distribution']:
                cum_sum += race_prop
                if race_rand < cum_sum:
                    break
                race_code += 1
            self.student_population.append(Student(
                id_num=i,
                year_k=np.random.choice(years),
                gender=gender,
                race=race_code,
                ell=np.random.uniform() < self.demo['race']['ell'][race_code],
                poverty=np.random.uniform() < self.demo['race']['poverty'][race_code],
                disabled=np.random.uniform() < self.demo['race']['disability'][race_code],
                strategy=self.strategy
            ))


    def pretty_print(self, head=None):
        if head is None:
            head = len(self.student_population)
        for person in self.student_population[:head]:
            person.pretty_print()


    def print_to_file(self, csv_file_name="csv_output.csv"):
        headers = ["Student_id", "race", "year_started", "ell", "pov", "dis"]
        for year in range(12):
            y = str(year)
            #'GRADE', 'ENGLISH', 'MATH', 'READING', 'SCIENCE')
            headers += ["english_" + y, "math_" + y, "reading_" + y, "science_" + y] 

        with open(csv_file_name, 'w+') as csv_file:
            csv_filewriter = csv.writer(csv_file, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            #PRINT HEADERS
            csv_filewriter.writerow(headers)
            for person in self.student_population:
                person.print_to_file(csv_filewriter)


    def print_demos(self):
        men = 0
        women = 0
        races = [0, 0, 0, 0, 0, 0, 0]
        pov = 0
        pbr = [0, 0, 0, 0, 0, 0, 0]
        ell = 0
        ebr = [0, 0, 0, 0, 0, 0, 0]
        dis = 0
        dbr = [0, 0, 0, 0, 0, 0, 0]
        for stud in self.student_population:
            if stud.gender == 'm':
                men += 1
            else:
                women += 1
            races[stud.race] += 1
            if stud.poverty:
                pov += 1
                pbr[stud.race] += 1
            if stud.ell:
                ell += 1
                ebr[stud.race] += 1
            if stud.disabled:
                dis += 1
                dbr[stud.race] += 1
        pbr_pct = [round(p/t, 2) for (p, t) in zip(pbr, races)]
        ebr_pct = [round(e/t, 2) for (e, t) in zip(ebr, races)]
        dbr_pct = [round(d/t, 2) for (d, t) in zip(dbr, races)]
        print("Generated student demographics")
        print(f"Student count: {len(self.student_population)}")
        print(f"Gender breakdown: Men = {men}, Women = {women}")
        print(f"Racial breakdown: white = {races[0]}, black = {races[1]}, hisp = {races[2]}, asian = {races[3]}")
        print(f"                  islander = {races[4]}, native Am = {races[5]}, multi = {races[6]}")
        print("-"*60)
        print(f"Poverty count: {pov}")
        print(f"Racial breakdown: white = {pbr[0]}, black = {pbr[1]}, hisp = {pbr[2]}, asian = {pbr[3]}")
        print(f"                  islander = {pbr[4]}, native Am = {pbr[5]}, multi = {pbr[6]}")
        print(f"Racial percentages: white = {pbr_pct[0]}, black = {pbr_pct[1]}, hisp = {pbr_pct[2]}, asian = {pbr_pct[3]}")
        print(f"                  islander = {pbr_pct[4]}, native Am = {pbr_pct[5]}, multi = {pbr_pct[6]}")
        print("-"*60)
        print(f"English learner count: {ell}")
        print(f"Racial breakdown: white = {ebr[0]}, black = {ebr[1]}, hisp = {ebr[2]}, asian = {ebr[3]}")
        print(f"                  islander = {ebr[4]}, native Am = {ebr[5]}, multi = {ebr[6]}")
        print(f"Racial percentages: white = {ebr_pct[0]}, black = {ebr_pct[1]}, hisp = {ebr_pct[2]}, asian = {ebr_pct[3]}")
        print(f"                  islander = {ebr_pct[4]}, native Am = {ebr_pct[5]}, multi = {ebr_pct[6]}")
        print("-"*60)
        print(f"Disabled student count: {dis}")
        print(f"Racial breakdown: white = {dbr[0]}, black = {dbr[1]}, hisp = {dbr[2]}, asian = {dbr[3]}")
        print(f"                  islander = {dbr[4]}, native Am = {dbr[5]}, multi = {dbr[6]}")
        print(f"Racial percentages: white = {dbr_pct[0]}, black = {dbr_pct[1]}, hisp = {dbr_pct[2]}, asian = {dbr_pct[3]}")
        print(f"                  islander = {dbr_pct[4]}, native Am = {dbr_pct[5]}, multi = {dbr_pct[6]}")
