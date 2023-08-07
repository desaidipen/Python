a = "s3://epic-device-farm-assets20230802203856277300000001/test-assets/AWSDeviceFarmAndroidReferenceApp.apk"

print (f'0 > Full String: {a}')

b = a.split("/")
print (f'Bucket: {b[2]}')

c = b[3:]
print (f'Keys List: {c}')

d = "/".join(b[3:])
print (f'Key FINAL: {d}')