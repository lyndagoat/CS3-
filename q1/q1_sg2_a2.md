#Activity 2: Code Quality Assessment

Annex C
Code Quality Assessment Worksheet

Section: 9 BALINGKILAT                          Score:____________

C# / Name: #28 OCAMPO, LYNDZEE RAYE G.      Date: 08/14/2026


Questions with Checklists
1. Efficiency
Which algorithm is faster when the list of numbers is very large? Why?
- PseudoCode 1 is definitely the faster algorithm because it checks the number once only.
  It then compares all the numbers and keeping the biggest one out of all of them. On the other
  hand, PseudoCode2 has two loops which makes the algorithm check all the numbers a lot of times.

PseudoCode 1

/ : Does the algorithm use one loop or two nested loops?

x : Does the algorithm repeat work unnecessarily?

PseudoCode 1 : Which algorithm finishes in fewer steps?

PseudoCode2

/ : Does the algorithm use one loop or two nested loops?

/ : Does the algorithm repeat work unnecessarily?

PseudoCode 1 : Which algorithm finishes in fewer steps?


Checklist to guide your answer:
2. Readability

Which algorithm is easier to understand at first glance? What makes it clearer?
- PseudoCode 1 is easier to understand at first glance because it's simple, short, and direct.
  It only uses one loop which makes it easier for the user to use, it just checks all of the numbers and
  replaces the max when it finds a bigger number.

Checklist to guide your answer:

PseudoCode 1

/ : Are variable names meaningful (e.g., max vs. bigger)?

Simple : Is the logic simple or complicated?

/ : Are there fewer lines of code?

PseudoCode 2

/ : Are variable names meaningful (e.g., max vs. bigger)?

Complicated : Is the logic simple or complicated?

x : Are there fewer lines of code?

3. Maintainability
If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?
- PseudoCode 1 would probably be easier to update because it's very simple, short, and only uses one loop.
  If you want to add a new feature like finding both max and min, you can just add another variable called
  min and check for the smallest number in the same loop. 

Checklist to guide your answer:

PseudoCode 1

/ : Is the structure straightforward?

x : Would adding new steps break the code easily?

/ : Is there less chance of errors when updating?

PseudoCode 2

x : Is the structure straightforward?

/ : Would adding new steps break the code easily?

x : Is there less chance of errors when updating?

4. Testability
Which algorithm is easier to test with different inputs? Why?
- PseudoCode 1 is easier to test with different inputs because it has a simpler process
  than PseudoCode 2. 

Checklist to guide your answer:


PseudoCode 1

/ : Can you test with small lists easily?

/ : Does the algorithm have fewer conditions to check?

/ : Is the output predictable and clear?

PseudoCode 2

/ : Can you test with small lists easily?

x : Does the algorithm have fewer conditions to check?

/ : Is the output predictable and clear?


5. Security
Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?
- The algorithm should check if the list is empty and make sure that the user inputs numbers
  only by using int.
  
Checklist to guide your answer:

PseudoCode 1

x : Does the algorithm check if the list is empty?

x : Does it handle invalid inputs (like letters instead of numbers)?

x : Does it avoid crashing when inputs are unusual?

PseudoCode 2

x : Does the algorithm check if the list is empty?

x : Does it handle invalid inputs (like letters instead of numbers)?

x : Does it avoid crashing when inputs are unusual?

 

6. Final Answer
Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer
- The better algorithm that I would use is PseudoCode 1. It's easier to understand, use, and much simpler. Not only does it just use one loop,
  it also doesn't repeat any work that is not that important. However, the algorithm would've been better if it also considered
  user errors such as not inputting a number, if the list is empty, and etc. 

