#!/usr/bin/python3

import os
import consul
import argparse
from jinja2 import Environment, FileSystemLoader

'''
replacer_config = {
    consul_host: localhost
    consul_port: 8500
    consul_prefix: 
    templates_path: /tmp/templates/
}
'''

class Replacer(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        for key in kwargs:
            setattr(self, key.strip(), kwargs[key].strip())

    def consulSetup(self):
        try:
            cons = consul.Consul(self.consul_host, self.consul_port)
            keys = cons.kv.get(self.consul_prefix, recurse=True)
            kv_matrix = {}
            for key in keys[1]:
                kv_matrix[key['Key'].strip('/'+self.consul_prefix)] = key['Value'].decode()
            return kv_matrix
            
        except Exception as e:
            print(e)

    def renderTemplates(self):
        env = Environment(
            loader=FileSystemLoader(self.templates_path),
            trim_blocks=True
        )
        for template in env.list_templates():
            rendered_template = env.get_template(template).render(self.consulSetup())
            with open(self.templates_path+'/'+template, 'w') as f:
                f.write(rendered_template)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--consul_host', default='consul', dest="consul_host")
    parser.add_argument('-p', '--consul_port', default='8500', dest="consul_port")
    parser.add_argument('-c', '--consul_prefix', default='/', dest="consul_prefix")
    parser.add_argument('-t', '--templates_path', default='.', dest="templates_path")

    args = parser.parse_args()


    a = Replacer(consul_host=args.consul_host, 
        consul_port=args.consul_port, 
        consul_prefix=args.consul_prefix, 
        templates_path=args.templates_path)
    a.renderTemplates()