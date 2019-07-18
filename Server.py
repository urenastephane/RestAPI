from pyspark import SparkConf, SparkContext                                                                                                                          
from pyspark.sql import SQLContext, SparkSession                                                                                                                     
from pyspark.sql.types import *                                                                                                                                      
from pyspark.sql.functions import col                                                                                                                                
from pyspark.ml.feature import *                                                                                                                                     
from pyspark.ml.regression import RandomForestRegressor, DecisionTreeRegressor                                                                                       
from pyspark.ml import *                                                                                                                                             
import time
from pyspark.sql.functions import from_unixtime, unix_timestamp
from pyspark.sql import Row
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.storagelevel import StorageLevel
import numpy as np
from pyspark.sql.functions import lit
from flask import Flask, abort, jsonify, request
conf=SparkConf().set('spark.executor.memory','8G').set('spark.driver.memory','8G').set('spark.executor.heartbeatInterval','100s')
sc = SparkContext().getOrCreate()
sqlContext=SQLContext(sc)
spark = SparkSession.builder.appName("testAPI").getOrCreate() 
print("------------- READING SERIALIZED TRANSFORMER AND MODEL --------------")                                                                                       
rfTransformerPipeline=PipelineModel.load("Transformer")                                                                                                          
rfModel=PipelineModel.load("Model")

app=Flask(__name__)

@app.route('/api',methods=['POST'])
def make_predict():
	data=request.get_json(force=True)
	test=Row(**data)
	data=sqlContext.createDataFrame([test])
	df=data\
	.withColumn("timestamp", unix_timestamp(col("date")))\
	.withColumn("time", from_unixtime(col("timestamp"), "H")*3600 + from_unixtime(col("timestamp"), "m")*60 + from_unixtime(col("timestamp"), "s"))\
	transformedTestData=rfTransformerPipeline.transform(DF)
	y_hat=rfModel.transform(transformedTestData)
	return str(y_hat.select("prediction").head()[0])

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=50111,debug=True)