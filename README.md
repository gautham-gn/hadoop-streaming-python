**Hadoop Streaming using Python**   

The task is on running a MapReduce program using Python in Hadoop Cluster. Follow the below mentioned steps to perform Hadoop streaming.  

1. Login to Hadoop Cluster using your credentials.
2. Run Command  
``git clone https://github.uc.edu/gondinm/hadoop-streaming.git``    
3. The above commands creates a directory in file system.  
4. Go inside the directory by using change directory.  
``cd hadoop-streaming``  
5. You will see mapper and reducer scripts inside the directory.  
6. Now, run the following command to run map reduce on new york city traffic accidents data.  
``hadoop jar /usr/hdp/2.6.3.0-235/hadoop-mapreduce/hadoop-streaming-2.7.3.2.6.3.0-235.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input /data/nyc/nyc-traffic.csv -output /user/gondinm/pyOut/``  
7. The log for running above code and the output file has been pushed into this repository as RunLog.txt and Outputfile.  
8. Now, once the command gets executed it creates a pyOut directory in the hadoop cluster. Copy it to local directory using:  
``hadoop fs -get /user/gondinm/pyOut /home/gondinm/pyOut``  
9. Go inside the pyOut directory and check part_0000 file to view the output of the code.  
