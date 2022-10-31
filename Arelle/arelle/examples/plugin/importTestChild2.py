'''
pluginPackages test case

See COPYRIGHT.md for copyright information.
'''
from arelle.Version import authorLabel, copyrightLabel

def foo():
    print ("imported unpackaged plug-in child 2")

__pluginInfo__ = {
    'name': 'Unpackaged Listed Import Child 2',
    'version': '0.9',
    'description': "This is a unpackaged child plugin.",
    'license': 'Apache-2',
    'author': authorLabel,
    'copyright': copyrightLabel,
    # classes of mount points (required)
    'Import.Unpackaged.Entry3': foo,
    # import plugins
    'import': ('importTestGrandchild1.py', 'importTestGrandchild2.py')
}
