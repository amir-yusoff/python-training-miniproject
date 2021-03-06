# Mini project for Certified Python Professional by IR Academy (1/3/2022 - 7-3/2022)

The data generated is randomised and might have some discrepencies.

- [Mini project for Certified Python Professional by IR Academy (1/3/2022 - 7-3/2022)](#mini-project-for-certified-python-professional-by-ir-academy-132022---7-32022)
  - [How to use](#how-to-use)
  - [Findings](#findings)
    - [Student age distribution](#student-age-distribution)
    - [Student origin state](#student-origin-state)
    - [Student results](#student-results)
    - [Student marks](#student-marks)
    - [Overall best student](#overall-best-student)
    - [Best and worst scoring subjects](#best-and-worst-scoring-subjects)
      - [Graph of Sum of Marks](#graph-of-sum-of-marks)
      - [Graph of Mean of Marks](#graph-of-mean-of-marks)

</br>
</br>

## How to use

- You could clone the repository or download it as a zip file.
- To run in your own computer, make sure to change the file paths to your appropriate folders. For example, to connect to your own sql.server, change the values in the `{YOUR-SQL-SERVER-HERE}` line in files `main.py` or `student-management-system.ipynb`.
  
  ```python
  conn = pyodbc.connect('Driver={SQL Server};'
                      'Server={YOUR-SQL-SERVER-HERE};'
                      'Database=training_project;'
                      'Trusted_Connection=yes;')
  ```

- I used batch import of data into the SQL server from a csv file. It could be done in python using the `data/csv-to-mssql.ipynb` file (might have some errors atm), or using an SQL query provided in `db-query.sql`.
- Analytics is all done in `analytics.ipynb` and generated graphs are saved in `/data` folder.
- Prototyping is done in `student-management-system.ipynb` and then consolidated into `main.py`
- To run the program, you could open a Terminal or PowerShell (hold control and right click on this folder, then click run PowerShell here) window in your directory. Run `python main.py` to execute the program.
  

## Findings

### Student age distribution

From the data, this is the distribution of the ages of which the students. It is found that the youngest students are of age 23, while the oldest is of age 43. Students of age 25 compromises of the most number.

![](./output/student-age-distribution.png)

### Student origin state

From the data, this is the distribution of the states of which the students resides in. Most of the students live in Kuala Lumpur, while the least are from Negeri Sembilan, Terengganu, and Sarawak respectively.

![](./output/student-state.png)

### Student results

From the data, this is the distribution of the student results. 23 passed and 7 failed.

![](./output/student-result.png)

### Student marks

To get the lowest and the highest marks and the correponding students, this code is used:

```python
for i in index[2:]:
    print(i)

    max = df_marks[i].idxmax()
    max_name = df_marks['Std_Name'][max]
    max_marks = df_marks[i][max]
    
    min = df_marks[i].idxmin()
    min_name = df_marks['Std_Name'][min]
    min_marks = df_marks[i][min]

    print('Highest:\t',max_name, ',', max_marks)
    print('Lowest:\t',min_name, ',', min_marks)
    print()
```

From the data, these are my findings:

![](./output/student-marks.png)

### Overall best student

To get the overall best student, this code is used:

```python
top = df['Total'].idxmax()
name = df['Std_Name'][top]

print('Best student: ', name)
```
![](./output/student-marks-best.png)

### Best and worst scoring subjects

From the data, this is the distribution of the sum of marks of all subjects. This is to visualise and analyse which subjects are the students best and worst performing in. Code below is to get the sum of each subject columns

```
sum_of_cols = df_marks_only.sum(axis=0)
print(sum_of_cols)
```
![](./output/marks-sum.png)

Since the data obtained is fairly small, we could see that Students best perform in Arts and performs worst in Science


#### Graph of Sum of Marks
![](./output/marks-sum-graph.png)

#### Graph of Mean of Marks

```python
mean_of_cols = df_marks_only.mean(axis=0)

formatted_output = mean_of_cols.apply(lambda x: '{:.2f}'.format(x))
print(formatted_output)
```

![](./output/student-marks-mean.png)

![](./output/marks-mean-graph2.png)


