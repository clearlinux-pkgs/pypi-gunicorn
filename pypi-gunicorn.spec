#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-gunicorn
Version  : 21.2.0
Release  : 5
URL      : https://files.pythonhosted.org/packages/06/89/acd9879fa6a5309b4bf16a5a8855f1e58f26d38e0c18ede9b3a70996b021/gunicorn-21.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/06/89/acd9879fa6a5309b4bf16a5a8855f1e58f26d38e0c18ede9b3a70996b021/gunicorn-21.2.0.tar.gz
Summary  : WSGI HTTP Server for UNIX
Group    : Development/Tools
License  : MIT
Requires: pypi-gunicorn-bin = %{version}-%{release}
Requires: pypi-gunicorn-license = %{version}-%{release}
Requires: pypi-gunicorn-python = %{version}-%{release}
Requires: pypi-gunicorn-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cryptography)
BuildRequires : pypi(eventlet)
BuildRequires : pypi(gevent)
BuildRequires : pypi(packaging)
BuildRequires : pypi(pytest_cov)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Applications to test Django support:
testing -> Django 1.4

%package bin
Summary: bin components for the pypi-gunicorn package.
Group: Binaries
Requires: pypi-gunicorn-license = %{version}-%{release}

%description bin
bin components for the pypi-gunicorn package.


%package license
Summary: license components for the pypi-gunicorn package.
Group: Default

%description license
license components for the pypi-gunicorn package.


%package python
Summary: python components for the pypi-gunicorn package.
Group: Default
Requires: pypi-gunicorn-python3 = %{version}-%{release}

%description python
python components for the pypi-gunicorn package.


%package python3
Summary: python3 components for the pypi-gunicorn package.
Group: Default
Requires: python3-core
Provides: pypi(gunicorn)
Requires: pypi(packaging)

%description python3
python3 components for the pypi-gunicorn package.


%prep
%setup -q -n gunicorn-21.2.0
cd %{_builddir}/gunicorn-21.2.0
pushd ..
cp -a gunicorn-21.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1692065433
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-gunicorn
cp %{_builddir}/gunicorn-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-gunicorn/924d84267fe6376c699c87ac2f8b3fd4871b2250 || :
cp %{_builddir}/gunicorn-%{version}/NOTICE %{buildroot}/usr/share/package-licenses/pypi-gunicorn/1d1d5f8c928d82f6e23789fb64067b38fd394cf5 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gunicorn

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-gunicorn/1d1d5f8c928d82f6e23789fb64067b38fd394cf5
/usr/share/package-licenses/pypi-gunicorn/924d84267fe6376c699c87ac2f8b3fd4871b2250

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
