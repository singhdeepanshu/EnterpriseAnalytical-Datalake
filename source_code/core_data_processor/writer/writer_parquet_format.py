class WriterParquetFormat:
    def write_dataframe(self, dataframe, column_names, partition_column, hdfs_path):
        #dataframe.select(column_names).write.partitionBy(partition_column).option("format", "parquet").save(hdfs_path)
        dataframe.select(column_names).write.partitionBy(partition_column).mode("append").parquet(hdfs_path)
        
        
