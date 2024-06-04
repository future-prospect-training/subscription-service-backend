from setuptools import setup

setup(
    name='subscription-service-backend',
    version='1.0',
    author='Blagovest Davidov',
    description='A sample Python project',
    install_requires=[
        'flake8==7.0.0',
        'autopep8==2.1.0',
        'pytest==8.1.2',
        'Flask==3.0.3',  # For Flask-based setup
        'Flask-SQLAlchemy==3.1.1',
        'Flask-Migrate==4.0.7',
        'Flask-JWT-Extended==4.6.0',
        'psycopg2-binary==2.9.3',
        'marshmallow==3.14.1',
        'celery==5.2.3',
        'wheel==0.43.0',
        'python-dotenv==1.0.1',
        'Werkzeug==3.0.3'
    ]
)
