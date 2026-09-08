# The Bash Shell

> Part of **Topic 2: Bash and Git** · source item type: WikiPage

---
## Introduction

When conducting Data Science (or programming in general), it’s helpful to get oriented with the command line, or bash shell. On mac computers, this is the terminal application. You've actually already seen some of this when working through how to download lessons from Learn and GitHub onto your local computer! The command line serves as a low-level interpreter through which you, the user, can send commands directly to the computer. As a computer user, you previously have probably sent commands to the computer through a graphical user interface (GUI) such as a web browser, text editor, photo editor, or any other of the myriad of computer programs now in existence. While the command line is initially daunting with its cryptic looking text, we will quickly see some of its advantages.

## Objectives

You will be able to:

- Navigate between directories using the Bash shell


## Shell

To start, open up your shell program. For mac, this is the terminal, and for Windows we recommend git bash. Note that the "command prompt" on Windows may look similar but it is actually another language.

## Mac

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-bash-shell/master/images/mac_terminal.png)

## Windows

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-bash-shell/master/images/git_bash.png)

## Workflow Hints

When going back and forth between this lesson and your shell, it is useful to either use split screen or to know the shortcuts to switch between applications on your computer.

Shortcuts to change programs/applications:

- Mac: (cmd+tab)

- Windows: (alt+tab)

## pwd

Remember, **pwd** stands for **print working directory**. This is essential to determine where you are within the file structure.

## cd

From there, remember that **cd** stands for **change directory**. You can navigate to the home directory with `cd` alone, or go up one level with `cd ..`. You can also use the `~` symbol to refer to your home directory. For example, `cd ~/Documents` will take you to the Documents folder in your home directory no matter where you are.

## ls

You can use the **ls** command, which stands for **list files** to print all the files in the current working directory.

## Tab completion

Another useful feature when working on the command line is tab completion. This also works in many other programming environments such as Jupyter notebooks.

## Additional Resources

- [More Basic Shell Commands](http://www.ks.uiuc.edu/Training/Tutorials/Reference/unixprimer.html)
- [Linux Bash Man Page](https://linux.die.net/man/1/bash)
- [Detailed Bash](https://tiswww.case.edu/php/chet/bash/bashref.html)

## Summary

In this lesson, we reviewed some of the basic bash commands in order to navigate through files and folders on your computer. From here, we're ready to get started with Git, an important version control system used by many programmers, developers, and Data Scientists.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
