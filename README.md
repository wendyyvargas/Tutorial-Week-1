# Week-1

Access the slides that provide program specifications on Google Classroom. 

Use this guide to help you set up your environment (also provided in Google Classroom). 

# Install VSCode
1. Go to  https://code.visualstudio.com/
2. Download it for your OS.
3. Run the installer
4. During setup, check
  - Add to PATH
  - Register Code as editor for supported file types
5. Let installation finish and open VSCode

# Installing Python
1. Go to https://www.python.org/downloads/
2. Download the latest version for your OS
  - IMPORTANT: Check ✅ "Add Python to PATH" during installation
3. Let it install
4. Install the Python Extension in VSCode
  - Open VSCode → Go to Extensions tab → search for “Python” → install the one from Microsoft.
5. Select a Python Interpreter (First Time Only) by...
6. Open a .py file
7. Look at the bottom-left corner or press Ctrl+Shift+P → type “Python: Select Interpreter”
8. Choose the right one (usually ends in python.exe or has your virtualenv name)

# Creating GitHub account
1. Go to https://github.com/join  and sign up
2. Create a Personal Access Token
3. Go to https://github.com/settings/tokens
4. Click "Tokens (classic)" -> "Generate new token"
5. Give your token a name
6. Set expiration date (optional)
7. Check the permissions: repo, read:user, and user:email
6. Generate token and store it somewhere safe. 

# Installing Git
1. Go to  https://git-scm.com/downloads
2. Choose your OS and download the installer. 
3. Run the installer with default options and make sure "Add Git to PATH" is selected
4. If on Windows, make sure to check the option "Git from the command line and also from 3rd-party software"

# Setting up Git
1. Open your terminal and type: git --version
2. If you see a version number, you are good! If not, head back to Installing Git steps.
3. Time to configure your identity. 
  git config --global user.name "YOUR NAME"
  git config --global user.email "EMAIL@EMAIL.COM"
4. Go back to GitHub and create a repository  
    - make it private
    - name it "TEST"
    - Add a README file
5. Copy the repository URL
  - green "Code" button -> HTTPS link
6. Open VSCode and type "git clone URL"
7. Make any change to the README file
8. Check the status of your file (git status)
9. Use "git add FILENAME" to add files to commit
10. Commit the changes by "git commit -m "Commit Message"
11. Push the changes using "git push"
  - being first time, will have to do "git push -u origin main" instead
12. Now git will ask for your username and token, enter those
13. !! Git will offer to save token, CLICK YES
14. Go back to GitHub, refresh repository page, and changes should be there. 

# Setting up for Project
We will provide base code for projects, to make it a bit easier you. 
We store all those files in repositories (think of it as the place in the cloud where we can keep our files)
You then can take those files and can work on them on your own local computer, this is how you do that.

1. go to this weeks repository link
2. On top right, click Fork, and then Create Fork
  - this created a version/copy of OUR repo under your name, you now can work on it locally without affecting our original

How to work on it locally on your computer. 
1. Go your repo. 
2. Click green button, and copy the HTTPS link. 
3. Go to VSCode and choose the folder where you will work on this.
4. In the terminal, use, git clone URL
5. You now have a version of your repo locally. 


# Git Commands
Since this is an easy lab - lets learn how to branch in this one. 
You do have to do this, but its recommended to learn how to branch, good technique to have :)
You do not have to branch in every project, but its just cleaner. 
Branching is a way to work on code without affecting your current version. 
Take it like this, your main branch works great, but you need to add another function, but need to test it and do not want bugs added to alreadt working code. So you make a separate version where you can, and later merge this new version back to the original. 

In this lab:
1. use git branch NAME to create a new branch
2. use git checkout NAME to move into the new branch
3. make changes - aka build a function
4. use git status to check what files you need to add
5. use git add FILENAME to add files to a commit
6. use git commit -m "MESSAGE" to commit these changes
7. use git push so that you can see these changes online (might have to do upstream or origin)
8. head to github and go to pull requests
9. check the changes, fix any conflicts, and merge it. 
10. head back to VSCode and use git checkout main to head back to working main branch
11. use git pull to get all changes that you just pushed. 
12. your main branch is up to date :)

This is usually the struture.
Without branching:
1. Fork
2. Clone
3. Make changes
4. add changes
5. commit changes
6. push changes

With branching:
1. Fork
2. clone
3. Make new branch and checkout to it
4. make changes
5. add changes
6. commit changes
7. push changes
8. in github, merge changes
9. in vscode, head back to main branch and pull changes

It is good practice, especially if working in a team, to always git pull before working. 
