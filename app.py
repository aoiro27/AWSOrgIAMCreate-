import boto3
import sys

AWAS_ACCESSKEY = sys.argv[1]
AWS_SECRETKEY = sys.argv[2]
ACCOUNT_ID = sys.argv[3]
USERNAME = sys.argv[4]
PASSWORD = sys.argv[5]
RoleArn = "arn:aws:iam::" + ACCOUNT_ID + ":role/OrganizationAccountAccessRole"

sts = boto3.client('sts',aws_access_key_id=AWAS_ACCESSKEY, aws_secret_access_key=AWS_SECRETKEY)

assumedRoleObject = sts.assume_role( 
	RoleArn=RoleArn, 
	RoleSessionName='dummy_session', 
	) 
credentials = assumedRoleObject['Credentials'] 

iam = boto3.client(
	'iam', 
	aws_access_key_id = credentials['AccessKeyId'], 
	aws_secret_access_key = credentials['SecretAccessKey'], 
	aws_session_token = credentials['SessionToken'], 

)

try:
	iam.create_user(
		Path = '/',
		UserName = USERNAME
		)
except Exception as e:
	print(e)

iam = boto3.resource( 
	'iam', 
	aws_access_key_id = credentials['AccessKeyId'], 
	aws_secret_access_key = credentials['SecretAccessKey'], 
	aws_session_token = credentials['SessionToken'], 
) 

policy = iam.Policy('arn:aws:iam::aws:policy/AdministratorAccess')

policy.attach_user(
	UserName=USERNAME,
)

login_profile = iam.LoginProfile(USERNAME)

try:
	login_profile.create(
		Password = PASSWORD,
		PasswordResetRequired = False
	)
except Exception as e:
	print(e)