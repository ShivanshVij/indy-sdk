from distutils.core import setup
import os

PKG_VERSION = os.environ.get('PACKAGE_VERSION') or '1.10.0'

TEST_DEPS = [
    'pytest<3.7', 'pytest-asyncio', 'base58'
]

setup(
    name='python3-indy',
    version=PKG_VERSION,
    packages=['indy'],
    url='https://github.com/hyperledger/indy-sdk',
    license='MIT/Apache-2.0',
    author='Vyacheslav Gudkov',
    author_email='vyacheslav.gudkov@dsr-company.com',
    description='This is the official SDK for Hyperledger Indy (https://www.hyperledger.org/projects), which provides a distributed-ledger-based foundation for self-sovereign identity (https://sovrin.org). The major artifact of the SDK is a c-callable library.',
    install_requires=['base58'],
    tests_require=TEST_DEPS,
    extras_require={
        'test': TEST_DEPS
    }
)
