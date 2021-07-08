# python_stuff
To run code, create a script.py file with your code inside a folder named after your username. Then go to .github/wokflows/python-app.yml and add the following code to the bottom of the file.
```yml
name: execute py script for YOUR_USERNAME
  run: |
    python YOUR_USERNAME/script.py
```
Replace 'YOUR_USERNAME' with your GitHub username. Once you have done this, go to your script and find its current CI status. Click on 'Details', next to the process named 'Python application / build (push)'. Scroll and find your name amongst all the processes. Open it up. The output is listed there.

# Already installed libraries
There are a few libraries that are already installed. The following is a list of all pre-installed libraries (including dependencies). This list also contains links to the docs for each library.
* NumPy ([Docs](https://numpy.org/doc/))
* SciPy ([Docs](https://www.scipy.org/docs.html))
* MatPlotLib ([Docs](https://matplotlib.org/stable/contents.html))
* Pandas ([Docs](https://pandas.pydata.org/pandas-docs/stable/))
* Scikit-Learn ([Docs](https://scikit-learn.org/stable/user_guide.html))
