from setuptools import setup, find_packages

setup(
    name='jenkins_report',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'Flask',
        'dataset',
        'bokeh',
    ],
    scripts=['jenkins_report/scripts/jenkins_report_import_all.py'],
    package_data = {
        'jenkins_report': ['templates/*.html', 'templates/include/*html'],
    },
    data_files=[
        ('/usr/share/jenkins_report/static', [
         'jenkins_report/static/bootstrap.min.css',
         'jenkins_report/static/bootstrap.min.js',
        ]),
        ('/usr/share/jenkins_report/static/css', [
         'jenkins_report/static/css/bokeh.min.css',
        ]),
        ('/usr/share/jenkins_report/static/js', [
         'jenkins_report/static/js/bokeh.min.js',
        ]),
    ],
    zip_safe=False,
)
