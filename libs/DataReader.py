def read_lendingClub(spark,env):
        conf = ConfigReader.get_app_conf(env)
        lendingClub_file_path = conf["lendingClub.file.path"]
     return spark.read \
             .format("csv") \
             .option("header","true") \
             .schema(get_lendingClub_schema()) \
             .load(lendingClub_file_path)
