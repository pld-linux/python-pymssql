Summary:	A Python interface to MSSQL
Summary(pl.UTF-8):	Interfejs Pythona do MSSQL
Name:		python-pymssql
Version:	0.8.0
Release:	4
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pymssql/pymssql-%{version}.tar.gz
# Source0-md5:	1526315e20f55a6c74c86d6ca0ce07c4
URL:		http://pymssql.sourceforge.net/
BuildRequires:	freetds-devel >= 0.63
BuildRequires:	python
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python interface to MSSQL.

%description -l pl.UTF-8
Interfejs Pythona do MSSQL.

%prep
%setup -q -n pymssql-%{version}

%build
env CFLAGS="%{rpmcflags}" %{_bindir}/%py_build

%install
rm -rf $RPM_BUILD_ROOT

python -- setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PKG-INFO
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py[co]
