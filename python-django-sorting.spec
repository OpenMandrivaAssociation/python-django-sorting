%define realname    django-sorting
%define name	    python-%{realname}
%define version 0.1
%define release %mkrel 1

Name: %{name}
Version: %{version}
Release: %{release}
Summary:        A Django application for easy sorting
Group:          Development/Python
License:        BSD
URL:            http://pypi.python.org/pypi/django-sorting
Source:         %{realname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
BuildRequires:  python-devel python-setuptools
Requires:       python-django

%description
Django-sorting allows for easy sorting, and sorting links generation
without modifying your views.

%prep
%setup -q -n %{realname}-%{version}
find . -name \*._* -exec rm {} +
find . -name \*.buildinfo* -exec rm {} +

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{py_puresitedir}/*



%changelog
* Tue Nov 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.1-1mdv2011.0
+ Revision: 591973
- import python-django-sorting

