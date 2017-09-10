#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pickleshare
Version  : 0.7.4
Release  : 6
URL      : http://pypi.debian.net/pickleshare/pickleshare-0.7.4.tar.gz
Source0  : http://pypi.debian.net/pickleshare/pickleshare-0.7.4.tar.gz
Summary  : Tiny 'shelve'-like database with concurrency support
Group    : Development/Tools
License  : MIT
Requires: pickleshare-legacypython
Requires: pickleshare-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Like shelve, a PickleShareDB object acts like a normal dictionary. Unlike shelve,
        many processes can access the database simultaneously. Changing a value in 
        database is immediately visible to other processes accessing the same database.
        
        Concurrency is possible because the values are stored in separate files. Hence
        the "database" is a directory where *all* files are governed by PickleShare.

%package legacypython
Summary: legacypython components for the pickleshare package.
Group: Default

%description legacypython
legacypython components for the pickleshare package.


%package python
Summary: python components for the pickleshare package.
Group: Default
Requires: pickleshare-legacypython

%description python
python components for the pickleshare package.


%prep
%setup -q -n pickleshare-0.7.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505055603
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1505055603
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
