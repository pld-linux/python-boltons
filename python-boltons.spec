#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	When they're not builtins, they're boltons
Summary(pl.UTF-8):	To, co nie jest wbudowane, jest w boltons
Name:		python-boltons
Version:	21.0.0
Release:	6
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/boltons/
Source0:	https://files.pythonhosted.org/packages/source/b/boltons/boltons-%{version}.tar.gz
# Source0-md5:	c7a17577f80a5c3316b8cb61b79d09c9
URL:		https://pypi.org/project/boltons/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Functionality that should be in the standard library. Like builtins,
but Boltons.

%description -l pl.UTF-8
Funkcjonalność, która powinna być w bibliotece standardowej, Podobnie
jak builtins, ale to są Boltons.

%package -n python3-boltons
Summary:	When they're not builtins, they're boltons
Summary(pl.UTF-8):	To, co nie jest wbudowane, jest w boltons
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-boltons
Functionality that should be in the standard library. Like builtins,
but Boltons.

%description -n python3-boltons -l pl.UTF-8
Funkcjonalność, która powinna być w bibliotece standardowej, Podobnie
jak builtins, ale to są Boltons.

%prep
%setup -q -n boltons-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest --doctest-modules boltons
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest --doctest-modules boltons
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md TODO.rst
%{py_sitescriptdir}/boltons
%{py_sitescriptdir}/boltons-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-boltons
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md TODO.rst
%{py3_sitescriptdir}/boltons
%{py3_sitescriptdir}/boltons-%{version}-py*.egg-info
%endif
