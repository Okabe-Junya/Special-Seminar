# Special Seminar

<p align="left">
    <a href="#">
        <img src="https://img.shields.io/badge/-archive-red">
    </a>
    <a href="https://github.com/Okabe-Junya/Special-Seminar/blob/main/README.md">
        <img src="https://img.shields.io/badge/link-Japanese-blue">
    </a>
</p>

## Abstract

This is an archive of the [Special Seminar](https://kdb.tsukuba.ac.jp/syllabi/2021/GB13312/en/) on Information Technology taken in the second year of the undergraduate course. The theme of the exercise was "Optimization of Hub Placement in Airline Networks". The advisor was [Mr. Koji Hasebe](http://www.cs.tsukuba.ac.jp/~hasebe/).

### Supplement

This is a two-credit course for first- to third-year undergraduates, in which students take part in exercises (≒ research activities) for about six months on a theme of their own choosing. However, unlike research activities such as graduation research, students are not required to be  **Novelty** (of course, they are required to summarize the contents of the exercise and submit a report).

## Contents

I conducted an exercise on the **Hub Location Problem**, which minimizes the total cost of the entire network by locating several hub airports in the airline network. First, I surveyed papers on the Hub Location Problem. In parallel, I studied mathematical optimization. Then, I extended the existing model, proposed a new model, and derived its exact solution. A mathematical optimization solver, [Gurobi Optimizer](https://www.gurobi.com/products/gurobi-optimizer/), was used to derive the exact solution.

## Schedule

The exercises begin in June and end in January (February) of the following year. Basically, a (group) meeting is held every two weeks to report the progress. After that, receive advice and questions. Individual meetings with advisors are held as needed.

### April~May

Contacting the advisor. Determination of the place of assignment.

### June

Start of the exercise. Determination of the topic of the exercise and a brief survey of the relevant field.

### July~September

Interim presentation (report on the exercise theme and current progress). Start of the study of mathematical optimization. Survey of papers in the field.

### October~November

Create a new model and implement the program.

### December~January

Preparation of presentations and reports for the final presentation. Fixing minor bugs in the source code.

### February

Submission of the [Final Report](https://github.com/Okabe-Junya/Special-Seminar/blob/main/Publications/Final_Report.pdf). End of the exercise.

## Directory Structure

This Repository has the following directory structure.

```text
.
├── Publications
│   ├── Final_Presentation.pdf
│   └── Final_Report.pdf
├── README.md
├── README_en.md
└── src
    ├── README
    ├── draw.py
    ├── my_def.py
    └── res
```

In the `Publications` folder, there are presentation slides of the final presentation and the final report. In the `src` folder, there is the code implemented based on the proposed model.

