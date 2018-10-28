# ZmeiAppsAPI
# AKIAI2KG5GCGSOSE3Z4A
# 0xqelZ7VOUrnXERQX9y07ySyeA+9ObA1K5BL+XCV
import io
import os
import shutil
import sys
import zipfile
from glob import glob
from shutil import rmtree
from venv import EnvBuilder

import botocore
from botocore.exceptions import ClientError


def collect_files_and_site_packages():
    print('Archiving files')

    files = zipfile.ZipFile('out/lambda.zip', mode='w')

    # site packages
    site_packages = [x for x in sys.path if x.endswith('site-packages')][0]
    paths = set([x[len(site_packages) + 1:] for x in glob(f'{site_packages}/**/*', recursive=True)])

    for path in paths:
        if path.startswith('.'):
            continue
        # print(path)
        files.write(f'{site_packages}/{path}', arcname=path)

    # local files
    local_files = os.getcwd()
    paths = set([x[len(local_files) + 1:] for x in glob(f'{local_files}/**/*', recursive=True)])

    for path in paths:
        if path.startswith('out/'):
            continue

        print(f'{local_files}/{path}', path)
        if path.startswith('.'):
            continue
        files.write(f'{local_files}/{path}', arcname=path)

    files.close()

    print('Done.')


import boto3

iam_client = boto3.client('iam')
lambda_client = boto3.client('lambda')

role = iam_client.get_role(RoleName='lambda_basic_execution')

env_variables = {
    'DJANGO_SETTINGS_MODULE': 'app.settings_aws'
}

if os.path.exists('out/env'):
    rmtree('out/env')

os.system('pip install -r requirements.txt -t out/env --src out/env --compile') # --ignore-installed
os.system('rm -rf out/env/{*.dist-info,bin,wheel}')
os.system('rsync -rv --exclude=out --exclude=.* ./ out/env/')
#
# shutil.make_archive('out/lambda', 'zip', 'out/env')
#
# with open('out/lambda.zip', 'rb') as f:
#     zipped_code = f.read()
#
# try:
#     lambda_client.create_function(
#         FunctionName='django_test',
#         Runtime='python3.6',
#         Role=role['Role']['Arn'],
#         Handler='lambda.lambda_handler',
#         Code=dict(ZipFile=zipped_code),
#         Timeout=300,  # Maximum allowable timeout
#         Environment=dict(Variables=env_variables),
#     )
# except ClientError as e:
#     lambda_client.update_function_code(
#         FunctionName='django_test',
#         ZipFile=zipped_code,
#         Publish=True
#     )
#
#     # env_variables = dict() # Environment Variables
#     # with open('lambda.zip', 'rb') as f:
#     #   zipped_code = f.read()
