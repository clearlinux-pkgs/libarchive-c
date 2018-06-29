#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libarchive-c
Version  : 2.8
Release  : 17
URL      : http://pypi.debian.net/libarchive-c/libarchive-c-2.8.tar.gz
Source0  : http://pypi.debian.net/libarchive-c/libarchive-c-2.8.tar.gz
Summary  : Python interface to libarchive
Group    : Development/Tools
License  : CC0-1.0
Requires: libarchive-c-python3
Requires: libarchive-c-python
BuildRequires : libarchive-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://travis-ci.org/Changaco/python-libarchive-c.svg
:target: https://travis-ci.org/Changaco/python-libarchive-c

%package python
Summary: python components for the libarchive-c package.
Group: Default
Requires: libarchive-c-python3

%description python
python components for the libarchive-c package.


%package python3
Summary: python3 components for the libarchive-c package.
Group: Default
Requires: python3-core

%description python3
python3 components for the libarchive-c package.


%prep
%setup -q -n libarchive-c-2.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530278501
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
