%define realname    django-sorting

Name:		python-%{realname}
Version:	0.1
Release:	3
Summary:        A Django application for easy sorting
Group:          Development/Python
License:        BSD
URL:            https://files.pythonhosted.org/packages/source/d/django-sorting/django-sorting-%{version}.tar.gz
Source:         %{realname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel python-setuptools
Requires:       python-django

%description
Django-sorting allows for easy sorting, and sorting links generation
without modifying your views.

%prep
%autosetup -p1 -n %{realname}-%{version}
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

