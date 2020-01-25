#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	File
%define		pnam	Slurp-Tiny
Summary:	File::Slurp::Tiny - A simple, sane and efficient file slurper [DISCOURAGED]
Summary(pl.UTF-8):	File::Slurp::Tiny - prosty, rozsądny i wydajny moduł do wciągania plików [ODRADZANY]
Name:		perl-File-Slurp-Tiny
Version:	0.004
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7575b81543281ea57cdb7e5eb3f73264
URL:		http://search.cpan.org/dist/File-Slurp-Tiny/
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides functions for fast and correct slurping and
spewing. All functions are optionally exported.

Note: this module is discouraged in favour of File::Slurper.

%description -l pl.UTF-8
Ten moduł udostępnia funkcje do szybkiego i poprawnego wciągania i
wypluwania. Wszystkie funkcje są eksportowane opcjonalnie.

Uwaga: ten moduł jest odradzany na rzecz modułu File::Slurper.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/File/Slurp
%{perl_vendorlib}/File/Slurp/Tiny.pm
%{_mandir}/man3/File::Slurp::Tiny.3pm*
