Answer the following questions in a new **UNDERSTAND.md** file:
- What Python interpreter are you running? 
- Do we need a conda virtual environment? Justify your answer. 
- VS Code reports **problems** for each of the Python module.  
    - How many problems are reported for each moduel? 
    - What generates these problems and wny?
- How can the problems be fixed? 
    - Describe your solution to fixing these problems. 
- What categories of changes have you or VS Code made to the code to fix the problems? 

### Answers and questions ###
1. What Python interpreter are you running?
Ans. I'm using the python 3.11.5

 2. Do we need a conda virtual environment? Justify your answer.
 Ans. * The virtual environment allow you to manage the projects and each project can have separately have its own enverionments with  installed packages it can conflicts between different version.
      * The  virtual envrionment running it on a different machine and virtual environment can help you to ensure that it can runs the same way in the one machine.
      * And it also usefull to update the new packages are the Python version without affecting the pyhon version.
The virtual envrionment is so helpfull inorder to manage the packages and python envrionments to do in a different projects  and it also gives the different python unique versions and libraries and preventing the conflicts in between the versions and packages.

3.  VS Code reports **problems** for each of the Python module.
Ans. The VS Code reports problems for each of the python module by using the python extension and other packages and sometimes this could inlude syntax errors the problem panel will show where the error is and it will show the where the error getting.

4. How many problems are reported for each moduel?
Ans. There are three moduel are they a_star.py, graph.py and main.py
    1. a_star.py
    total errors: 206 errors
    
    2.graph.py
    total errors: 63 errors

    3.main.py
    total errors: 23 errors

5. What generates these problems and why?  
Ans. It was generate by a linter or a static code analysis tools here's why these tools generate these problems:
    1. Syntax errors: These are issues that prevent the code from running correctly.
    2. stylistic issues: it like the indentation errors or unsued imports
    3. Potentail bugs: If you are using the undefined variables or deprecated function it will get problems.
  by addressing all these problems we can make code easier to read and improve the quality of the code.

6. How can the problems be fixed? 
Ans. In Visual Studio Code simply navigate to the each problems panel whuch gives the description of the particular problem and it location in the certain code by using the test editor or edit the code in the particular errors to fix the errors or problems and again save the cod recheck the code untill fixed the problem and it will no longer apper in the problems panel.

7. Describe your solution to fixing these problems.
Ans. First i identefied the problems in Visual Studio and I understand the problem where the errors are getting like which line it coming and i opened the problems and i edit all the syntax errors and adjusting the code and changing the to avoid the errors and after i save the code and i recheck the problems if the problems was not solved and i tried the differernt ways to fix the problems by changing the lines and correcting the lines and indentation errors.

8. What categories of changes have you or VS Code made to the code to fix the problems? 
Ans. In the Visual Studio code i used the different types of extension to fix the problems like i used the black formate to formate all the code to fix the problems and i used editor in the visual studio code by hovering the modules and erros to understand the code and correcting the Syntax correction like correcting the variable name and fixing the incorrect indentation and removing the unnecessary whitespace and reordering the imports and removing the unused variables function or imports and adding the docstrings and improveing the code. 