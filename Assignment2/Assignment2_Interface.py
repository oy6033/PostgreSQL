#!/usr/bin/python2.7
#
# Assignment2 Interface
#

import psycopg2
import os
import sys
# Donot close the connection inside this file i.e. do not perform openconnection.close()
def RangeQuery(ratingMinValue, ratingMaxValue, openconnection, outputPath):
    #Implement RangeQuery Here.
	con = openconnection
	cur = con.cursor()
	#query all the attribute from the RangeRatingsMetadata table
	cur.execute("select * from RangeRatingsMetadata;")
	#get all the rows from the table
	rows = cur.fetchall()
	for row in rows:
		PartitionNum = str(row[0])
		MinRating = float(row[1])
		MaxRating = float(row[2])
		RangeTableName = "RangeRatingsPart" + PartitionNum
		if(MinRating >= ratingMinValue and MaxRating <= ratingMaxValue):
			cur.execute("""select * from %s where rating >= %d and rating <=%d """
			% ())
			rows = cur.fetchall()
			try:
				f = open(outputPath,"a")
				for row in rows:
					f.write()
			except:
				print "file wirte error"
			finally:
				f.close()
			
		
	
    

def PointQuery(ratingValue, openconnection, outputPath):
    #Implement PointQuery Here.
    pass # Remove this once you are done with implementation
