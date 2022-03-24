# Activity 7: Fast Arrays
![GitHub Classroom Workflow](../../workflows/GitHub%20Classroom%20Workflow/badge.svg?branch=main) ![Points badge](../../blob/badges/.github/badges/points.svg)


## Problem

Use numpy arrays to calculate for a vector `b` (numpy array) of length `N`

```
y[i] = 0.5 * (b[i−1] + b[i+1])
```

and set 
```
y[0] = y[N−1] = end
```
where `end` is a number.

Write a function `avg_neighbors(b, end=100)` that takes `b` as input
and returns `y` as output. Add your code to the file `exercise.py`.


## Background

See the notebook
[14_PDEs/numpy_arrays.ipynb](https://github.com/Py4Phy/PHY432-resources/blob/main/14_PDEs/numpy_arrays.ipynb)
for notes on how to use array operations to avoid writing loops when
working on NumPy arrays.


## Workflow

The workflow for submitting homeworks in this class will be

1. **Follow the repository creation link** (on Canvas). It will be
   posted in the current Module as **Activity NN** where "NN" is the
   number of the activity. The link looks like
   `https://classroom.github.com/a/FuNNyleTT3rs`. This will create
   your personal, private repository, named `activity-NN-yourname`
   where _yourname_ is your GitHub username and NN is the activity
   number.
2. In the shell on your computer, **clone the repository to your own
   computer**, using the specific repository name:

        git clone  https://github.com/Py4Phy/activity-NN-yourname.git
	  
   This creates a directory `activity-NN-yourname` on your computer. This is
   your *local repository*.

3. **Navigate to the local repository**

        cd activity-NN-yourname

4. **Solve the problem**: read the instructions in the assignment file
   and do what you need to do, e.g., add code, create files and
   directories, etc.
   
5. **Add your changes** (can be done as often as you like):

        git add -A .
	  
6. **Commit your changes** (can be done as often as you like):

        git commit -m "updated assignment"
	  
   (Write a more expressive message than "updated assignment".)
   
7. **Push your changes** to GitHub (can be done as often as you like):

        git push

   This will synchronize your repository in the cloud on GitHub with
   your local repository. When you push the changes, you **submit your
   homework**. You can push changes as often as you like until the
   submission deadline. 
   
   **Only changes in your GitHub repository until the deadline count
   for grading**.
   
8. **Check autograding**: Your homework repository on GitHub has "pull
   request" named **Feedback**. Navigate to it in your webbrowser and
   look at the **checks**. If you have a _green_ checkmark then all
   the tests passed. If you have _red_ X then some tests failed and
   you should look at the output of the tests to see what exactly
   failed. This will initially look dauting and complicated but you'll
   quickly learn what to look for.
   
   There is more help available in [Viewing autograding
   results](https://docs.github.com/en/education/manage-coursework-with-github-classroom/learn-with-github-classroom/view-autograding-results).
   
   Alternatively, run the tests locally with
   ```
   pytest --tb=short
   ```
   This will provide you a quick view of what is failing (but will not
   compute points.)
   
9. If you have errors then fix your submission and resubmit: `GOTO 4`

10. Else: your done


