import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

datasource0 = glueContext.create_dynamic_frame.from_catalog(database = "cli_glueworkshop", table_name = "cli_csv", transformation_ctx = "datasource0")
applymapping1 = ApplyMapping.apply(frame = datasource0, mappings = [("uuid", "long", "uuid", "long"), ("country", "string", "country", "string"), ("item type", "string", "item_type", "string"), ("sales channel", "string", "sales_channel", "string"), ("order priority", "string", "order_priority", "string"), ("order date", "string", "order_date", "string"), ("region", "string", "region", "string"), ("ship date", "string", "ship_date", "string"), ("units sold", "long", "units_sold", "long"), ("unit price", "double", "unit_price", "double"), ("unit cost", "double", "unit_cost", "double"), ("total revenue", "double", "total_revenue", "double"), ("total cost", "double", "total_cost", "double"), ("total profit", "double", "total_profit", "double")], transformation_ctx = "applymapping1")
resolvechoice2 = ResolveChoice.apply(frame = applymapping1, choice = "make_cols", transformation_ctx = "resolvechoice2")
dropnullfields3 = DropNullFields.apply(frame = resolvechoice2, transformation_ctx = "dropnullfields3")
datasink4 = glueContext.write_dynamic_frame.from_jdbc_conf(frame = dropnullfields3, catalog_connection = "lab5-rds-connection", connection_options = {"dbtable": "sales", "database": "glueworkshop"}, transformation_ctx = "datasink4")

job.commit()
