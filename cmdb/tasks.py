#!/usr/bin/env python
#coding:utf-8
#__time__: 2020/4/8 0:28
#__author__ = 'ren_mcc'

from celery import task

@task
def mul(x, y):
    return x * y