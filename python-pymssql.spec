Summary:	A Python interface to MSSQL
Summary(pl):	Interfejs Pythona do MSSQL
Name:		pymssql
Version:	0.6.0
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://optusnet.dl.sourceforge.net/sourceforge/pymssql/pymssql-0.6.0.tar.gz
# Source0-md5:	eb51a4261a68fc4dfb19768f539da68e
URL:		http://pymssql.sourceforge.net/
Requires:	python >= 2.4
Requires:	python-libs >= 2.4
Requires:	freetds
Requires:	unixODBC
BuildRequires:	unixODBC-devel >= 2.2.9-2
BuildRequires:	freetds-devel >= 0.60
BuildRequires:  python-devel >= 2.4
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python interface to MSSQL

%description -l pl
Interfejs Pythona do MSSQL

%prep
%setup -q -n %{name}-%{version}

%build
env CFLAGS="%{rpmcflags}" %{_bindir}/python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python -- setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitescriptdir} \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PKG-INFO
%attr(755,root,root) %{py_sitescriptdir}/*.so
%{py_sitescriptdir}/*.py*
