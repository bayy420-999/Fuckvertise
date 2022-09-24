from setuptools import setup, find_packages

setup(
    name = 'Fuckvertise',
    version = '1.0.0',
    description = 'Fuck that annoying shortlink! Powered by `bypass.vip`',
    author = 'Bayu Aji',
    author_email = 'getkilla5@gmail.com',
    url = 'https://github.com/bayy420-999/Fuckvertise',
    packages = find_packages(),
    install_require = ['requests', 'urllib', 'colorama'],
    keywords = ['python', 'shortlink', 'bypass', 'linkvertise'],
    entry_points = {
        'console_scripts': [
            'Fuckvertise = Fuckvertise.main:main',
        ]
    }
)