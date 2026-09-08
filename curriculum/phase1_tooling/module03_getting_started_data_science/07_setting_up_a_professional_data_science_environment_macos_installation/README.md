# Setting up a Professional Data Science Environment - MacOS Installation

> Part of **Topic 1: Getting Started with Data Science** · source item type: WikiPage

---
## Introduction

There are two major pieces we need to install in order to set you up for success as a professional data scientist! In this lesson, we will be installing Git and Anaconda for MacOS.

## Objectives

You will be able to:

- Install Git

- Install Anaconda

Please note - the exact names and versions will change over time.

## Installing Git

If you are comfortable with the command line and have installed [homebrew](https://brew.sh/), you should install Git by running the command `brew install git` in a terminal window. If you have no idea what that last sentence meant, please disregard and follow the below steps.

### Overview

Please also reference the image screengrabs for more detail below.

1. Navigate to Git's download page for MacOS [here](https://git-scm.com/download/mac). Since you are not using homebrew, you should click on the latest version number under the Binary Installer option
  - This should take you to another page, where the download of the installer dmg file should begin automatically after a few seconds

2. Double click on the downloaded dmg file to open a small Finder window
3. Double click on the .pkg file to run it, and click "Open" when the pop-up security warning asks if you are sure you want to open it
  - If you get a security warning that simply says the file cannot be opened because it is from an unidentified developer, then:
    - Click on the Apple symbol at the top left of your screen
    - Select “System Preferences” from the drop-down menu
    - Select “Security and Privacy”
    - Select the “General” tag
    - Below the “Allow apps downloaded from” option, click the "Open Anyway" option. You may need to click the lock to make changes, which will prompt you to enter your password

4. When the Installer opens, click "Continue" on each screen, then "Install"
  - You may need to enter your password when prompted

5. When the installation is complete, click the "Close" button
  - If the installation window asks if you want to move the installer .pkg file to trash, you can click “Move to Trash”

#### Git Installation Step-by-Step:

Step 1: Git’s download page for MacOS - choose the Binary Installer option (click the version number)

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-data-science-env-mac-installation/master/images/mac-git-download-latestversionboxed.png)

Download the Git .dmg file from the new site (download should begin automatically after a few seconds)

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-data-science-env-mac-installation/master/images/mac-git-download-sourceforgedownloadpage.png)

Step 2: Open the downloaded .dmg file

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-data-science-env-mac-installation/master/images/mac-git-openeddmg.png)

Step 3: Open the downloaded .pkg file inside the .dmg file

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-data-science-env-mac-installation/master/images/mac-git-openpkg.png)

You may need to work around a security warning. If you see this:

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-data-science-env-mac-installation/master/images/mac-git-pkgcannotbeopened.png)

Go to your Security & Privacy menu and click "Open Anyway"

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-data-science-env-mac-installation/master/images/mac-git-openpkganyway.png)

Step 4: Move through the Installer, clicking "Continue" on each screen to stick with the default options, then click "Install"

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-data-science-env-mac-installation/master/images/mac-git-installation-intro.png)

Step 5: Installation Complete! Click “Close”

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-data-science-env-mac-installation/master/images/mac-git-installation-successful.png)

If the installation window asks if you want to move the installer .pkg file to trash, you can click “Move to Trash”

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-data-science-env-mac-installation/master/images/mac-git-moveinstallertotrash.png)

### Confirming Your Git Installation

To confirm you have installed Git successfully:

1. Open a terminal window

```python
- When we ask you to use the terminal, we mean the “Terminal” app in the “Utilities” folder within your “Applications” folder - or, find the "Terminal" app in your Launchpad (often found in a subdirectory named "Other")
```

1. Type `git --version`: It should return the version of git you are running

---

## Installing Anaconda

The easiest way to get set up with Python and Jupyter Notebook so you can start coding is to install the Anaconda distribution.

### Overview:

Please also reference the image screengrabs for more detail below.

1. Download the latest version of Anaconda [here](https://www.anaconda.com/products/individual)
2. Open the pkg file once it has downloaded to open the Anaconda installer
3. Click "Continue" to run the package to determine if the software can be installed
4. When the Installation window opens, click "Continue"
5. Read the Read Me, then click "Continue"
6. Accept the license by clicking "Continue", then click "Agree" in the pop-up window
7. Click "Install" to install the software
  - You may need to enter your password when prompted
  - You can ignore any supplementary materials advertised, such as PyCharm

8. Click "Close" when the installation was completed successfully
  - If the installation window asks if you want to move the installer .pkg file to trash, you can click “Move to Trash”

#### Anaconda Installation Steps, step-by-step:

Step 1: Download Anaconda, choosing the 64-bit GUI option

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-data-science-env-mac-installation/master/images/mac-anaconda-download-64bitgui.png)

Step 2: Open the downloaded .pkg file

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-data-science-env-mac-installation/master/images/mac-anaconda-openpkg.png)

Step 3: Click "Continue" to determine if the package can be installed

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-data-science-env-mac-installation/master/images/mac-anaconda-installation-determineinstall.png)

Step 4: Installer - click "Continue"

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-data-science-env-mac-installation/master/images/mac-anaconda-installation-intro.png)

Step 5: Read the Read Me, then click "Continue"

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-data-science-env-mac-installation/master/images/mac-anaconda-installation-readme.png)

Step 6: Accept the license by clicking "Continue", then click "Agree" in the pop-up window

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-data-science-env-mac-installation/master/images/mac-anaconda-installation-agreelicense.png)

Step 7: Install

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-data-science-env-mac-installation/master/images/mac-anaconda-installation.png)

You can ignore any supplementary pages, such as this advertisement for PyCharm

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-data-science-env-mac-installation/master/images/mac-anaconda-pycharm.png)

Step 8: Installation Complete! Click "Close"

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-data-science-env-mac-installation/master/images/mac-anaconda-installation-successful.png)

If the installation window asks if you want to move the installer .pkg file to trash, you can click “Move to Trash”

### Confirming Your Anaconda Installation

To confirm you have installed Anaconda successfully:

1.

Open a terminal window
2.

Type `conda info`: It should return a table of details about your conda installation

## Confirmation

This image shows what it should look like when you confirm both your Git and Anaconda installs (although version numbers and details may change):

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-data-science-env-mac-installation/master/images/mac-confirm-install.png)

## Summary

Congratulations! If you've gotten this far and everything has worked, you have successfully installed Git and Anaconda on your Mac!

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
