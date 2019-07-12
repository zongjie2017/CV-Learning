#!/usr/bin/env python
# coding: utf-8
import cv2
import numpy as np
#导入Lena.jpg
img = cv2.imread('lena.jpg', 0)
cv2.imshow('lena', img)
key = cv2.waitKey()
if key == 27:
    cv2.destroyAllWindows()
#固定值填充 : 填零
cons = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value = 0)
median_3 = cv2.medianBlur(cons, 3)
cv2.imshow('median_lena', median_3)
key = cv2.waitKey()
if key == 27: 
    cv2.destroyAllWindows()
#固定值填充：填零 and 5X5
cons = cv2.copyMakeBorder(img, 2, 2, 2, 2, cv2.BORDER_CONSTANT, value = 0)
median_5 = cv2.medianBlur(cons, 5)
cv2.imshow('median_lena', median_5)
key = cv2.waitKey()
if key == 27: 
    cv2.destroyAllWindows()
#固定值填充： REPLICATE aaaaa/abcdefgh/hhhhhh
cons = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_REPLICATE)
median_3 = cv2.medianBlur(cons1, 3)
cv2.imshow('median_lena', median_3)
key = cv2.waitKey()
if key == 27: 
    cv2.destroyAllWindows()
cons = cv2.copyMakeBorder(img, 2, 2, 2, 2, cv2.BORDER_REPLICATE)
median_5 = cv2.medianBlur(cons, 5)
cv2.imshow('median_lena', median_5)
key = cv2.waitKey()
if key == 27: 
    cv2.destroyAllWindows()
