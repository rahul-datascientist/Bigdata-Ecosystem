import sys

from pyspark import SparkContext, SparkConf

if __name__ == "__main__":

	conf = SparkConf().setAppName("Spark WordCount")
	sc = SparkContext(conf=conf)

	baseRDD = sc.textFile("/Sample")

	countRDD = baseRDD.flatMap(lambda l: l.split(" ")).map(lambda w: (w, 1)).reduceByKey(lambda a,b: a+b, 1)

	countRDD.saveAsTextFile("/PySparkOP1")

	sc.stop()