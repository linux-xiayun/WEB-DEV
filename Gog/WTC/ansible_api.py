#!/usr/bin/env python
#coding: utf-8
import subprocess
import os


def popen(request):
    ansible_shell = "ansible %s -m win_ping" % request
    subprocess.call(ansible_shell, shell=True)

#if __name__ == "__main__":
#    popen("test_windows")