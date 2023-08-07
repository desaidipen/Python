# # source_key = "usaa-mfp-dl-nfs-dev-dl0/mfp/dl0/test/infrastructure/mfp1/mfp_capability_1/spark_poc/small_file_3.csv"
# # source_key = "usaa-mfp-dl-nfs-dev-dl0/mfp/dl0/test/infrastructure/mfp1/mfp_capability_1/spark_poc/dropzone/small_file_3.csv"

# source_key = "mfp/dl0/test/infrastructure/mfp1/mfp_capability_1/spark_poc/small_file_3.csv"
# source_key = "mfp/dl0/test/infrastructure/mfp1/mfp_capability_1/spark_poc/dropzone/small_file_3.csv"
# print (f"1 >> source_key : {source_key}")

# file_path = source_key.split("/")
# print (f"2 >> file_path : {file_path}")

# if "dropzone" in file_path: file_path.remove("dropzone")
# print (f"2 - E >> file_path : {file_path}")

# archive_bucket_key = "/".join(map(str, file_path))
# print (f"3 >> archive_bucket_key : {archive_bucket_key}")

# file_path.insert(-1, "archive")
# print (f"4 >> file_path : {file_path}")

# archive_prefix_key = "/".join(map(str, file_path))
# print (f"5 >> archive_prefix_key : {archive_prefix_key}")


# source_key = "mfp/dl0/test/infrastructure/mfp1/mfp_capability_1/spark_poc/small_file_3.csv"
source_key = "mfp/dl0/test/infrastructure/mfp1/mfp_capability_1/spark_poc/dropzone/small_file_3.csv"
print (f"1 >> source_key : {source_key}")

file_path = source_key.split("/")[:-1]
print (f"2 >> file_path : {file_path}")

if "dropzone" in file_path: file_path.remove("dropzone")
print (f"3 >> file_path - E : {file_path}")

dropzone = "/".join(map(str, file_path))
print (f"4 >> dropzone : {dropzone}")

file_path.append("archive")
print (f"5 >> file_path - E : {file_path}")

arch = "/".join(map(str, file_path))
print (f"6 >> arch : {arch}")
