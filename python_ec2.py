#!/usr/bin/python

import boto.ec2

conn = boto.ec2.connect_to_region("ap-south-1")

conn.run_instances(
          image_id='ami-f9daac96',
           key_name='ChefAll',
           instance_type='t2.micro',
           security_groups=['ChefServer']
               )
