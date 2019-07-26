# these are based on "2015 NWEA MAP Growth normative data"
# (cf. team-education/Data Elements/2015-normative-data.pdf)
# index is the grade, 0 = kindergarten
YEAR_START_NORMS = [
    {
        "reading": {"mu": 141.0, "sigma": 13.54},
        "math": {"mu": 140.0, "sigma": 15.06}
    },
    {
        "reading": {"mu": 160.7, "sigma": 13.08},
        "math": {"mu": 162.4, "sigma": 12.87}
    },
    {
        "reading": {"mu": 174.7, "sigma": 15.52},
        "math": {"mu": 176.9, "sigma": 13.22},
        "english": {"mu": 174.5, "sigma": 16.58}
    },
    {
        "reading": {"mu": 188.3, "sigma": 15.85},
        "math": {"mu": 190.4, "sigma": 13.10},
        "english": {"mu": 189.4, "sigma": 15.20},
        "science": {"mu": 187.5, "sigma": 11.74}
    },
    {
        "reading": {"mu": 198.2, "sigma": 15.53},
        "math": {"mu": 201.9, "sigma": 13.76},
        "english": {"mu": 198.8, "sigma": 14.66},
        "science": {"mu": 194.6, "sigma": 11.16}
    },
    {
        "reading": {"mu": 205.7, "sigma": 15.13},
        "math": {"mu": 211.4, "sigma": 14.68},
        "english": {"mu": 205.6, "sigma": 13.87},
        "science": {"mu": 200.2, "sigma": 11.06}
    },
    {
        "reading": {"mu": 211.0, "sigma": 14.94},
        "math": {"mu": 217.6, "sigma": 15.53},
        "english": {"mu": 210.7, "sigma": 13.79},
        "science": {"mu": 204.3, "sigma": 11.54}
    },
    {
        "reading": {"mu": 214.4, "sigma": 15.31},
        "math": {"mu": 222.6, "sigma": 16.59},
        "english": {"mu": 214.0, "sigma": 13.82},
        "science": {"mu": 207.2, "sigma": 11.92}
    },
    {
        "reading": {"mu": 217.2, "sigma": 15.72},
        "math": {"mu": 226.3, "sigma": 17.85},
        "english": {"mu": 216.2, "sigma": 14.17},
        "science": {"mu": 210.3, "sigma": 12.28}
    },
    {
        "reading": {"mu": 220.2, "sigma": 15.68},
        "math": {"mu": 230.3, "sigma": 18.13},
        "english": {"mu": 218.4, "sigma": 14.15}
    },
    {
        "reading": {"mu": 220.4, "sigma": 16.85},
        "math": {"mu": 230.1, "sigma": 19.60},
        "english": {"mu": 218.9, "sigma": 15.04}
    },
    {
        "reading": {"mu": 222.6, "sigma": 16.75},
        "math": {"mu": 233.3, "sigma": 19.95},
        "english": {"mu": 221.5, "sigma": 14.96}
    }
]

# differences are from end of previous year to beginning of indexed year.
YEAR_GROWTH_NORMS = [
    {
        "reading": {"mu": 17.1, "sigma": 8.11},
        "math": {"mu": 19.1, "sigma": 7.59}
    },
    {
        "reading": {"mu": 16.8, "sigma": 8.09, "diff": 2.6},
        "math": {"mu": 18.4, "sigma": 7.45, "diff": 3.3}
    },
    {
        "reading": {"mu": 14.0, "sigma": 8.20, "diff": -2.8},
        "math": {"mu": 15.2, "sigma": 7.11, "diff": -3.9},
        "english": {"mu": 15.2, "sigma": 9.83}
    },
    {
        "reading": {"mu": 10.3, "sigma": 7.59, "diff": -0.4},
        "math": {"mu": 13.0, "sigma": 6.47, "diff": -1.7},
        "english": {"mu": 10.6, "sigma": 7.69, "diff": -0.3},
        "science": {"mu": 8.0, "sigma": 8.02}
    },
    {
        "reading": {"mu": 7.8, "sigma": 7.05, "diff": -0.4},
        "math": {"mu": 11.6, "sigma": 6.41, "diff": -1.5},
        "english": {"mu": 7.9, "sigma": 6.90, "diff": -1.2},
        "science": {"mu": 6.4, "sigma": 7.19, "diff": -0.8}
    },
    {
        "reading": {"mu": 6.1, "sigma": 7.15, "diff": -0.2},
        "math": {"mu": 9.9, "sigma": 6.80, "diff": -2.1},
        "english": {"mu": 5.8, "sigma": 6.78, "diff": -1.1},
        "science": {"mu": 5.5, "sigma": 7.13, "diff": -0.8}
    },
    {
        "reading": {"mu": 4.8, "sigma": 7.19, "diff": -0.8},
        "math": {"mu": 7.7, "sigma": 6.75, "diff": -3.8},
        "english": {"mu": 4.5, "sigma": 6.84, "diff": -0.8},
        "science": {"mu": 4.3, "sigma": 7.14, "diff": -1.4}
    },
    {
        "reading": {"mu": 3.7, "sigma": 7.11, "diff": -1.4},
        "math": {"mu": 6.0, "sigma": 6.55, "diff": -2.7},
        "english": {"mu": 3.6, "sigma": 6.61, "diff": -1.3},
        "science": {"mu": 3.7, "sigma": 7.10, "diff": -1.4}
    },
    {
        "reading": {"mu": 2.8, "sigma": 8.19, "diff": -1.0},
        "math": {"mu": 4.6, "sigma": 7.66, "diff": -2.3},
        "english": {"mu": 2.9, "sigma": 7.22, "diff": -1.4},
        "science": {"mu": 3.2, "sigma": 7.56, "diff": -0.6}
    },
    {
        "reading": {"mu": 1.7, "sigma": 8.87, "diff": 0.1},
        "math": {"mu": 3.1, "sigma": 8.15, "diff": -0.6},
        "english": {"mu": 2.0, "sigma": 7.79, "diff": -0.6}
    },
    {
        "reading": {"mu": 0.7, "sigma": 9.66, "diff": 0.5},
        "math": {"mu": 2.3, "sigma": 8.92, "diff": -3.3},
        "english": {"mu": 1.2, "sigma": 8.61, "diff": -1.5}
    }
]

# cf. Assessment Score Reporting Category Descriptions by Subject
SRC_INDICES = {
    "english": [1, 2, 3, 4],
    "reading": [1, 2, 3, 4],
    "math": [1, 2, 3],
    "science": [1, 2, 3]
}