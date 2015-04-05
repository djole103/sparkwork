import sys

sys.path.append("~/Builds/spark-1.3.0/python/pyspark/")
#from pyspark import *

lines = sc.textFile("data.txt")
