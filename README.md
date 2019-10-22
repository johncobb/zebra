# Maintaining ZPL Teplates

## Table of contents
- [Overview](#overview)
- [Prerequisites](#prereq)
- [Examples](#examples)
- [References](#references)

<div id='overview'/>
In order to efficiently modify the design of a label it is important to setup an efficient workflow. The repetitive nature of this mind numbing task can be challenging. This article will help you setup the most efficient workflow to accomplish this task.

<div id='prereq'/>

## Prerequisites:

 - Install Python
 - Install USB/Serial bus
 - Install Null Modem cable


 <div id='examples'/>

## Examples

### Modify the ZPL to match your desired layout
The command below will upload the required script files
```console
scp -P 2022 format_label.py printme pi@10.0.0.224:~/pyprint
```


### Test the new label format by executing the command below
The command below will upload the required script files
```console
./printme
```
 
