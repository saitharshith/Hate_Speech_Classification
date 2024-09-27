import setuptools

with open('README.md','r',encoding='utf-8') as f:
    long_description = f.read()

__version__ ='0.0.0'
repo_name='Hate_Speech_Classification'
author_user_name='saitharshith'
src_repo='Hate_Speech_Classification'
author_email='sai1726791@gmail.com'

setuptools.setup(
    name=repo_name,
    version=__version__,
    author=author_user_name,
    author_email=author_email,
    description='Hate Speech Detection',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f'https://github.com/{author_user_name}/{repo_name}',
    project_urls={
        'Bug Tracker': f'https://github.com/{author_user_name}/{repo_name}/issues'
    },
    package_dir={"","src"},
    packages=setuptools.find_packages(where='src')
)