#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pickleshare
Version  : 0.7.5
Release  : 21
URL      : https://files.pythonhosted.org/packages/d8/b6/df3c1c9b616e9c0edbc4fbab6ddd09df9535849c64ba51fcb6531c32d4d8/pickleshare-0.7.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/d8/b6/df3c1c9b616e9c0edbc4fbab6ddd09df9535849c64ba51fcb6531c32d4d8/pickleshare-0.7.5.tar.gz
Summary  : Tiny 'shelve'-like database with concurrency support
Group    : Development/Tools
License  : MIT
Requires: pickleshare-python3
Requires: pickleshare-license
Requires: pickleshare-python
BuildRequires : buildreq-distutils3

%description
Like shelve, a PickleShareDB object acts like a normal dictionary. Unlike shelve,
        many processes can access the database simultaneously. Changing a value in 
        database is immediately visible to other processes accessing the same database.
        
        Concurrency is possible because the values are stored in separate files. Hence
        the "database" is a directory where *all* files are governed by PickleShare.

%package license
Summary: license components for the pickleshare package.
Group: Default

%description license
license components for the pickleshare package.


%package python
Summary: python components for the pickleshare package.
Group: Default
Requires: pickleshare-python3 = %{version}-%{release}

%description python
python components for the pickleshare package.


%package python3
Summary: python3 components for the pickleshare package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pickleshare package.


%prep
%setup -q -n pickleshare-0.7.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1537931781
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/pickleshare
cp LICENSE %{buildroot}/usr/share/doc/pickleshare/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/pickleshare/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
