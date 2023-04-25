# Codeforces Round Fetcher

## Introduction

Codeforces is a project joining people interested in and taking part in programming contests. On one hand, Codeforces is a social network dedicated to programming and programming contests. On the other hand, it is a platform where contests are held regularly, the participant's skills are reflected by their rating and the former contests can be used to prepare. 

## Aim

Codeforces Round Fetcher pulls the _**next** codeforces round and its to be held date_ and displays a system notification regarding the details. It works best when the system is configured to run the script automatically on system startup.

## Table of Contents

> * [Title](#codeforces-round-fetcher)
> * [Introduction](#introduction)
> * [Aim](#aim)
> * [Usage](#usage)
> * [References](#references)

## Usage

### 1. Running the script

1. Install the mentioned libraries using pip. 

    ```bash
    pip install plyer
    pip install python-dateutil
    pip install requests
    ```

2. Run the python program either using any IDE or terminal.

    <img src="files/output-ubuntu.png">
    <img src="files/output-windows.png">

### 2. Configure script for startup

- ### Ubuntu

  1. Open [Startup Applications](https://help.ubuntu.com/stable/ubuntu-help/startup-applications.html.en).
  2. Click on **Add**.
  3. Fill the **Name** as CRF. In the **Command** enter `python3 /<path to>/CRF.py`.
  4. Click on **Save**.

- ### Windows

  1. Open **Run**.
  2. Search for **shell:startup**.
  3. Create a file **CRF.vbs**. Make sure the extension is `.vbs`.
  4. Enter the following script
  
      ```vbs
      Set oShell = CreateObject ("Wscript.Shell")
      Dim strArgs
      strArgs = "cmd /c python <path to>/CRF.py"
      oShell.Run strArgs, 0, false
      ```
      
  5. Save.

## References

1. [How to run a batch file without launching a "command window"?](https://superuser.com/a/140077)